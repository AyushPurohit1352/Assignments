import json

USER_FILE = "users.json"
TODO_FILE = "todos.json"

def load_users():
    try:
        with open(USER_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_users(users):
    with open(USER_FILE, 'w') as file:
        json.dump(users, file)

def load_todos():
    try:
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file)

users = load_users()
todos = load_todos()

def register_user():
    print("=== Register ===")
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Please choose another.")
        return
    
    password = input("Enter a new password: ")
    users[username] = password
    save_users(users)
    print(f"User '{username}' registered successfully.")

def login_user():
    print("=== Login ===")
    username = input("Enter your username: ")
    if username not in users:
        print("Username does not exist.")
        return None
    
    password = input("Enter your password: ")
    if users[username] == password:
        print(f"Welcome, {username}!")
        return username
    else:
        print("Incorrect password.")
        return None

def add_todo(username):
    print("\n=== Add a TODO ===")
    todo = input("Enter the task: ")
    due_date = input("Enter the due date (e.g., 2024-09-10): ")
    if username not in todos:
        todos[username] = []
    todos[username].append({"task": todo, "due_date": due_date})
    save_todos(todos)
    print("TODO added successfully.")

def remove_todo(username):
    print("\n=== Remove a TODO ===")
    view_todos(username)
    try:
        index = int(input("Enter the index of the TODO to remove: ")) - 1
        if 0 <= index < len(todos.get(username, [])):
            todos[username].pop(index)
            save_todos(todos)
            print("TODO removed successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")

def update_todo_date(username):
    print("\n=== Update a TODO Due Date ===")
    view_todos(username)
    try:
        index = int(input("Enter the index of the TODO to update: ")) - 1
        if 0 <= index < len(todos.get(username, [])):
            new_date = input("Enter the new due date (e.g., 2024-09-10): ")
            todos[username][index]["due_date"] = new_date
            save_todos(todos)
            print("TODO due date updated successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")

def view_todos(username):
    print("\n=== Your TODO List ===")
    user_todos = todos.get(username, [])
    if not user_todos:
        print("No TODOs found.")
    else:
        for i, todo in enumerate(user_todos, start=1):
            print(f"{i}. Task: {todo['task']}, Due Date: {todo['due_date']}")

def todo_menu(username):
    while True:
        print("\n=== TODO Menu ===")
        print("1. View TODOs")
        print("2. Add TODO")
        print("3. Remove TODO")
        print("4. Update TODO Due Date")
        print("5. Logout")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            view_todos(username)
        elif choice == '2':
            add_todo(username)
        elif choice == '3':
            remove_todo(username)
        elif choice == '4':
            update_todo_date(username)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            register_user()
        elif choice == '2':
            user = login_user()
            if user:
                todo_menu(user)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
