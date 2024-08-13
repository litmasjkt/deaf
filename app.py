import numpy as np
import pickle
import streamlit as st


# loadmodel
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Anda tidak menderita diabetes'
    else:
      return 'Anda menderita diabetes'
  
  
def main():
    
    
    # Judul
    st.title('Prediksi Diabetes Bebasis Web')
    
    
    # membagi colom
    col1, col2 = st.columns(2)
    with col1:
      Pregnancies = st.number_input('Nilai Pregnancies', min_value=0, step=1, format="%d")
    with col2:
      Glucose = st.number_input('Nilai Glucose', min_value=0, step=1, format="%d")
    with col1:
      BloodPressure = st.number_input('Nilai Tekanan Darah', min_value=0, step=1, format="%d")
    with col2:
      SkinThickness = st.number_input('Nilai Skin Thickness', min_value=0, step=1, format="%d")
    with col1:
      Insulin = st.number_input('Nilai Insulin', min_value=0, step=1, format="%d")
    with col2:
      BMI = st.number_input('Nilai BMI', min_value=0.0, step=0.1, format="%.1f")
    with col1:
      DiabetesPedigreeFunction = st.number_input('Nilai Diabetes Pedigree Function', min_value=0.0, step=0.01, format="%.2f")
    with col2:
      Age = st.number_input('Nilai Usia', min_value=0, step=1, format="%d")
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
if __name__ == '__main__':
    main()
    
 
    # Add footer
st.write("---")
st.write("Aplikasi Prediksi Diabetes ini dibuat untuk membantu memprediksi kemungkinan diabetes berdasarkan data kesehatan yang dimasukkan.")