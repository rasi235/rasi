import numpy as np
import pickle

# loading the saved model
loaded_model=pickle.load(open('C:/Users\pavani.pasupulati\OneDrive - Anblicks\Desktop\MACHINE LEARING/trained_model.model','rb')) 


input_data = ( 41,1,0,110,172,0,0,158,0,0,2,0,3)


input_data_as_numpy_array =np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
                                                       
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]--0):
  print(" the person  have a heart disease")
else:
  print("the person doesnt  has heart disease")

# st.display(prediction)