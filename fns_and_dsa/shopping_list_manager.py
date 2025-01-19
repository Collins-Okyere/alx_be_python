# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list
    while True:  # Loop to continuously display the menu
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':  # Add an item
            item = input("Enter the item to add: ").strip()
            if item:  # Ensure the item name is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item name cannot be empty. Please try again.")
        elif choice == '2':  # Remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:  # Check if the item exists
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the list. Please check the name and try again.")
        elif choice == '3':  # Display the shopping list
            if shopping_list:  # If the list is not empty
                print("\nCurrent Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == '4':  # Exit the program
            print("Goodbye!")
            break
        else:  # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 4.")
