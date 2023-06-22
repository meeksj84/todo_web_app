def get_todos(filepath='data.txt'):
    """ Read a text file and return a list of to-do items """
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()  # reads the data from data.txt and creates a list from those items
    return todo_list_local


def write_todos(todo_list_arg, filepath='data.txt'):
    """ Write the to-do item list in the text file """
    with open(filepath, 'w') as file:  # writes items to the data.txt file.
        file.writelines(todo_list_arg)  # will create or overwrite to a file (see docs for more info)
