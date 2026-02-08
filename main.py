todos = []

name = input("Enter your name: ")

while True:
    choice = input("Enter if you want to add,show,edit,complete or exit: ")
    choice = choice.strip()

    match choice:
        case "add":
            todo = input("Enter your todo list : ")+ "\n"

            files=open('todos.txt','r')
            todos=files.readlines()
            files.close()

            todos.append(todo)

            files=open('todos.txt','w')
            files.writelines(todos)
            files.close()

        case "show":
            files=open('todos.txt','r')
            todos=files.readlines()
            files.close()

            new_todos=[]

            for items in todos:
                new_item=items.strip()
                new_todos.append(new_item)

            for index,item in enumerate(new_todos):
                row=f"{index+1}-{item}"
                print(row)

        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "complete":
            counted=int(input("Enter the number of todo completed: "))
            todos.pop(counted-1)
        case "exit":
            break

print(f"Bye {name} ")
