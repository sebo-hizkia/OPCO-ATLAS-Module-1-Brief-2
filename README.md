# OPCO-ATLAS-Module-1-Brief-2 : API de prédiction de montant de prêt

## Description

Cette application expose un modèle d'IA via une API **FastAPI**.
Elle inclut :

- les endpoints `/predict` et `/health`,
- un système de **journalisation avec Loguru**,
- des **tests fonctionnels** avec Pytest,
- un **Dockerfile** pour le déploiement.

---

## Architecture de l’API

- `predict_api.py` : application FastAPI
- `logs/` : fichiers de logs générés par Loguru
- `tests/test_api.py` : tests fonctionnels Pytest
- `Dockerfile` : conteneurisation de l’API
- `requirements.txt` : dépendances Python

---

## Routes disponibles

### `GET /health`

Vérifie la santé de l’API.

**Réponse :**

```json
{
  "status": "OK"
}
```

### `POST /predict`

Envoie des données au modèle et récupère une prédiction.

**Données en entrée**
```json
{
  "nom": "string",
  "prenom": "string",
  "age": 30,
  "taille": 175,
  "poids": 70,
  "sexe": "F",
  "sport_licence": "oui",
  "niveau_etude": "master",
  "region": "string",
  "smoker": "non",
  "nationalité_francaise": "oui",
  "revenu_estime_mois": 2500
}
```

**Réponse :**

```json
{
  "montant_pret": 19431.5546875
}
```


## Configuration de l'environnement virtuel python
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration du dépôt
### Initialisation du dépôt GIT local
```
git config --global user.name "Sebastien"
git config --global user.email"s.andres@hizkia.eu"
git init
git add README.md
git commit -m "Initialisation du dépôt"
```

### Lié le dépôt local à GitHub
```
git branch -M main
git remote add origin https://github.com/sebo-hizkia/OPCO-ATLAS-Module-1-Brief-2.git
git push -u origin main
```

## Développement
### API
Lancement de l'API : ```uvicorn predict_api:app --reload --port 9000```

Test de l'API via interface automatique : http://127.0.0.1:9000/docs

### Tests API
```
PYTHONPATH=. pytest
```

### Page web avec formulaire à remplir
Lancement de l'application : ```streamlit run predict_streamlit.py```

## Déploiement
### Docker
Installation sur Linux Debian/Ubuntu : ```sudo apt install docker.io docker-compose```

Ajouter votre user au groupe docker : ```sudo usermod -aG docker $USER``` et redémarrer votre session

Construction de l'image : ```docker build -t predict-api .```

Lancement de l'API dans Docker : ```docker run -p 9000:9000 predict-api```
