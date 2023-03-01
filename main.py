import streamlit as st
import functions

st.set_page_config(layout="wide")


def add_todo():
    add_todo_item = st.session_state["new_todo"] + "\n"
    todos.append(add_todo_item)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your <b>productivity</b>.", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="ok", placeholder="Add new todo...", on_change=add_todo, key='new_todo', label_visibility="hidden")


st.session_state