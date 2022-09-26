import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_housing_data, load_pkl_file
from src.machine_learning.evaluate_reg import regression_performance, regression_evaluation_plots


def page_ml_predict_price_body():

    # load price pipeline files
    version = 'v1'
    price_pipe = load_pkl_file(f"outputs/ml_pipeline/predict_price/{version}/regression_pipeline.pkl")
    data_cleaning_pipe = load_pkl_file(f"outputs/ml_pipeline/data_cleaning/dataCleaning_pipeline.pkl")
    price_feat_importance = plt.imread(f"outputs/ml_pipeline/predict_price/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_price/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_price/{version}/X_test.csv")
    y_train =  pd.read_csv(f"outputs/ml_pipeline/predict_price/{version}/y_train.csv")
    y_test =  pd.read_csv(f"outputs/ml_pipeline/predict_price/{version}/y_test.csv")

 

    st.write("### ML Pipeline: Predict House Price")    
    # display pipeline training summary conclusions
    st.info(
        f"* The pipeline was tuned aiming at least 0.75 accuracy for the sales price of a property with a given set of attributes.\n"

        f"* The pipeline performance on the train and test set is 0.99 and 0.79 respectively.\n"
       )
    st.write("---")

    # show pipeline steps
    st.write("* ML pipeline to clean the data ")
    st.write(data_cleaning_pipe)
    st.write("* ML pipeline to predict sales prices of houses ")
    st.write(price_pipe)
    st.write("---")

    # show best features
    st.write("* The features the model was trained and their importance")
    st.write(X_train.columns.to_list())
    st.image(price_feat_importance)
    st.write("---")


    st.write("### Pipeline Performance")
    regression_performance(X_train=X_train, y_train=y_train,
                        X_test=X_test, y_test=y_test,
                        pipeline=price_pipe) 

    st.write("### Regression Performance Plots")
    regression_evaluation_plots(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, pipeline=price_pipe)  