def add(d):
    name = input('Enter name: ')
    phone = input("Enter phone number: ")
    d[name] = phone
    print("\nContact added successfully!")


def search(d):
    name = input("Enter name: ")
    print("Phone number: ", d[name])


def list_contacts(d):
    print("Contacts")
    for keys, values in d.items():
        print(keys, ': ', values)

print("1.Add a new conact.\n2.Search for a contacts.\n3.List all contacts.\nExit ")
d = {}
while True:
    j = int(input("Enter your choice: "))
    if j == 1:
        add(d)
    elif j == 2:
        search(d)
    elif j == 3:
        list_contacts(d)
    else:
        print("Goodbye!")
        break
