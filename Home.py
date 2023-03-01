import streamlit as st
import functions


st.set_page_config(layout="wide")


def add_todo():
    add_todo_item = st.session_state["new_todo"] + "\n"
    todos.append(add_todo_item)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


todos = functions.get_todos()

st.title("Python Todo App")
st.subheader("This app can help you to increase your productivity")
st.text("Type what you need to DO in the box")
st.text_input(label="ok", placeholder="Add new todo...", on_change=add_todo, key='new_todo', label_visibility="hidden")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        #  todo_completed = todos[index]
        todos.pop(index)
        functions.write_todos(todos)
        functions.write_complete_todos(todo)
        del st.session_state[todo]
        st.experimental_rerun()

# st.session_state
