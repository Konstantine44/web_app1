import streamlit as st
import functons

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functons.write_todos(todos)


todos = functons.get_todos()

st.title("My Todo app")
st.subheader("this is my todo app")




for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functons.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter", placeholder="Add New Todo...",
              on_change=add_todo, key="new_todo")


