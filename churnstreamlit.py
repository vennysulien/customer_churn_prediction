import streamlit as st
from PIL import Image
import requests

header_image = Image.open('/home/vennysln/assets/customer churn pic 2.png')
st.image(header_image)
st.title("Customer Churn Prediction")
st.subheader('Just enter variables below then click Predict button:')

# create form
with st.form(key='churn_prediction_form'):
    gender = st.number_input(
        label = "1. Input customer's gender: ",
        help = "Example value: 0"
    )

    SeniorCitizen = st.number_input(
        label = "2. Input customer's SeniorCitizen: ",
        help = "Example value: 0"
    )

    Partner = st.number_input(
        label = "3. Input customer's Partner: ",
        help = "Example value: 0"
    )
    
    Dependents = st.number_input(
        label = "4. Input customer's Dependents: ",
        help = "Example value: 0"
    )

    PhoneService = st.number_input(
        label = "5. Input customer's PhoneService: ",
        help = "Example value: 0"
    )

    MultipleLines = st.number_input(
        label = "6. Input customer's MultipleLines: ",
        help = "Example value: 0"
    )

    InternetService = st.number_input(
        label = "7. Input customer's InternetService: ",
        help = "Example value: 0"
    )

    OnlineSecurity = st.number_input(
        label = "8. Input customer's OnlineSecurity: ",
        help = "Example value: 0"
    )

    OnlineBackup = st.number_input(
        label = "9. Input customer's OnlineBackup: ",
        help = "Example value: 0"
    )

    DeviceProtection = st.number_input(
        label = "10. Input customer's DeviceProtection: ",
        help = "Example value: 0"
    )

    TechSupport = st.number_input(
        label = "11. Input customer's TechSupport: ",
        help = "Example value: 0"
    )

    StreamingTV = st.number_input(
        label = "12. Input customer's StreamingTV: ",
        help = "Example value: 0"
    )

    StreamingMovies = st.number_input(
        label = "13. Input customer's StreamingMovies: ",
        help = "Example value: 0"
    )

    Contract = st.number_input(
        label = "14. Input customer's Contract: ",
        help = "Example value: 0"
    )

    PaperlessBilling = st.number_input(
        label = "15. Input customer's PaperlessBilling: ",
        help = "Example value: 0"
    )

    PaymentMethod = st.number_input(
        label = "16. Input customer's PaymentMethod: ",
        help = "Example value: 0"
    )

    tenure = st.number_input(
        label = "17. Input customer's tenure: ",
        help = "Example value: 0"
    )
    
    MonthlyCharges = st.number_input(
        label = "18. Input customer's MonthlyCharges: ",
        help = "Example value: 0"
    )

    TotalCharges = st.number_input(
        label = "19. Input customer's TotalCharges: ",
        help = "Example value: 0"
    )

    # button submit
    submitted = st.form_submit_button("Predict")

    if submitted:
        # collect data from form
        form_data = {
            "gender": gender,
            "SeniorCitizen": SeniorCitizen,
            "Partner": Partner,
            "Dependents": Dependents,
            "PhoneService": PhoneService,
            "MultipleLines": MultipleLines,
            "InternetService": InternetService,
            "OnlineSecurity": OnlineSecurity,
            "OnlineBackup": OnlineBackup,
            "DeviceProtection": DeviceProtection,
            "TechSupport": TechSupport,
            "StreamingTV": StreamingTV,
            "StreamingMovies": StreamingMovies,
            "Contract": Contract,
            "PaperlessBilling": PaperlessBilling,
            "PaymentMethod": PaymentMethod,
            "tenure": tenure,
            "MonthlyCharges": MonthlyCharges,
            "TotalCharges": TotalCharges
        }
        
        # sending the data to api service
        with st.spinner("Sending data to Prediction Server... Please Wait..."):
            res = requests.post(f"http://127.0.0.1:8000/predict", json= form_data).json()

        # parse the prediction result
        if res['status'] == 200:
            st.success(f"Customer Classification Prediction is: {res['prediction']}")
        else:
            st.error(f"Error predicting the data... Please Check Your Code {res}")
