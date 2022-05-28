# imports
import os
import sys
import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt
import streamlit as st
import awesome_streamlit as ast
import time
from logging import log
import streamlit as st
import pandas as pd
from scripts.logger_config import logger
sys.path.append(os.path.abspath(os.path.join('./scripts')))
from file_handler import FileHandler
st.set_page_config(page_title="Rossman Pharmaceuticals")

st.title('Rossmann Pharmaceuticals Prediction Dashboard')
st.sidebar.write('Sidebar')

## INPUTS
store_id = st.sidebar.number_input('Store Id', min_value=0, step=1)
test_file = st.sidebar.file_uploader("Upload Files",type=['csv'])
predict_button = st.sidebar.button('Predict')

try:
  test_df = pd.read_csv(test_file)
  st.write(test_df.head())
except:
  logger.error('File Not Correct')
  print("In Correct File type")

if(predict_button):
  st.write(f"Store = {store_id} Prediction Begin ...")
  time.sleep(2000)
  st.write('Sorry, Dashboard not completed build on progress')
def write():
    """Used to write the page in the app.py file"""
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.header('Prediction on test data')
    file_handler = FileHandler()
    df =  pd.read_csv('features/test_features.csv')
    test_df =  pd.read_csv('src/data/test.csv')
    st.markdown('### Sample test data input')
    st.write(test_df.head(10))
    model = pickle.load(open('models/XGB Regressor_Sales 2021-08-01-16:01:09.pkl', "rb"))
    y_preds = model.predict(df)
    prediction_df = df.copy()
    prediction_df["Pred_sales"] = y_preds
    st.markdown('### Sample prediction output')
    st.write(prediction_df["Pred_sales"].head(10))
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(df)
    st.header('Feature Importance')
    plt.title('Feature importance based on SHAP values')
    shap.summary_plot(shap_values, df)
    st.pyplot(bbox_inches='tight')
    st.write('---')

    plt.title('Feature importance based on SHAP values (Bar)')
    shap.summary_plot(shap_values, df, plot_type="bar")
    st.pyplot(bbox_inches='tight')
