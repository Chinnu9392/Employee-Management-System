import mysql.connector

# Establish a connection to the MySQL database
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # replace with your MySQL username
        password="root",   # replace with your MySQL password
        database="employee_db"      # replace with your database name
    )

# Create the Employee table if it doesn't exist
def create_employee_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INT PRIMARY KEY,
        name VARCHAR(100),
        department VARCHAR(100),
        role VARCHAR(100),
        salary DECIMAL(10, 2)
    )
    """)
    conn.commit()
    conn.close()

# Function to create (add) a new employee to the database
def create_employee(emp_id, name, department, role, salary):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO employees (emp_id, name, department, role, salary)
    VALUES (%s, %s, %s, %s, %s)
    """, (emp_id, name, department, role, salary))
    conn.commit()
    conn.close()

# Function to retrieve all employees from the database
def get_all_employees():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    conn.close()
    return employees

# Function to update an employee's role
def update_employee_role(emp_id, new_role):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE employees SET role = %s WHERE emp_id = %s
    """, (new_role, emp_id))
    conn.commit()
    conn.close()
