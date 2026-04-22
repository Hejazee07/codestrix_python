import json
import csv

with open("users.json", "r") as f:
    data = json.load(f)

with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "email", "name", "password", "phone", "address",
        "dob", "gender", "aadhaar",
        "account_number", "account_type", "balance", "pin"
    ])

    for email, user in data.items():
        writer.writerow([
            email,
            user["name"],
            user["password"],
            user["phone"],
            user["address"],
            user["dob"],
            user["gender"],
            user["aadhaar"],
            user["account_number"],
            user["account_type"],
            user["balance"],
            user["pin"]
        ])

with open("transactions.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["email", "type", "amount", "time"])

    for email, user in data.items():
        for t in user["transactions"]:
            writer.writerow([
                email,
                t["type"],
                t["amount"],
                t["time"]
            ])

print("Conversion complete: users.csv and transactions.csv created.")