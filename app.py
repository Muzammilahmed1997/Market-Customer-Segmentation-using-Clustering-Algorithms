import streamlit as st
import pandas as pd
import pickle


pickle_in = open("E:/rf.pkl", "rb") 
classifier = pickle.load(pickle_in)

def predict_note_authentication(PURCHASES, ONEOFF_PURCHASES,INSTALLMENTS_PURCHASES, PURCHASES_FREQUENCY, ONEOFF_PURCHASES_FREQUENCY, PURCHASES_INSTALLMENTS_FREQUENCY, PURCHASES_TRX):
    prediction = classifier.predict([[PURCHASES, ONEOFF_PURCHASES,INSTALLMENTS_PURCHASES, PURCHASES_FREQUENCY, ONEOFF_PURCHASES_FREQUENCY, PURCHASES_INSTALLMENTS_FREQUENCY, PURCHASES_TRX]])
    print(prediction)
    return prediction


def main():

    st.title("Customer Category Predictor")

    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">Predict The Category of Customer </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    PURCHASES  =  st.number_input("Enter value Purchases", key="1")

    ONEOFF_PURCHASES = st.number_input("Enter Value for One Off_Purchases", key="2")

    INSTALLMENTS_PURCHASES = st.number_input("Enter Installments Purchases", key="3")

    PURCHASES_FREQUENCY = st.number_input("Enter Purchases Frequency", key="4")

    ONEOFF_PURCHASES_FREQUENCY = st.number_input("Enter One Off Purchases Frequency", key="5")

    PURCHASES_INSTALLMENTS_FREQUENCY = st.number_input("Enter Purchases Installments Frequency", key="6")

    PURCHASES_TRX = st.number_input("Enter Purchases Frequency", key="6")

    result= ""

    if st.button("Predict"):
        result = predict_note_authentication(PURCHASES, ONEOFF_PURCHASES,INSTALLMENTS_PURCHASES, PURCHASES_FREQUENCY, ONEOFF_PURCHASES_FREQUENCY, PURCHASES_INSTALLMENTS_FREQUENCY, PURCHASES_TRX)
    
    
    if result == 0:
        st.success('Customer Belongs to Cluster Group 1')
    elif result == 1:
        st.success("Customer Belongs to Cluster Group 2")
    elif result == 2:
        st.success("Customer Belongs to Cluster Group 3")
    

if __name__=='__main__':
    main()