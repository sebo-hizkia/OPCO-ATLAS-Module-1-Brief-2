# OPCO-ATLAS-Module-1-Brief-2

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
