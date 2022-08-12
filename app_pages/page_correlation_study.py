import streamlit as st
from src.data_management import load_housing_data


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

from feature_engine.discretisation import ArbitraryDiscretiser
import numpy as np
import plotly.express as px

def page_correlation_study_body():

    df = load_housing_data()

    vars_to_study = ['1stFlrSF', 'GarageArea', 'GarageYrBlt', 'GrLivArea', 'KitchenQual', 'MasVnrArea', 'OverallQual', 'TotalBsmtSF', 'YearBuilt', 'YearRemodAdd']

    st.write("### Housing Prices Correlation Study")
    st.info(
        f"* The client is interested in identifying the features that have strong correlation with "
        f"house prices so that she can maximize the sales revenue."
    )

    # inspect data
    if st.checkbox("Inspect Customer Base"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")
        
        st.write(df.head(10))

    st.write("---")

    df_eda = df.filter(vars_to_study + ['SalePrice'])


    # Individual plots per variable
    if st.checkbox("House Prices per Variable"):
        house_price_per_variable(df_eda)


def house_price_per_variable(df_eda):
    vars_to_study = ['1stFlrSF', 'GarageArea', 'GarageYrBlt', 'GrLivArea', 'KitchenQual', 'MasVnrArea', 'OverallQual', 'TotalBsmtSF', 'YearBuilt', 'YearRemodAdd']
    time = ['GarageYrBlt', 'YearBuilt', 'YearRemodAdd']
    target_var = 'SalePrice'
    
    for col in vars_to_study:
        if len(df_eda[col].unique()) <= 10:
            plot_box(df_eda, col, target_var)
            print("\n\n")
        else:
            if col in time:
                plot_line(df_eda, col, target_var)
                print("\n\n")
            else:
                plot_scatter(df_eda, col, target_var)
                print("\n\n")



def plot_scatter(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.scatterplot(data=df, x=col, y=target_var)
    plt.title(f"{col}", fontsize=20)        
    st.pyplot(fig) # st.pyplot() renders image, in notebook is plt.show()

def plot_line(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.lineplot(data=df, x=col, y=target_var)
    plt.title(f"{col}", fontsize=20)        
    st.pyplot(fig) # st.pyplot() renders image, in notebook is plt.show()

def plot_box(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.boxplot(data=df, x=col, y=target_var) 
    plt.title(f"{col}", fontsize=20)
    st.pyplot(fig) # st.pyplot() renders image, in notebook is plt.show()