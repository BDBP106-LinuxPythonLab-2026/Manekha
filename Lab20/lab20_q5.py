shopping_list = []

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Sort list")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")

        if item.lower() in [x.lower() for x in shopping_list]:
            print("Item already exists!")
        else:
            shopping_list.append(item)
            print("Item added successfully.")

    elif choice == "2":
        item = input("Enter item to remove: ")

        for x in shopping_list:
            if x.lower() == item.lower():
                shopping_list.remove(x)
                print("Item removed successfully.")
                break
        else:
            print("Item not found!")

    elif choice == "3":
        if len(shopping_list) == 0:
            print("Shopping list is empty.")
        else:
            for i, item in enumerate(shopping_list, start=1):
                print(i, item)

    elif choice == "4":
        shopping_list.sort(key=str.lower)
        print("Shopping list sorted.")

    elif choice == "5":
        print("Exiting shopping list manager.")
        break

    else:
        print("Invalid choice. Please try again.")