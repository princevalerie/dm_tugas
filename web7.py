import streamlit as st
import pickle
import numpy

# Assuming 'decision_tree_model' is your Decision Tree model
with open('decisiontree_model3.pkl', 'wb') as file:
    pickle.dump("DecisionTree", file)

diabetes_model_dtr = pickle.load(open('decisiontree_model3.pkl', 'rb'))

st.title("Prediksi diabetes menggunakan 3 model machine learning")

age = st.number_input('Input Umur', value=64, step=1)

# Convert gender to 0 or 1
gender = st.selectbox('Input Gender', ['Male', 'Female'])
gender = 0 if gender == 'Female' else 1

impluse = st.number_input('Input impluse', value=66, step=1)
pressurehight = st.number_input('Input pressurehight', value=160, step=1)
pressurelow = st.number_input('Input pressurelow', value=83, step=1)
glucose = st.number_input('Input glucose', value=160.0, step=1.0)
kcm = st.number_input('Input kcm', value=1.80, step=0.01)
troponin = st.number_input('Input troponin', value=0.012, step=0.001)

diagnosis_dtr = ''

if st.button('Test Prediksi Diabetes'):
    input_data = [[age, gender, impluse, pressurehight, pressurelow, glucose, kcm, troponin]]
      # Convert input_data to a numpy array
    input_data_asarray = np.asarray(input_data)

    # Reshape the input_data_asarray
    input_reshaped = input_data_asarray.reshape(1, -1)

    # Use loaded_model for prediction
    prediction = loaded_model.predict(input_reshaped)
    
    if prediction[0] == 1:
        diagnosis_dtr = "Pasien terkena diabetes (dtr)"
    else:
        diagnosis_dtr = "Pasien tidak terkena diabetes (dtr)"

st.write(diagnosis_dtr)
