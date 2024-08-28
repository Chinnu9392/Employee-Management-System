from database import create_employee, get_all_employees, update_employee_role, create_employee_table

# Initialize the database (create the table if it doesn't exist)
create_employee_table()

def main():
    while True:
        print("\n1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee Role")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            role = input("Enter Role: ")
            salary = float(input("Enter Salary: "))
            create_employee(emp_id, name, department, role, salary)
            print("Employee added successfully.")
        
        elif choice == '2':
            employees = get_all_employees()
            for emp in employees:
                print(f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, Role: {emp[3]}, Salary: {emp[4]}")
        
        elif choice == '3':
            emp_id = int(input("Enter Employee ID to update role: "))
            new_role = input("Enter new role: ")
            update_employee_role(emp_id, new_role)
            print("Role updated successfully.")
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
