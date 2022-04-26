# Flask
`FLask` est un framework python qui facilite la création d'application web en python ainsi que des API.

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
virtualenv env
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
```
