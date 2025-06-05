def zeige_themen():
    themen = [
        "1. Künstliche Intelligenz",
        "2. Maschinelles Lernen",
        "3. Webentwicklung",
        "4. Datenanalyse",
        "5. Spielentwicklung"
    ]

    print("Bitte wähle ein Thema:")
    for thema in themen:
        print(thema)

    wahl = input("Gib die Nummer deines Themas ein: ")

    try:
        wahl_int = int(wahl)
        if 1 <= wahl_int <= len(themen):
            print(f"Du hast '{themen[wahl_int - 1]}' gewählt.")
        else:
            print("Ungültige Auswahl. Bitte gib eine Zahl zwischen 1 und 5 ein.")
    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")


if __name__ == "__main__":
    zeige_themen()
