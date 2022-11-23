# projetWine

## Installation de l'application

### Environnement virtuel

A la racine du projet, faire :
`python3 -m venv .venv`
`source .venv/bin/activate`
`pip install -r app/requirements.txt`

### Lancer l'application

Le serveur peut être lancé avec `uvicorn app.main:app`.

L'API est accessible à l'addresse 127.0.0.1:8000