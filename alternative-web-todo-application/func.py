FILENAME = 'todos.txt'


def get_todos():
    with open(FILENAME, 'r') as file_local:
        todos = [i.strip('\n') for i in file_local.readline()]
    return todos


def write_todos(todos_local):
    with open(FILENAME, 'w') as file_local:
        file_local.writelines(todos_local)