import functions
import streamlit as st
completed_todos = functions.get_complete_todos()
st.header("Completed Todos")
for todo in completed_todos:
    checkbox = st.text(todo)