def fahrenheit(temp_celcius):
    return temp_celcius * 32 + 18

def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - (luchtvochtigheid / 100 ) * windsnelheid

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel_temp = gevoelstemperatuur (temp_celcius, windsnelheid, luchtvochtigheid)

    if gevoel_temp < 0 and windsnelheid > 10:
        return"het is heel koud en het stormt! verwarming helemaal aan!"
    elif gevoel_temp < 0 and windsnelheid <= 10:
        return "het is behoorlijk koud! veraming aan op de benedenverdieping!"
    elif 0 <= gevoel_temp < 10 and windsnelheid > 12:
        return "het is best kou en het waait; verwarming aan en roosters dicht!"
    elif 0 <= gevoel_temp < 10 and windsnelheid <= 12:
        return "het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gevoel_temp < 22:
        return "heerlijk weer, niet te koud of te warm."
    else:
        return "warm! airco aan!"

def weerstation():
    print("Welkom bij het Weerstation")
    print("Voer per dag de temperatuur, windsnelheid en luchtvochtigheid in.")
    print("Druk op Enter zonder waarde om te stoppen.")

    temperaturen = []
    for dag in range(1, 8): # maximaal 7 dagen
        #invoer temperatuur
        try:
            temp_input = input(f"Wat is op de dag {dag} de temperatuur[c]: ")
            if temp_input == "":
                print("programma gestopt door gebruiker.")
                break
            temp_c=float(temp_input)

        #invoer windsnelheid
            wind_input = input(f"Wat is op dag {dag} de windsnelheid [m/s]: ")
            if wind_input == "":
                print("programma gestopt door gebruiker.")
                break
            windsnelheid = float(wind_input)

        #invoer vochtigheid
            vocht_input = input(f"Wat is op dag {dag} de vochtigheid[%]: ")
            if vocht_input == "":
                print("programma gestopt door gebruiker.")
                break
            luchtvochtigheid = int(vocht_input)

            if not 0 <= luchtvochtigheid <= 100:
                print("Vochtigheid moet tusssen 0 en 100 liggen.")
            continue
        except ValueError:
            print("Ongeldige invoer! Gebruik alleen getallen.")
        except Exception as e:
            print(f"Er is een onverwachte fout opgestreden: {e}")
            continue

        # --- verwerking ---
        temp_f = fahrenheit(temp_c)
        rapport = weerrapport(temp_c, windsnelheid, luchtvochtigheid)
        temperaturen.append(temp_c)
        gemiddelde = sum(temperaturen) / len(temperaturen)

        # --- uitvoer ---
        print(f"Het is {temp_c:.1f}C ({temp_f:.1f}F)")
        print(rapport)
        print(f"Gemiddelde temperatuur tot nu toe is{gemiddelde:.1f}")

    print ("Einde van het programma")

if __name__ == "__main__":
    try:
        weerstation()
    except Exception as e:
        print(f"Kritieke fout: {e}")