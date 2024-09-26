"""
Utilize Python lists to create a simple shopping list manager 
that allows users to add items, 
view the current list, and remove items.
"""
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Item")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    return choice

def add_item(shopping_list):
    item = input("Enter item: ")
    shopping_list.append(item)
    print("Item added to list.")

def remove_item(shopping_list):
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print("Item removed from list.")
    else:
        print("Item not found in list.")

def view_item(shopping_list):
    print("Shopping List:")
    for item in shopping_list:
        print(item)

def shopping_list_manager():
    shopping_list = []
    while True:
        choice = display_menu()
        if choice == 1:
            add_item(shopping_list)
        elif choice == 2:
            remove_item(shopping_list)
        elif choice == 3:
            view_item(shopping_list)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    shopping_list = []
    shopping_list_manager(shopping_list)

if __name__ == "__main__":
    main()