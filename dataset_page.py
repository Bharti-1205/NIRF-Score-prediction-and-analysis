import pandas as pd
import streamlit as st

# displays the dataset used in regressor on dataset page 
def show_dataset_page():
    
    st.title("NIRF RANKING DATASET -")
    st.markdown("##")
    dataset = pd.read_csv("EngineeringRanking.csv")
    
    st.dataframe(dataset,800,500)
    