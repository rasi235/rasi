import numpy as np
import streamlit as st
import pickle



# loading the saved model
loaded_model=pickle.load(open('trained_model.model','rb')) 


def  heart_prediction(input_data):
    input_data = (41,1,0,110,172,0,0,158,0,0,2,0,3)

    input_data_as_numpy_array =np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
                                                       
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
       return("The  Person Does not have a Heart Disease")
    else:
       return("The person has  Heart Disease")

# heart_prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
# st.display(input_data)


def model():


    st.title("Heart Prediction Web App")
    #  age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
    age=st.text_input("Age of the person")
    sex=st.text_input("Male or Female(M=1,F=0")
    cp=st.text_input("CP(Chest Pain)")
    trestbps=st.text_input("TRESTPS(Resting Blood Pressure)")
    chol=st.text_input("CHOL(Serum Cholesterol)")
    fbs=st.text_input("FBS(Fasting Blood Sugar)")
    restecg=st.text_input("RESTECG(Resting Electrocardiographic Measurement)")
    thalach=st.text_input("THALACH(The Person's Maximum Heart Rate Achieved)")
    exang=st.text_input("EXANG(Exercise Induced Angina)")
    oldpeak=st.text_input("OLDPEAK(ST Depression Induced By Exercise Relative To Rest)")
    slope=st.text_input("SLOPE(The ST Segment Shift Relative To Exercise-Induced Increments In Heart Rate)")
    ca= st.text_input("CA(The Number of Major Vessels)")
    thal=st.text_input("THAL(The persons maximum heart rate achieved)")


    heartdisease=''

    if st.button('Heart Test Resullt'):
        ccg = heart_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    st.success(heartdisease)

if __name__ == '__main__':
    model()
