from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("accueil.html")


@app.route("/jeu", methods=["POST"])
def jeu():
    nom = request.form["nom"]
    return f"<h1>Bonjour {nom} ! La partie va bientôt commencer...</h1>"