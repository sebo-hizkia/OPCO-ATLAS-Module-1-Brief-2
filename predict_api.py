from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from loguru import logger
from modules.preprocess import preprocessing, split
from modules.print_draw import print_data, draw_loss
from models.models import create_nn_model, train_model, model_predict
import pandas as pd
import joblib
from os.path import join as join
import mlflow

# Configuration du logger
logger.add("logs/predict_api.log", rotation="100 MB", level="INFO")

# Création de l'application FastAPI
app = FastAPI(title="API d'exposition de modèle IA")

# Charger le préprocesseur
preprocessor_loaded = joblib.load(join('models','preprocessor.pkl'))

# charger le modèle
model = joblib.load(join('models','model_2024_08.pkl'))

# Modèle Pydantic pour la validation des données reçues
class ClientInput(BaseModel):
    nom: str
    prenom: str
    age: int
    taille: float
    poids: float
    sexe: str
    sport_licence: str
    niveau_etude: str
    region: str
    smoker: str
    nationalité_francaise: str
    revenu_estime_mois: float

# Point de terminaison pour recevoir vérifier l'état de santé de l'API
# Cela sert aux autres programme comme Docker ou Kubernates par exemple à vérifier que tout va bien
# Ils attendent un status 200 en réponse
@app.get("/health")
async def health():
    """
    Retourne l'état de santé de l'API
    """
    try:
        logger.info(f"healthcheck")

        return {"status": "OK"}


    except Exception as e:
        logger.error(f"Erreur healthcheck : {e}")
        raise HTTPException(status_code=500, detail="API non fonctionnelle")

# Point de terminaison pour recevoir le montant de prêt
@app.post("/predict/")
async def predict(input_data: ClientInput):
    """
    Exécution du modèle
    """
    try:
        logger.info(f"Requête reçue : {input_data}")

        # Convertir DataFrame pour preprocessing
        df = pd.DataFrame([input_data.model_dump()])

        X_processed = preprocessor_loaded.transform(df)

        y_pred = model_predict(model, X_processed)

        logger.info(f"Prédiction : {y_pred}")

        return {"montant_pret": float(y_pred[0])}

    except Exception as e:
        logger.error(f"Erreur d'analyse : {e}")
        raise HTTPException(status_code=500, detail=str(e))
