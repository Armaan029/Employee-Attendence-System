# It is an Employee Attendence System

import json
import os
import datetime
import getpass

EMP_FILE = "employees.json"
ATT_FILE = "attendance.json"
ADMIN_ID = "0029"
SECRET_CODE = "202129"

# Load Data
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return {}

employees = load_data(EMP_FILE)
attendance = load_data(ATT_FILE)

# Save Data
def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Admin Login
def admin_login():
    tries = 3
    while tries > 0:
        emp_id = getpass.getpass("Enter Admin Employee ID (hidden): ")
        code = getpass.getpass("Enter Secret Code (hidden): ")
        if emp_id == ADMIN_ID and code == SECRET_CODE:
            return True
        else:
            tries -= 1
            print(f"Wrong credentials! {tries} tries left.\n")
    print("Too many failed attempts. Access denied.\n")
    return False

# Add Employee
def add_employee():
    if not admin_login():
        return
    emp_id = input("Enter Employee ID: ")
    if emp_id in employees:
        print("Employee ID already exists!\n")
        return
    name = input("Enter Name: ")
    profession = input("Enter Profession: ")
    salary = input("Enter Salary: ")
    employees[emp_id] = {"name": name, "profession": profession, "salary": salary}
    save_data(EMP_FILE, employees)
    print("Employee added successfully!\n")

# Remove Employee
def remove_employee():
    if not admin_login():
        return
    emp_id = input("Enter Employee ID to remove: ")
    if emp_id in employees:
        del employees[emp_id]
        save_data(EMP_FILE, employees)
        print("Employee removed successfully!\n")
    else:
        print("Employee not found!\n")

# Check In
def check_in():
    emp_id = input("Enter Employee ID: ")
    if emp_id not in employees:
        print("Employee not found!\n")
        return
    today = str(datetime.date.today())
    if today not in attendance:
        attendance[today] = []
    for record in attendance[today]:
        if record["id"] == emp_id and record["check_out"] is None:
            print("You are already checked in!\n")
            return
    check_in_time = str(datetime.datetime.now().time()).split('.')[0]
    attendance[today].append({
        "id": emp_id,
        "name": employees[emp_id]["name"],
        "profession": employees[emp_id]["profession"],
        "salary": employees[emp_id]["salary"],
        "check_in": check_in_time,
        "check_out": None
    })
    save_data(ATT_FILE, attendance)
    print(f"Check-in successful for {employees[emp_id]['name']} at {check_in_time}\n")

# Check Out
def check_out():
    emp_id = input("Enter Employee ID: ")
    today = str(datetime.date.today())
    if today in attendance:
        for record in attendance[today]:
            if record["id"] == emp_id and record["check_out"] is None:
                check_out_time = str(datetime.datetime.now().time()).split('.')[0]
                record["check_out"] = check_out_time
                save_data(ATT_FILE, attendance)
                print(f"Check-out successful for {employees[emp_id]['name']} at {check_out_time}\n")
                return
        print("You have not checked in yet or already checked out!\n")
    else:
        print("No check-in record found!\n")

# View History
def view_history():
    if not admin_login():
        return
    date_input = input("Enter date (YYYY-MM-DD): ")
    if date_input in attendance:
        print(f"\n--- Attendance History for {date_input} ---")
        for record in attendance[date_input]:
            check_out_display = record['check_out'] if record['check_out'] else "Still Checked In"
            print(f"ID: {record['id']}, Name: {record['name']}, "
                  f"Profession: {record['profession']}, Salary: {record['salary']}, "
                  f"Check-In: {record['check_in']}, Check-Out: {check_out_display}")
        print("-------------------------------------------\n")
    else:
        print("No attendance records for this date.\n")

# Total Employees
def total_employees():
    if not admin_login():
        return
    print("\n--- Employee Details ---")
    for emp_id, details in employees.items():
        print(f"ID: {emp_id}")
        print(f"Name: {details['name']}")
        print(f"Profession: {details['profession']}")
        print(f"Salary: {details['salary']}")
        print("---------------------------")
    print(f"Total Employees: {len(employees)}\n")

# Main Menu
def main():
    while True:
        print("1. Check In")
        print("2. Check Out")
        print("3. Add Employee (Admin)")
        print("4. Remove Employee (Admin)")
        print("5. View History (Admin)")
        print("6. View All Employees (Admin)")
        print("7. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            check_in()
        elif choice == "2":
            check_out()
        elif choice == "3":
            add_employee()
        elif choice == "4":
            remove_employee()
        elif choice == "5":
            view_history()
        elif choice == "6":
            total_employees()
        elif choice == "7":
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()

