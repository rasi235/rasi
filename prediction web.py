import numpy as np
import streamlit as st
import pickle



# loading the saved model
loaded_model=pickle.load(open('C:/Users\pavani.pasupulati\OneDrive - Anblicks\Desktop\MACHINE LEARING/trained_model.model','rb')) 


def  heart_prediction(input_data):
    input_data = (41,1,0,110,172,0,0,158,0,0,2,0,3)

    input_data_as_numpy_array =np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
                                                       
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
       return(" the person  have a heart disease")
    else:
       return("the person doesnt  has heart disease")

# heart_prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
# st.display(input_data)


def model():


    st.title("heart prediction web app")
    #  age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
    age=st.text_input("age of the person")
    sex=st.text_input("male or female")
    cp=st.text_input("how many Constrictive pericarditis ")
    trestbps=st.text_input("how much blood sugar")
    chol=st.text_input("cholesterol")
    fbs=st.text_input("Fasting glucose levels")
    restecg=st.text_input(" Resting electrocardiographic measurement ")
    thalach=st.text_input("The person's maximum heart rate achieved")
    exang=st.text_input("exercise induced angina")
    oldpeak=st.text_input("ST depression induced by exercise relative to res")
    slope=st.text_input("The ST segment shift relative to exercise-induced increments in heart rate")
    ca= st.text_input("The number of major vessels ")
    thal=st.text_input("The persons maximum heart rate achieved")


    ccg =''

    if st.button('heart test resullt'):
        ccg = heart_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    st.success(ccg)

if __name__ == '__main__':
    model()