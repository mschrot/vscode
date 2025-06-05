# Ein einfaches Python-Programm, das verschiedene Konzepte demonstriert

# 1. Variablen und Datentypen
name = "Anna"          # String
alter = 25             # Integer
groesse = 1.68         # Float
student = True         # Boolean

# 2. Ausgabe mit print()
print("Hallo, mein Name ist", name)
print(f"Ich bin {alter} Jahre alt und {groesse}m groß.")

# 3. Bedingte Anweisung
if alter >= 18:
    print("Ich bin volljährig.")
else:
    print("Ich bin minderjährig.")

# 4. Schleife (for-loop)
print("\nZählen bis 5:")
for i in range(1, 6):
    print(i)

# 5. Funktion definieren
def berechne_quadrat(zahl):
    return zahl ** 2

# Funktion aufrufen
ergebnis = berechne_quadrat(4)
print(f"\nDas Quadrat von 4 ist {ergebnis}")

# 6. Liste und Schleife
tiere = ["Hund", "Katze", "Vogel"]
print("\nMeine Lieblingstiere:")
for tier in tiere:
    print("- " + tier)

# 7. Dictionary
person = {
    "name": "Max",
    "beruf": "Programmierer",
    "hobbys": ["Lesen", "Schwimmen", "Programmieren"]
}

# 8. Zugriff auf Dictionary-Elemente
print(f"\n{person['name']} ist {person['beruf']} und seine Hobbys sind:")
for hobby in person["hobbys"]:
    print(f"- {hobby}")

# 9. Benutzereingabe
eingabe = input("\nWie heißt du? ")
print(f"Schön dich kennenzulernen, {eingabe}!")
