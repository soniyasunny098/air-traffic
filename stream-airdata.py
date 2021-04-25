#air traffic 
from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
model = load_model('air-traffic-data')






def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():
    from PIL import Image
    image = Image.open('GettyImages.jpg')
    image_office = Image.open('aeroplane.jpg')
    st.image(image,use_column_width=True)
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))
    st.sidebar.info('This app is created to predict terminal')
    st.sidebar.success('https://www.pycaret.org')
    st.sidebar.image(image_office)
    st.title("Predicting Airport Terminal")
    if add_selectbox == 'Online':
        Activity Period=st.number_input('Activity Period', min_value=0, max_value=201603, value=0)
        Passenger Count = st.number_input('Passenger Count',min_value=1, max_value=659837, value=1)
        Adjusted Passenger Count = st.number_input('Adjusted Passenger Count', min_value=1, max_value=659837, value=1)
        GEO Summary = st.selectbox('GEO Summary',['International','Domestic'])
        GEO Region = st.selectbox('GEO Region',[ 'US','Asia','Europe','Canada','Mexico','Other values'])
        Activity Type Code = st.selectbox('Activity Type Code', ['Deplaned', 'Enplaned','Thru/Transit'])
        Price Category Code = st.selectbox('Price Category Code', ['Low Fare', 'Other'])
        Boarding Area = st.selectbox('Boarding Area', ['A', 'B','C','F','G'])
        Adjusted Activity Type Code = st.selectbox('Adjusted Activity Type Code', ['Deplaned', 'Enplaned','Thru/Transit*2'])
        Year = st.selectbox('Year', [2005, 2016])
        Month = st.selectbox('Month',['January','July','August','September','October'])
        output=""
        input_dict={'Activity Period':Activity Period,'Passenger Count':Passenger Count,'Adjusted Passenger Count':Adjusted Passenger Count,'GEO Summary':GEO Summary,'GEO Region': GEO Region,'Activity Type Code':Activity Type Code,'Price Category Code' : Price Category Code,'Boarding Area':Boarding Area,'Adjusted Activity Type Code':Adjusted Activity Type Code,'Year':Year,'Month':Month}
        input_df = pd.DataFrame([input_dict])
        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = str(output)
            if output == '0':
              output="YOUR TERMINAL IS INTERNATIONAL"
            elif output == '2':
              output="YOUR TERMINAL IS TERMINAL 1"
            elif output == '3':
              output="YOUR TERMINAL IS TERMINAL 2"
            elif output == '4':
              output="YOUR TERMINAL IS TERMINAL 3"
            else:
              output="OTHER TERMINAL"
        st.success('The output is {}'.format(output))
    if add_selectbox == 'Batch':
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            data = pd.read_csv(file_upload)            
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)
def main():
    run()

if __name__ == "__main__":
  main()
