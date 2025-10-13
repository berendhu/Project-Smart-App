def aantal_dagen(inputFile):
    try:
        with open(inputFile, "r") as f:
            regels = f.readlines()
        return len(regels) - 1
    except FileNotFoundError:
        print(f"Bestand '{inputFile}' niet gevonden")
        return 0
    except Exception as e:
        print(f"Onverwachte fout bij lezen van bestand: {e}")


def auto_bereken(inputFile, outputFile):
    try:
        with open(inputFile, "r") as f:
            regels = f.readlines()[1:] #sla kolomnamen over
    except FileNotFoundError:
        print(f"bestand '{inputFile}'niet gevonden. ")
        return

    uitvoer = []

    for regel in regels:
        try:
            datum, personen, setpoint, buiten, neerslag = regel.strip().split()
            personen, setpoint, buiten, neerslag = int(personen), float(setpoint), float(buiten), float(neerslag)
        except ValueError:
            print(f"Ongeldige regel overgeslagen: {regel.strip()}")
            continue

        #cv ketel logica
        verschil = setpoint - buiten
        if verschil >= 20:
            cv = 100
        elif verschil >= 10:
            cv = 50
        else:
            cv = 0

        #ventilatie logica
        ventilatie = min(personen + 1, 4)

        #bewatering logica
        bewatering = neerslag < 3

        uitvoer.append(f"{datum}; {cv};{ventilatie};{bewatering}")

    try:
        with open(outputFile, "w") as f:
            for regel in uitvoer:
                f.write(regel + "\n")
                print("Actuatoren berekend en opgeslagen")
    except Exception as e:
                print(f"Fout bij schrijven naar bestand: {e}")

def overwrite_settings(outputFile):
    datum = input("Voer een datum in (bijv. 08-10-2024): ")
    systeem = input("Kies een systeem (1=CV, 2=ventilatie, 3=bewatering): ")

    try:
        with open(outputFile, "r") as f:
            regels = f.readlines()
    except FileNotFoundError:
        print(f"Bestand '{outputFile}' niet gevonden")
        return -1

    if not systeem.isdigit():
        print("Ongeldig systeem gekozen.")
        return -3
    systeem = int(systeem)
    gevonden = False

    for i in range(len(regels)):
        onderdelen = regels[i].strip().split(";")
        if onderdelen[0] == datum:
            gevonden = True

            if systeem == 1:
                waarde = input("Nieuwe waarde CV (0-100): ")
                if waarde.isdigit() and 0 <= int (waarde) <= 100:
                    onderdelen[1] = waarde
                else:
                    print("Ongeldige waarde.")
                    return -3

            elif systeem == 2:
                waarde = input("Nieuwe waarde ventilatie (0-4): ")
                if waarde.isdigit() and 0 <= int(waarde) <= 4:
                    onderdelen[2] = waarde
                else:
                    print("Ongeldige waarde")
                    return -3
            elif systeem == 3:
                waarde = input("Nieuwe waarde bewatering (0=uit, 1=aan): ")
                if waarde == "0":
                    onderdelen[3] = "False"
                elif waarde == "1":
                    onderdelen[3] = "True"
                else:
                    print("Ongeldige waarde.")
                    return -3
            else:
                print("Ongeldig systeem.")
                return -3
            regels[i] = ";".join(onderdelen) + "\n"
            break
    if not gevonden:
        print("Datum niet gevonden.")
        return -1

    try:
        with open(outputFile, "w") as bestand:
            bestand.writelines(regels)
            print("Waarde succesvol overschreven.")
    except Exception as e:
        print(f"Fout bij opslaan: {e}")
        return -3


def smart_app_controller():
    inputFile = "input.txt"
    outputFile = "output.txt"

    while True:
        print("\n=== SMART APP CONTROLLER ===")
        print("1. Toon aantal dagen")
        print("2. Autobereken actuatoren")
        print("3. Overschrijf actuatorwaarde")
        print("4. Stoppen")

        keuze = input("Maak een keuze (1-4): ")

        if keuze == "1":
            print(f"Aantal dagen: {aantal_dagen(inputFile)}")

        elif keuze == "2":
            auto_bereken(inputFile, outputFile)

        elif keuze == "3":
            overwrite_settings(outputFile)

        elif keuze == "4":
            print('Programma afgesloten')
            break

        else:
            print("Ongeldige keuze, probeer opnieuw.")

# Start het programma
if __name__ == "__main__":
    smart_app_controller()