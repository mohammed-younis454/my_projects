import time
import os
members = []
class Member:
    def __init__(self, fname, lname, ID, age, status):
        self.fname = fname
        self.lname = lname
        self.ID = ID
        self.age = age
        self.status = status

def create_member():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    id = input("Enter membership ID: ")
    age = input("Enter the member`s age: ")
    status = input("Enter membership status Or click enter: ").lower()
    if status != "active":
        status = "inactive"
    return Member(fname, lname, id, age, status)

def display_members():
    print("Displaying all members .....\n")
    time.sleep(0.5)
    for member in members:
        print(f"""
First Name: {member.fname}
Last Name: {member.lname}
Membership ID: {member.ID}
Member`s age: {member.age}
Membership Status: {member.status}
------------------------------
""")
        time.sleep(2)

def searching_members():
    print("""\n
Search by:\n
1. Membership ID
2. First Name
3. Membership status
          
""")
    s_choice = int(input("Enter your choice: "))
    if s_choice == 1:
        s_id = input("Enter the membership ID: ")
        os.system("cls")
        print("Members found:")
        for member in members:
            if member.ID == s_id:
                print(f"""
First Name: {member.fname}
Last Name: {member.lname}
Membership ID: {member.ID}
Member`s age: {member.age}
Membership Status: {member.status}
------------------------------
""")
    elif s_choice == 2:
        s_name = input("Enter the First Name: ")
        os.system("cls")
        print("Members found:")
        for member in members:
            if member.fname == s_name:
                print(f"""
First Name: {member.fname}
Last Name: {member.lname}
Membership ID: {member.ID}
Member`s age: {member.age}
Membership Status: {member.status}
------------------------------
""")
    elif s_choice == 3:
        s_status = input("Enter the Membership Status (active / inactive): ").lower()
        os.system("cls")
        print("Members found:")
        for member in members:
            if member.status == s_status:
                print(f"""
First Name: {member.fname}
Last Name: {member.lname}
Membership ID: {member.ID}
Member`s age: {member.age}
Membership Status: {member.status}
------------------------------
""")

while True:
    os.system("cls")
    print("\nWelcome to Gym Membership Management\n")
    print("""
Choose an action:
          
1. Add new member
2. Display all members
3. Search for a member
4. Exit
          
""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        os.system("cls")
        member = create_member()
        members.append(member)
        print("Member added successfully!\n")
        time.sleep(2)
    elif choice == 2:
        os.system("cls")
        display_members()
        input("Press Enter to return to the main menu...")
    elif choice == 3:
        os.system("cls")
        searching_members()
        input("Press Enter to return to the main menu...")
    elif choice == 4:
        print("Exiting .......")
        time.sleep(1.5)
        break
    else:
        print("Invailed choice.")
        time.sleep(1)