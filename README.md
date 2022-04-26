# Flask
`FLask` est un framework python qui facilite la création d'application web, et API en python.

## Dependances à installer

### python3
```bash
sudo apt install python3 -y
```
### virtualenv
```bash
sudo apt install python3-virtualenv -y
```

## Environnement virtuel
Une fois les paquets installer, il faut créer un environnement de développement on installera le paquet `Flask`

### Creation d'un environement python
```bash
python3 -m venv env
```

`env` est le nom de répertoire de notre environnement.

### Activation de l'environnement python

```bash
source .env/bin/activate
```

## Installation du paquet Flask

```bash
pip install flask
```

## HelloWorld.py

```python
#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
  return 'Hello, World :)'  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```
Copier les lignes ci-dessus et coller dans le fichier `HelloWorld.py`

## Demarrage du serveur

Il ne reste plus qu'a démarrer notre serveur WEB

```bash
python ./HelloWorld.py
```
## Deploiement du serveur en production
Notre serveur WEB est en mode développement, pour déployer notre serveur en production visiter la [documentation](https://flask.palletsprojects.com/en/2.1.x/deploying/) de Flask. 
