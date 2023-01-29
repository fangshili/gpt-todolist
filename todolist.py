import streamlit as st
import shelve

# Open the shelf file
todo_db = shelve.open('todo_list')

# Create lists to store to-do and done items
if 'todo' not in todo_db:
    todo_db['todo'] = []
if 'done' not in todo_db:
    todo_db['done'] = []

todo_items = todo_db['todo']
done_items = todo_db['done']

# Create a function to add new items
def add_item(item):
    todo_items.append(item)
    todo_db['todo'] = todo_items

# Create a function to mark items as done
def mark_done(item):
    todo_items.remove(item)
    done_items.append(item)
    todo_db['todo'] = todo_items
    todo_db['done'] = done_items

# Create a function to mark items as not done
def mark_not_done(item):
    done_items.remove(item)
    todo_items.append(item)
    todo_db['todo'] = todo_items
    todo_db['done'] = done_items

# Create a function to remove items
def remove_item(item):
    todo_items.remove(item)
    todo_db['todo'] = todo_items

# Main program
st.set_page_config(page_title="To-Do List", page_icon=":clipboard:", layout="wide")

# Add a new item
new_item = st.text_input("Enter a new item:")
if new_item:
    add_item(new_item)

# Display the to-do list
st.header("To-Do List")
for item in todo_items:
    is_done = st.checkbox(item)
    if is_done:
        mark_done(item)

# Display the done list
st.header("Done List")
for item in done_items:
    is_not_done = st.checkbox(item)
    if is_not_done:
        mark_not_done(item)

# Close the shelf file
todo_db.close()
