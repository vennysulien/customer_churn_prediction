from fastapi import FastAPI
from fastapi import Request
import pickle

app = FastAPI()

@app.get('/')
async def root ():
    response = {
        "status": 200,
    }
    return response


def load_model():
    try:
        pickle_file = open('models/production_model.pkl','rb')
        classifier = pickle.load(pickle_file)
        return classifier
    except Exception as e:
        response = {
            "status": 204,
            "message": str(e)
        }
        return response

@app.get('/check')
async def check():
    model = load_model()
    return model

@app.post('/predict')
async def predict (data: Request):

    # load request
    data = await data.json()
    
    gender = data["gender"]
    SeniorCitizen = data["SeniorCitizen"]
    Partner = data["Partner"]
    Dependents = data["Dependents"]
    PhoneService = data["PhoneService"]
    MultipleLines = data["MultipleLines"]
    InternetService = data["InternetService"]
    OnlineSecurity = data["OnlineSecurity"]
    OnlineBackup = data["OnlineBackup"]
    DeviceProtection = data["DeviceProtection"]
    TechSupport = data["TechSupport"]
    StreamingTV = data["StreamingTV"]
    StreamingMovies = data["StreamingMovies"]
    Contract = data["Contract"]
    PaperlessBilling = data["PaperlessBilling"]
    PaymentMethod = data["PaymentMethod"]
    tenure = data["tenure"]
    MonthlyCharges = data["MonthlyCharges"]
    TotalCharges = data["TotalCharges"]
    

    model = load_model()
    labels = ['Berhenti berlangganan', 'Berlangganan']
    try:
        prediction = model.predict([[gender, SeniorCitizen, Partner, Dependents, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, tenure, MonthlyCharges, TotalCharges]])
        result = labels[prediction[0]]
        response = {
            "status": 200,
            "prediction": result
        }
    except Exception as e:
        response = {
            "status": 204,
            "message": str(e)
        }
    return response
    