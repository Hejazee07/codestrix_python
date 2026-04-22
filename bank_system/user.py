from accounts import Savings, Current, Student
import re
import random


def is_valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)


def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True


class User:
    def __init__(self, name, email, password, phone, address, dob, gender, aadhaar, account):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.address = address
        self.dob = dob
        self.gender = gender
        self.aadhaar = aadhaar
        self.account = account
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        return random.randint(1000000000, 9999999999)

    def show_details(self):
        print(f"\nName: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
        print(f"DOB: {self.dob}")
        print(f"Gender: {self.gender}")
        print(f"Aadhaar: {self.aadhaar}")
        print(f"Account No: {self.account_number}")
        print(f"Account Type: {self.account.type_of_account()}")


class NewUser(User):

    @classmethod
    def create_user(cls):
        name = input("Enter your full name: ").strip()

        while True:
            email = input("Enter your email: ").strip()
            if is_valid_email(email):
                break
            print("Invalid email format")

        while True:
            password = input("Create password: ").strip()
            if is_strong_password(password):
                break
            print("Weak password")

        while True:
            phone = input("Enter phone number: ")
            if phone.isdigit() and len(phone) == 10:
                break
            print("Invalid phone number")

        address = input("Enter address: ")
        dob = input("Enter DOB: ")
        gender = input("Enter gender: ")

        while True:
            aadhaar = input("Enter Aadhaar: ")
            if aadhaar.isdigit() and len(aadhaar) == 12:
                break
            print("Invalid Aadhaar")

        while True:
            pin_input = input("Set 4 digit PIN: ")
            if pin_input.isdigit() and len(pin_input) == 4:
                pin = int(pin_input)
                break
            print("Invalid PIN")

        print("1) Savings  2) Current  3) Student")
        choice = input("Choose: ")

        account = create_account(choice, pin)
        if account is None:
            return None

        return cls(name, email, password, phone, address, dob, gender, aadhaar, account)


class OldUser:

    @staticmethod
    def login(users_dict):
        email = input("Email: ")
        password = input("Password: ")

        user = users_dict.get(email)

        if not user:
            print("User not found")
            return None

        if user.password != password:
            print("Wrong password")
            return None

        print(f"Welcome {user.name}")
        return user


def create_account(choice, pin):
    if choice == "1":
        return Savings(pin)
    elif choice == "2":
        return Current(pin)
    elif choice == "3":
        return Student(pin)
    return None


def add_user(users_dict, user):
    if user.email in users_dict:
        print("User exists")
        return False

    users_dict[user.email] = user
    print("User created")
    return True