import streamlit as st
import pandas as pd
import plotly.express as px

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
st.header("SITE EM DESENVOLVIMENTO")
