# Author: Blake Fox
# File Name: student_awards_checker.py
# Description: This app accepts student names and GPAs, tests whether
#              they qualify for the Dean's List or Honor Roll, and
#              provides the corresponding messages.

while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    
    if last_name.upper() == 'ZZZ':
        print("Exiting the program. Goodbye!")
        break
    
    first_name = input("Enter the student's first name: ")
    
    try:
        gpa = float(input("Enter the student's GPA: "))
    except ValueError:
        print("Invalid GPA entered. Please enter a valid numeric value.")
        continue
    
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List!")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll!")
    else:
        print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")

    print()