# ───────────── Easter Egg ───────────── #
godzilla = "    ⠀⠀⠀⠀⠀⠀⠀⡰⠀⠀⠀⠀⠀⢀⠀⢀⣠⠂⠀⢀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀" "\n" "    ⠀⠀⠀⠀⠀⣀⣼⠃⢀⢠⣄⣾⣶⣿⣆⣾⣿⢂⣶⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀" "\n" "    ⠀⠀⠀⢠⣶⡿⠃⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢁⣴⣤⣾⣤⣶⠞⠁⠀" "\n" "    ⠀⠀⣬⣾⡿⠁⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡥⠀⠀⠀" "\n" "    ⠀⣠⣿⣿⠃⠀⢸⣿⡟⣿⠟⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀" "\n" "    ⢠⣾⣿⡟⠀⠀⠀⠿⠁⠿⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣷⣖⣀⣀" "\n" "    ⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉⠁" "\n" "    ⢺⣿⣿⣇⠀⠀⠀⠀⠀⠀⡠⢾⣿⠟⠉⠉⢸⣿⣿⣿⣿⣿⣿⣿⣿⣏⡉⠀⠀⠀" "\n" "    ⢨⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠁⠃⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡆⠀⠀" "\n" "    ⠘⢿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠙⠋⠉⠁⠀" "\n" "    ⠺⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀" "\n" "    ⠀⠀⠠⣿⣿⣿⣿⣿⣿⣶⣦⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠈⠈⠀⠀⠀⠀" "\n" "    ⠀⠀⠀⠈⠩⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠻⠀⠀⠀⠀⠀⠀⠀" "\n" "    ⠀⠀⠀⠀⠀⠀⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠻⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀" "\n" "    ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠙⠉⠀⠘⠁⠀" "\n"

# ───────────── Imports ───────────── #

from apps.Weerstation import weerstation
from apps.Smart_app_controller import smart_app_controller

# ───────────── Keuzemenu ───────────── #

while True:

    print("")
    print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
    print("           Hoofdmenu")
    print("───────────" "── ⋆⋅☆⋅⋆ ──" "───────────")
    print(" Optie 1: Weerstation ")
    print(" Optie 2: Smart App Controller ")
    print(" Optie 3: Sluiten ")
    print(" " "\n" "───────────" "── ⋆⋅☆⋅⋆ ──" "───────────")

    keuze = input("Welke optie wil je kiezen? (1-3): ")

    if keuze == "godzilla":
        print("\033[1m" " ─────────── " "RAAAWR! 🦖" " ─────────── " "\033[0m")
        print(godzilla)
        continue

    try:
        keuze = int(keuze)

    except ValueError:
        print("Ongeldige invoer, probeer het opnieuw.")
        continue

    if keuze == 1:
        print("Je hebt gekozen voor optie 1: Weerstation!")
        weerstation()
        continue

    elif keuze == 2:
        smart_app_controller()
        continue

    elif keuze == 3:
        print("Tot ziens!")
        break

    else:
        print("Ongeldige invoer, probeer het opnieuw.")
        continue