def display_menu():
    print("Shopping list manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Item")
    print("4. Exit")
def main():
    shooping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            shooping_list.append(input("Enter the item to add: "))
        elif choice == "2":
            shopping_list.remove(input("Remove an Item: "))
        elif choice == "3":
            for item in shopping_list:
                print(item)
        elif choice == "4":
            print("chrih a3chiri ^^")
            break
        else:
            print("Invalid choice. Please try again.")
main()
