to_do_list = []

def add_items():
    add = input("Enter items to add on your list: ")
    to_do_list.append(add)

def view_list():
    for i, task in enumerate(to_do_list):
        print(f"{i}.{task}")

def delete_list():
    del_index = int(input("Enter the index of the item to delete: "))
    if del_index  <= 0 < len(to_do_list):
        del to_do_list[del_index]
        print("Item deleted successfully.")
    else:
        print("Invalid index.")

while True:
    user_input = input("Enter a command ('view', 'delete' ,'add') or 'exit' to quit: ")
    if user_input == "add":
        add_items()
    elif user_input == "view":
        view_list()
    elif user_input == "delete":
        delete_list()
    elif user_input == "exit":
        break
    else:
        print("Invalid command.")
        