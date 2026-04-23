import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "une_cle_secrete_pour_le_pendu"


def charger_mots():
    """Lit le dictionnaire et renvoie la liste des mots."""
    with open("dictionnaire.txt", "r", encoding="utf-8") as fichier:
        lignes = fichier.readlines()
    mots = []
    for ligne in lignes:
        mot = ligne.strip().split(";")[0]
        mots.append(mot)
    return mots


def construire_mot_indice(mot, lettres_trouvees):
    """Construit l'affichage du mot avec tirets et lettres trouvees."""
    mot_indice = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_indice = mot_indice + lettre + " "
        else:
            mot_indice = mot_indice + "_ "
    return mot_indice


@app.route("/")
def home():
    return render_template("accueil.html")


@app.route("/jeu", methods=["POST"])
def jeu():
    # Le joueur vient de l'accueil, on démarre une nouvelle partie
    nom = request.form["nom"]
    mots = charger_mots()
    mot_tire = random.choice(mots)

    # On enregistre l'état de la partie dans la session
    session["nom"] = nom
    session["mot"] = mot_tire
    session["lettres_trouvees"] = []
    session["vies"] = 5

    mot_indice = construire_mot_indice(mot_tire, [])

    return render_template(
        "jeu.html",
        nom=nom,
        mot_indice=mot_indice,
        vies=5,
        mot_secret=mot_tire
    )


@app.route("/tentative", methods=["POST"])
def tentative():
    lettre = request.form["lettre"]

    mot = session["mot"]
    lettres_trouvees = session["lettres_trouvees"]
    vies = session["vies"]

    if lettre in mot:
        lettres_trouvees.append(lettre)
    else:
        vies = vies - 1

    session["lettres_trouvees"] = lettres_trouvees
    session["vies"] = vies

    mot_indice = construire_mot_indice(mot, lettres_trouvees)

    if "_" not in mot_indice:
        return render_template("fin.html", nom=session["nom"], mot=mot, gagne=True)

    if vies <= 0:
        return render_template("fin.html", nom=session["nom"], mot=mot, gagne=False)

    return render_template(
        "jeu.html",
        nom=session["nom"],
        mot_indice=mot_indice,
        vies=vies,
        mot_secret=mot
    )