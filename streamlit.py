import streamlit as st
import pandas as pd
import numpy as np
import pickle

def main():
    st.title('Customer Churn Prediction App')
    age = st.number_input('Age', min_value=0, max_value=100)

    # Create a button to trigger predictions
    if st.button('Predict'):
        input_data = {
            'Age': age,
        }
        
        input_df = pd.DataFrame([input_data])
        
        # Make predictions
        predictions = predict_churn(input_df)
        st.write('Predictions:', predictions)

if __name__ == '__main__':
    main()