# projetWine

Auteurs : Carmes Aurélien (ICC), Richeme Florian (IA)


## Installation de l'application

### Environnement virtuel

A la racine du projet, faire :
`python3 -m venv .venv`
`source .venv/bin/activate`
`pip install -r app/requirements.txt`

### Lancer l'application

Le serveur peut être lancé avec `uvicorn app.main:app`.

L'API est accessible à l'addresse 127.0.0.1:8000


### But
Créer une application FastAPI permettant d’interagir avec ce modèle prédictif
    • POST /api/predict permet de réaliser une prédiction en donnant en body les données nécessaires du vin à celle-ci. La prédiction est donnée via une note sur 10 du vin entré.
    • GET /api/predict permet de générer une combinaison de données permettant d’identifier le “vin parfait” (probablement inexistant mais statistiquement possible). La prédiction devra fournir les caractéristiques du “vin parfait”

    • GET /api/model permet d’obtenir le modèle sérialisé
    • GET /api/model/description permet d’obtenir des informations sur le modèle
       - Paramètres du modèle
       - Métriques de performance du modèle sur jeu de test (dernier entraînement)
       - Autres (Dépend de l’algo utilisé)
    • PUT /api/model permet d’enrichir le modèle d’une entrée de donnée supplémentaire (un vin en plus. Une donnée supplémentaire doit avoir le même format que le reste des données.
    • POST /api/model/retrain permet de réentrainer le modèle. Il doit prendre en compte les données rajoutées a posteriori