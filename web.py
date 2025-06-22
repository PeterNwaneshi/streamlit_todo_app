import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()

def add_todo():
    todo = st.session_state["New_Todo"] + '\n'
    todos.append(todo.capitalize())
    write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app will increase your productivity")

st.text_input(label='', placeholder='Add new todo ..', 
              on_change=add_todo, key='New_Todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()

