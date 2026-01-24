# Patrick Davis
# SDEV220_M2_Lab-Patrick_Davis.py
# This program prompts the user to enter their last name, first name, and GPA
# in order to determine if they have made the Dean's List or Honor Roll.

last_name = input("Enter your last name: ")
while last_name != 'ZZZ':
    first_name = input("Enter your first name: ")
    gpa = float(input("Enter your GPA: "))
    if gpa >= 3.5:
        print("You have made the Dean's List.")
    else:
        print("You have not made the Dean's List.")
    if gpa >= 3.25:
        print("You have made the Honor Roll.")
    else:
        print("You have not made the Honor Roll.")
    last_name = input("Enter your last name: ")
else:
    print("Program terminated.")