class User:
    def _init_(self, email,  name, age, address):
        self.email = email
        self.name = name
        self.age = age
        self.address = address


class UserDatabase:
    db = {}

    def add_user_data(self, u1):
        if u1.email not in self.db:
            self.db[u1.email] = {'name':u1.name, 'age':u1.age, 'address':u1.address}
            print("User added successfully")
            print(self.db)
        else:
            print("User already exists")

    def remove_user_data(self, email_remove):
        if email_remove in self.db:
            removed = self.db.pop(email)
            print(removed["name"], "Removed Successfully")
        else:
            print("User Doesn't Exists")

    def display_user_data(self):
        if self.db:
            print(self.db)
        else:
            print("Database Empty")


def add_user():
    email = input("Enter your Email:")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your Address:")
    u1 = User(email, name, age, address)
    return u1


user2 = UserDatabase()
while True:
    print("1. Add User Data")
    print("2. Remove User Data")
    print("3. Display User Data")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        user1 = add_user()
        user2.add_user_data(user1)
    elif choice == 2:
        email = input("Please enter email that you want to remove: ")
        user2.remove_user_data(email)

    elif choice == 3:
        user2.display_user_data()
    elif choice == 4:
        break

