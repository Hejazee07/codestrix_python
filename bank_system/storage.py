import json

FILE_NAME = "users.json"


def save_users(users_dict):
    data = {}

    for email, user in users_dict.items():
        data[email] = {
            "name": user.name,
            "password": user.password,
            "phone": user.phone,
            "address": user.address,
            "dob": user.dob,
            "gender": user.gender,
            "aadhaar": user.aadhaar,
            "account_number": user.account_number,
            "account_type": user.account.__class__.__name__,
            "balance": user.account.balance,
            "pin": user.account.pin,
            "transactions": user.account.transactions
        }

    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def load_users():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return {}