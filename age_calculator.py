from datetime import datetime

dob_input = input("Enter your Date of Birth (DD-MM-YYYY): ")

dob = datetime.strptime(dob_input, "%d-%m-%Y")
today = datetime.today()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Your age is:", age, "years")
