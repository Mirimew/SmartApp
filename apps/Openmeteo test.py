# OpenMeteo API commentaar aangeleverd met hashtags.

# pip install openmeteo-requests

import openmeteo_requests

openmeteo = openmeteo_requests.Client()

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"hourly": ["temperature_2m", "precipitation", "wind_speed_10m"],
	"current": ["temperature_2m", "relative_humidity_2m"],
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation: {response.Elevation()} m asl")
print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

# Process current data. The order of variables needs to be the same as requested.
current = response.Current()
current_temperature_2m = current.Variables(0).Value()
current_relative_humidity_2m = current.Variables(1).Value()

print(f"Current time: {current.Time()}")
print(f"Current temperature_2m: {current_temperature_2m}")
print(f"Current relative_humidity_2m: {current_relative_humidity_2m}")

""" Pre-Meteo Weerstation:

# ───────────── Imports ───────────── #

import datetime
import locale

try:
    locale.setlocale(locale.LC_TIME, "nl_NL.UTF-8")
except locale.Error:
    locale.setlocale(locale.LC_TIME, "dutch")

x = datetime.datetime.now()

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

# ───────────── Hoofdfunctie ───────────── #
def weerstation():
    opgegeven_temperaturen = []

    print(" " "\n" "▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱" "\n" "                Weerstation" "\n" "────────────────── ⋆⋅☆⋅⋆ ──────────────────" "\n" " ")
    print(x.strftime("Welkom bij het weerstation!" "\n" "Het is vandaag %A %d %B, %H:%M uur." "\n"))

    for dag in range(1, 8):
        temperatuur = input(f"Wat is op dag {dag} de temperatuur in °C?: ")

        if temperatuur == (""):
            print("           Tot ziens!")
            print("───────────" "── ⋆⋅☆⋅⋆ ──" "───────────")
            break

        if temperatuur == ("godzilla"):
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

# ───────────── End ───────────── #

#weerstation()

"""