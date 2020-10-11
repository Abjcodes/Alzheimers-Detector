
import numpy as np
import pickle
import pandas as pd
import streamlit as st 

pickle_in = open("Prediction.pickle","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(gender,age,yoed,ses,mmse,etiv,nwbv,asf):
   
    prediction=classifier.predict([[gender,age,yoed,ses,mmse,etiv,nwbv,asf]])
    print(prediction)
    return prediction



def main():
    st.title("Alzheimer's Detector")
    html_temp = """
    <div style="background-color:#ffaf7a;padding:10px">
    <h2 style="color:white;text-align:center;">Alzheimer's Detection App</h2>
    </div>
    """
    if st.button("About"):
        st.text("This is a simple portal")
        st.text("to predict early symptoms of")
        st.text("Alzheimer's Disease (AD)")


    st.markdown(html_temp,unsafe_allow_html=True)
    gender = st.text_input("Gender (Input 1 for Male and 0 for Female)","")
    age = st.text_input("Age","")
    yoed = st.text_input("Years of Education","")
    ses = st.slider("Socioeconomic Status (SES) (On a scale 1 to 5)",1,5)
    st.write("You've selected",ses)
    mmse = st.text_input("Mini Mental State Examination (MMSE)","")
    etiv = st.text_input("Estimated Total Intracranial Volume (eTIV)","")
    nwbv = st.text_input("Normalize Whole Brain Volume (nWBV)","")
    asf = st.text_input("Atlas Scaling Factor (ASF)","")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(gender,age,yoed,ses,mmse,etiv,nwbv,asf)
    st.success('Alzheimers Status : {}'.format(result))
    st.text('')
    st.text('Index')
    st.text('')
    st.text('Demented: Showcases positive symptoms of Alzheimers')
    st.text('Non-Demented: Showcases no symptoms of Alzheimers')
    st.text('Coverted: Further tests are required for confirmation')


    
if __name__=='__main__':
    main()
    