import pandas
import streamlit as st
import send_email

st.title('Contact Me')

with st.form(key='my_form'):
    email = st.text_input('Enter email address:')
    file_read = pandas.read_csv('best-company-website/pages/jobs.csv')
    jobs = [i[1][0] for i in file_read.iterrows()]
    selected_job = st.selectbox('Select your job', options=jobs)
    message = st.text_area()
    button = st.form_submit_button('Submit Here')
    if button:
        send_email.email_sender(message=message, job=selected_job, email=email)

