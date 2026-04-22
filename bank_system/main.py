from user import NewUser, OldUser, add_user, User
from accounts import Savings, Current, Student
from storage import save_users, load_users


def reconstruct_users(data):
    users = {}

    for email, u in data.items():

        if u["account_type"] == "Savings":
            acc = Savings(u["pin"])
        elif u["account_type"] == "Current":
            acc = Current(u["pin"])
        else:
            acc = Student(u["pin"])

        acc.balance = u["balance"]
        acc.transactions = u["transactions"]

        user_obj = User(
            u["name"],
            email,
            u["password"],
            u["phone"],
            u["address"],
            u["dob"],
            u["gender"],
            u["aadhaar"],
            acc
        )

        user_obj.account_number = u["account_number"]

        users[email] = user_obj

    return users


users_data = reconstruct_users(load_users())


def account_menu(user):
    acc = user.account

    print(f"\nLogged in as {user.name}")
    print(acc.type_of_account())

    while True:
        print("\n1) Deposit 2) Withdraw 3) Transactions 4) Details 5) Balance 6) Logout")
        ch = input("Choose: ")

        if ch == "1":
            try:
                amt = int(input("Amount: "))
                print(acc.deposit(amt))
                save_users(users_data)
            except:
                print("Invalid input")

        elif ch == "2":
            try:
                amt = int(input("Amount: "))
                pin = int(input("PIN: "))
                print(acc.withdraw(amt, pin))
                save_users(users_data)
            except:
                print("Invalid input")

        elif ch == "3":
            print(acc.show_transactions())

        elif ch == "4":
            user.show_details()

        elif ch == "5":
            print("Balance:", acc.check_balance())

        elif ch == "6":
            break

        else:
            print("Invalid")


def main():
    while True:
        print("\n1) New 2) Login 3) Show Users 4) Exit")
        op = input("Choose: ")

        if op == "1":
            u = NewUser.create_user()
            if u and add_user(users_data, u):
                save_users(users_data)
                account_menu(u)

        elif op == "2":
            u = OldUser.login(users_data)
            if u:
                account_menu(u)

        elif op == "3":
            for u in users_data.values():
                print(u.name, u.email)

        elif op == "4":
            save_users(users_data)
            break


if __name__ == "__main__":
    main()