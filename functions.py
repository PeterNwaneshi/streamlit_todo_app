
def get_todos(file_path="todos.txt"):
    """Gets todo list from the text file"""
    # todos = []
    with open(file_path, 'r') as file:
            todos = file.readlines()

    # for index, todo in enumerate(f_todos, start=1):
    #       todos.append(f"{index}. {todo.capitalize()}")
    return todos

def write_todos(todos, file_path ="todos.txt"):
    """Writes todo list to the text file"""
    with open(file_path, 'w') as file:
            file.writelines(todos)