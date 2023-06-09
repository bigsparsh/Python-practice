import streamlit as st
import func
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        file.write('')

# Titles
st.title('Todo Application')
st.subheader('- Sparsh Singh')

todos = func.get_todos()

# Checkboxes and labels
st.write(todos)