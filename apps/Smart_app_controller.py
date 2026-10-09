# ─────────────── Functies ─────────────── #

def aantal_dagen(inputFile):

    with open(inputFile, "r") as f:
        next(f)
        regels = f.readlines()

        return (len(regels))

def auto_bereken(inputFile, outputFile):

    with open(inputFile, "r") as f:
        next(f)
        regels = f.readlines()

    with open(outputFile, "w") as f:

        for regel in regels:
            waarden = regel.split()

            date = waarden[0]
            numPeople = int(waarden[1])
            tempSetpoint = float(waarden[2])
            tempOutside = float(waarden[3])
            precip = float(waarden[4])

            verschil = tempSetpoint - tempOutside

            if verschil >= 20:
                cv = 100
            elif verschil >= 10:
                cv = 50
            else:
                cv = 0

            if numPeople < 4:
                ventilatie = numPeople + 1
            else:
                ventilatie = 4

            bewatering = precip < 3

            f.write(f"{date};{cv};{ventilatie};{bewatering}\n")

def overwrite_settings(outputFile):
    datum = input("Wat is de datum? (Gescheiden met -): ")
    systeem = input("Welk systeem wil je kiezen (1: CV ketel, 2: ventilatie, 3: bewatering)?: ")

    try:
        systeem = int(systeem)
    except ValueError:
        return -3

    if systeem not in [1, 2, 3]:
        return -3

    waarde = input("Met welke waarde moet hij overschreven worden?: ")

    try:
        waarde = int(waarde)
    except ValueError:
        return -3

    if systeem == 1:
        if not 0 <= waarde <= 100:
            return -3

    elif systeem == 2:
        if not 0 <= waarde <= 4:
            return -3

    elif systeem == 3:
        if waarde not in [0, 1]:
            return -3

    with open(outputFile, "r") as f:
        regels = f.readlines()

    gevonden = False

    for i in range(len(regels)):
        onderdelen = regels[i].strip().split(";")

        if onderdelen[0] == datum:
            gevonden = True

            if systeem == 1:
                onderdelen[1] = str(waarde)
            elif systeem == 2:
                onderdelen[2] = str(waarde)
            elif systeem == 3:
                onderdelen[3] = str(waarde == 1)

            regels[i] = ";".join(onderdelen) + "\n"

    if not gevonden:
        return -1

    with open(outputFile, "w") as f:
        f.writelines(regels)

    return 0


# ───────────── Hoofdfunctie ───────────── #

def smart_app_controller():
    print(
        " " "\n" "▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱" "\n" "                Smart App Controller" "\n" "────────────────── ⋆⋅☆⋅⋆ ──────────────────" "\n" " ")
    print("Welkom bij Smart App Controller! Wat wil je doen?")

    print("1. Ik wil weten hoeveel dagen er zijn opgeslagen.")
    print("2. Ik wil alle actuatoren automatisch laten berekenen en naar het uitvoerbestand schrijven.")
    print("3. Ik wil een waarde overschrijven in het uitvoerbestand.")
    print("4. Ik wil stoppen.")

    while True:

        keuze = input("Voer een cijfer in (1-4): ")

        try:
            keuze = int(keuze)

            if keuze == 1:
                dagen = aantal_dagen("data.txt")
                print(f"Er zijn {dagen} opgeslagen.")
                continue

            elif keuze == 2:
                auto_bereken("data.txt", "output.txt")
                print("De actuatoren zijn automatisch berekend en opgeslagen.")
                continue

            elif keuze == 3:
                resultaat = overwrite_settings("output.txt")
                if resultaat == 0:
                    print("Waarde succesvol overschreven.")
                elif resultaat == -1:
                    print("Deze datum bestaat niet.")
                elif resultaat == -3:
                    print("Ongeldige invoer.")
                continue

            elif keuze == 4:
                print("Je wordt teruggestuurd naar het hoofdmenu. Tot ziens!")
                print("")
                print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
                print("           Hoofdmenu")
                print("───────────" "── ⋆⋅☆⋅⋆ ──" "───────────")
                print(" Optie 1: Weerstation ")
                print(" Optie 2: Smart App Controller ")
                print(" Optie 3: Sluiten ")
                print(" " "\n" "───────────" "── ⋆⋅☆⋅⋆ ──" "───────────")

                break

            else:
                print("Ongeldige invoer! Probeer het opnieuw.")
                continue

        except ValueError:
            print("Dat is geen cijfer! Probeer het opnieuw.")
            continue