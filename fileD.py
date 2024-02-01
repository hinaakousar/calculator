def add_candidate(user_date):
    email = input("Please Enter your email ")
    if email in user_data:
        print("Candidate Already Exists with this email")
        return
    name = input("Enter Candidate Name: ")
    age = int(input("Enter Candidate Age: "))
    address = input("Enter the Candidate Address: ")
    user_data[email] = {"name": name, "age": age, "address": address}
    print("Data added successfully!")

def remove_candidate(user_data):
    email = input("Please enter the Candidate email that you want to remove: ")
    if email in user_data:
        removed_user= user_data.pop(email)
        print(removed_user["name"], "has ben removed Sucessfully")
    else:
        print("Candidate with this email doesnt exists")

def search_candidate(user_data):
     email = input("Please enter the Candidate email that you want to Find Out: ")
     if email not in user_data:
         print("Candidate with this email doesnt exists")
         return
     print(user_data[email])

def display_candidates(user_data):
    print("All Candidates Data")
    for i in user_data.items():
        print(i)


user_data= {}
while True:
    print("1. For Candidate Addition ")
    print("2. For Candidate Removal ")
    print("3. For Candidate Searching ")
    print("4. Display all data ")
    print("5. For Exit ")
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        add_candidate(user_data)
    elif choice == 2:
        remove_candidate(user_data)
    elif choice == 3:
        search_candidate(user_data)
    elif choice == 4:
        display_candidates(user_data)
    elif choice == 5:
        break
    else:
        print("Please provide the valid Input")