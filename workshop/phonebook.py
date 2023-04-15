phonebook = {}
choice= 0
while choice != 5:
    choice = int(input("Please select an option: \n1. List Phone Book\n2. Add Number\n3. Delete Number\n4. Update Number\n5. Quit"))
    if choice == 1:
        print(phonebook)
    elif choice == 2:
        name = input("Enter name: ")
        phone = input("Enter phone : ")
        phonebook[name] = phone
    elif choice == 3:
        print(phonebook)
        delete = input("Input a name of person that you want to delete: ")
        del phonebook[delete]
    elif choice == 4:
        print(phonebook)
        updatename = input("Input a name of person that you want to update: ")
        newphone = input("Input person's new phone number")
        phonebook.update({updatename: newphone})
    elif choice == 5:
        quit()
    else:
        print("Invalid")









