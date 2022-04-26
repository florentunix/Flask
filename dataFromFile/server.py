#!/usr/bin/python3
import flask
app = flask.Flask(__name__)

app.config["DEBUG"] = True

# Demander le repertoire racine avec la methode get
@app.route("/", methods=['GET'])
def index():
    return "<h1>Bienvenue sur notre serveur de donner</h1><p>Pour voir tout les données, cliquer <a href='./static/json/data.json'>ici</a></p>"


# La fonction ci-dessous permet de délivrer les fichiers statiques contenues
# a l'utilisateur
@app.route("/static/<path:path>")
def staticPath():
    return flask.send_from_directory('static', path)

if __name__ == '__main__':
    app.run()
