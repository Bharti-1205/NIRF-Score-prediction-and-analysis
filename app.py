import streamlit as st

# importing modules of webapp from differenr files
from predict_page import show_predict_page
from explore_page import show_explore_page
from dataset_page import show_dataset_page

#displays the sidebar with three options
page = st.sidebar.selectbox("EXPLORE OR PREDICT", ("Predict", "Explore","Dataset")) 

if page == "Predict":
    show_predict_page()
elif page == "Explore":
    show_explore_page()
else:
    show_dataset_page()
