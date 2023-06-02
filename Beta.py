while True:
    choice = input("Enter your choice (Insert, Edit, Delete, Show, Exit): ")
    match choice.capitalize():
        case "Show":
            i = 1
            file = open('todos.txt', 'r')
            todos = file.readlines()
            for todo in todos:
                print(f"{i}> {todo}")
                i += 1

        case "Insert":
            todo = input("Enter a todo: ")
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo.capitalize() + '\n')
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case "Delete":
            number = int(input("Enter number of the todo you want to delete: "))
            todos.pop(number - 1)
        case "Edit":
            number = int(input("Enter number of the todo you want to edit: "))
            todo = input("Enter the new todo: ")
            todos[number - 1] = todo.capitalize()
        case "Exit":
            break
        case _:
            print("You seem to have entered an invalid command, Try again.")
