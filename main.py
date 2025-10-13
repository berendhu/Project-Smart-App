from weerstation import weerstation
from smart_app_controller import smart_app_controller
from nauwkeurige_weersvoorspelling import huidig_weer

def main_menu():
    while True:
        print("\n=== SMART PLATFORM ===")
        print("1. Start Weerstation")
        print("2. Start Smart Home Controller")
        print("3. Toon acturele temperatuur in Utrecht")
        print("4. Stoppen")

        keuze = input("Maak een keuze (1-4): ")

        try:
            if keuze == "1":
                weerstation()
            elif keuze == "2":
                smart_app_controller()
            elif keuze == "3":
                print(huidig_weer(52.0908, 5.1222))
            elif keuze == "4":
                print("Tot ziens!")
                break
            else:
                print("Ongeldige keuze.")
        except Exception as e:
            print(f"Er is iets misgegaan: {e}")

if __name__ == "__main__":
    main_menu()