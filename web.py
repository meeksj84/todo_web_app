import streamlit as st  # https://docs.streamlit.io/library/get-started
import functions

todo_list = functions.get_todos()


def add_todo():
    todo_local = st.session_state['new_todo'] + '\n'
    todo_list.append(todo_local)
    functions.write_todos(todo_list)


st.title('My Todo App')
st.subheader('This is my web app')
st.write('This app is to increase your productivity')

for index, item in enumerate(todo_list):
    checkbox = st.checkbox(item, key=f"{index}-{item}")
    if checkbox:
        todo_list.pop(index)
        functions.write_todos(todo_list)
        del st.session_state['new_todo']
        st.experimental_rerun()

st.text_input(label='End of list', placeholder='Add a todo: ',
              on_change=add_todo, key='new_todo')

