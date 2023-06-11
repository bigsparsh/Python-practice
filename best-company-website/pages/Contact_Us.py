import pandas
import streamlit as st

st.title('Contact Me')

with st.form(key='my_form'):
    email = st.text_input('Enter email address:')
    # jobs = pandas.read_csv('best-company-website')
    selected_job = st.selectbox()
