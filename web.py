import streamlit as st
import functions as f

todos = f.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    f.write_todos(todos)

st.title('My Todo App')
st.subheader("This is my todo app")
st.write('This app is to increase your productivity')

for i, t in enumerate(todos):
    checkbox = st.checkbox(t, key=t)
    if checkbox:
        todos.pop(i)
        f.write_todos(todos)
        del st.session_state[t]
        st.rerun()

st.text_input(label="My todo", placeholder="Add a new todo",
              on_change=add_todo, key='new_todo')

#st.session_state