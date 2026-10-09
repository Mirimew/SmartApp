# ───────────── Imports ───────────── #

import datetime
import locale
import openmeteo_requests

try:
    locale.setlocale(locale.LC_TIME, "nl_NL.UTF-8")
except locale.Error:
    locale.setlocale(locale.LC_TIME, "dutch")

x = datetime.datetime.now()
openmeteo = openmeteo_requests.Client() # Voor OpenMeteo heb ik wel AI gebruikt, want ik kwam er niet uit.

steden = { # Ik ben van plan om nog meer steden toe te voegen.
    "utrecht": (52.09, 5.12),
    "eindhoven": (51.44, 5.47),
    "enschede": (52.21, 6.89),
    "amsterdam": (52.37, 4.89),
    "rotterdam": (51.92, 4.47),
    "emmen": (52.79, 6.89),
    "zwolle": (52.51, 6.08),
    "hogeschool utrecht": (52.08, 5.18)
}

# ───────────── Functies ───────────── #

def fahrenheit(temperatuur):
    return 32 + 1.8 * temperatuur

def gevoelstemperatuur(temperatuur, windsnelheid, luchtvochtigheid):
    return temperatuur - luchtvochtigheid / 100 * windsnelheid

def weerrapport(temperatuur, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temperatuur, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return("Het is heel koud en het stormt! Verwarming helemaal aan!")
    elif gevoel < 0 and windsnelheid <= 10:
        return("Het is behoorlijk koud! Verwarming aan op de benedenverdieping!")
    elif gevoel >= 0 and gevoel < 10 and windsnelheid > 12:
        return("Het is best koud en het waait; verwarming aan en roosters dicht!")
    elif gevoel >= 0 and gevoel < 10 and windsnelheid <= 12:
        return("Het is een beetje koud, elektrische kachel op de benedenverdieping aan!")
    elif gevoel < 22:
        return("Heerlijk weer, niet te koud of te warm.")
    else:
        return("Warm! Airco aan!")

def actueel_weer(breedtegraad, lengtegraad):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": breedtegraad,
        "longitude": lengtegraad,
        "daily": ["temperature_2m_mean", "wind_speed_10m_max", "relative_humidity_2m_mean"],
        "wind_speed_unit": "ms",
        "timezone": "auto",
        "forecast_days": 7,
    }
    response = openmeteo.weather_api(url, params=params)[0]
    daily = response.Daily()

    temperaturen = daily.Variables(0).ValuesAsNumpy()
    windsnelheden = daily.Variables(1).ValuesAsNumpy()
    luchtvochtigheden = daily.Variables(2).ValuesAsNumpy()

    return [
        (float(t), float(w), int(round(float(lv))))
        for t, w, lv in zip(temperaturen, windsnelheden, luchtvochtigheden)
    ]

# ───────────── Hoofdfunctie ───────────── #
def weerstation():
    opgegeven_temperaturen = []

    print(" " "\n" "▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱" "\n" "                Weerstation" "\n" "────────────────── ⋆⋅☆⋅⋆ ──────────────────" "\n" " ")
    print(x.strftime("Welkom bij het weerstation!" "\n" "Het is vandaag %A %d %B, %H:%M uur." "\n"))
    print("Wil je:")

    print("\033[94m")
    print("1. De gegevens inzien van een stad?")
    print("2. Zelf een weerrapport ophalen?")
    print("3. Terug naar het hoofdmenu?")
    print("\033[98m")

    keuze = input("")

    if keuze == "1":
        print("Beschikbare steden: " + ", ".join(s.capitalize() for s in steden))
        stad = input("Voor welke stad wil je het weer? ").strip().lower()

        if stad == "":
            print("           Tot ziens!")
            print("───────────" "── ⋆⋅☆⋅⋆ ──" "───────────")
            return

        if stad not in steden:
            print("Die stad is niet beschikbaar.")
            return

        try:
            weer_per_dag = actueel_weer(*steden[stad])
        except Exception as fout:
            print(f"Kon het weer niet ophalen. (Internetverbinding?): {fout}")
            return

        for dag, (temperatuur, windsnelheid, luchtvochtigheid) in enumerate(weer_per_dag):
            datum = x + datetime.timedelta(days=dag)
            dagnaam = datum.strftime("%A").capitalize()

            opgegeven_temperaturen.append(temperatuur)
            gemiddelde = sum(opgegeven_temperaturen) / len(opgegeven_temperaturen)

            print(f"{dagnaam}: {temperatuur:.1f}°C ({fahrenheit(temperatuur):.2f}°F), "
                  f"wind {windsnelheid:.1f} m/s, luchtvochtigheid {luchtvochtigheid}%")

            print(weerrapport(temperatuur, windsnelheid, luchtvochtigheid))
            print(f"De gemiddelde temperatuur tot nu toe is: {gemiddelde:.1f}°C")
            print("================")

    elif keuze == "2":
        for dag in range(1, 8):
            temperatuur = input(f"Wat is op dag {dag} de temperatuur in °C?: ")

            if temperatuur == (""):
                print("           Tot ziens!")
                print("───────────" "── ⋆⋅☆⋅⋆ ──" "───────────")
                break

            if temperatuur == ("godzilla"): # Easter Egg
                print("\033[1mRAAAWR! 🦖\033[0m")
                print("")
                print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
                print("           Hoofdmenu")
                print("───────────" "── ⋆⋅☆⋅⋆ ──" "───────────")
                print(" Optie 1: Weerstation ")
                print(" Optie 2: Smart App Controller ")
                print(" Optie 3: Sluiten ")
                print(" " "\n" "───────────" "── ⋆⋅☆⋅⋆ ──" "───────────")
                break

            temperatuur = float(temperatuur)
            opgegeven_temperaturen.append(temperatuur)

            windsnelheid = float(input(f"Wat is op dag {dag} de windsnelheid in m/s?: "))
            luchtvochtigheid = int(input("Wat is de luchtvochtigheid? "))
            gemiddelde = sum(opgegeven_temperaturen) / len(opgegeven_temperaturen)

            print(f"Het is vandaag {temperatuur}°C ({fahrenheit(temperatuur):.2f}°F).")
            print(weerrapport(temperatuur, windsnelheid, luchtvochtigheid))
            print(f"De gemiddelde temperatuur vandaag is: {gemiddelde}")
            print("================")

    elif keuze == "3":
        print("           Tot ziens!")
        print("───────────" "── ⋆⋅☆⋅⋆ ──" "───────────")
        return

    else:
        print("Dat is geen geldige keuze! Kies 1, 2 of 3.")

# ───────────── End ───────────── #