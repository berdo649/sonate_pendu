import random

with open("dictionnaire.txt", "r", encoding="utf-8") as fichier:
    lignes = fichier.readlines()

mots = []
for ligne in lignes:
    ligne = ligne.strip()
    mot = ligne.split(";")[0]
    mots.append(mot)

print(f"Nombre de mots chargés : {len(mots)}")

mot_tire = random.choice(mots)
print(f"Mot tiré au hasard : {mot_tire}")

lettres_trouvees = ["r", "a"]

mot_indice = ""
for lettre in mot_tire:
    if lettre in lettres_trouvees:
        mot_indice = mot_indice + lettre + " "
    else:
        mot_indice = mot_indice + "_ "

print(f"Mot indice : {mot_indice}")

vies = 5
lettre_proposee = "e"

print(f"\nLe joueur a {vies} vies")
print(f"Il propose la lettre : {lettre_proposee}")

if lettre_proposee in mot_tire:
    print("✅ Bonne pioche !")
else:
    vies = vies - 1
    print(f" Raté ! Il reste {vies} vies.")