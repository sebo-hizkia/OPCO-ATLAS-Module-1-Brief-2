import streamlit as st
import requests

# URL de l'API FastAPI de prediction
API_URL = "http://localhost:9000/predict/"

st.set_page_config(page_title="Prédiction montant de prêt", page_icon="💰", layout="centered")

st.title("💰 Prédiction du montant de prêt")
st.markdown("Remplis les informations ci-dessous pour obtenir une estimation du montant de prêt.")

# --- FORMULAIRE ---

with st.form("client_form"):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    age = st.number_input("Âge", 18, 99, 30)
    taille = st.number_input("Taille (cm)", 150.0, 200.0, 175.0)
    poids = st.number_input("Poids (kg)", 30.0, 150.0, 70.0)

    sexe = st.selectbox("Sexe", ["H", "F"])
    sport_licence = st.selectbox("Licence sportive ?", ["oui", "non"])
    niveau_etude = st.selectbox("Niveau d'étude", ["aucun","bac", "bac+2", "master", "doctorat"])
    region = st.text_input("Région")

    smoker = st.selectbox("Fumeur ?", ["oui", "non"])
    nationalite = st.selectbox("Nationalité française ?", ["oui", "non"])

    revenu = st.number_input("Revenu mensuel estimé (€)", 0.0, 10000.0, 2500.0)

    submit = st.form_submit_button("Prédire le montant")


# --- TRAITEMENT ---

if submit:
    input_data = {
        "nom": nom,
        "prenom": prenom,
        "age": age,
        "taille": taille,
        "poids": poids,
        "sexe": sexe,
        "sport_licence": sport_licence,
        "niveau_etude": niveau_etude,
        "region": region,
        "smoker": smoker,
        "nationalité_francaise": nationalite,
        "revenu_estime_mois": revenu
    }

    st.write("📡 Envoi des données à l'API...")

    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            montant = response.json()["montant_pret"]
            st.success(f"Montant estimé du prêt : **{montant:,.2f} €**")
        else:
            st.error(f"Erreur API : {response.text}")

    except Exception as e:
        st.error(f"❌ Impossible de contacter l'API : {e}")
