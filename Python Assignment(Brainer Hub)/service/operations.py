from models.database import companyDb, employeeDb  # Importing the database models
from flask import Flask, jsonify  # Import Flask and jsonify for API responses
import pandas as pd  # Import pandas for handling data frames


# Function to upload a file (.csv or .xlsx ) containing employee data to the database
def upload_file(file):
    if file.filename.endswith('.csv'):  # Check if the file is a CSV
        data = pd.read_csv(file)  # Read the CSV file into a pandas DataFrame
    elif file.filename.endswith('.xlsx'):  # Check if the file is an Excel file
        data = pd.read_excel(file)  # Read the Excel file into a pandas DataFrame
    else:
        return jsonify(
            {'message': 'Invalid file format'}), 400  # Return an error response if the file format is invalid

    companies = {}  # Create a dictionary to store company information
    employees = []  # Create a list to store employee information

    for _, row in data.iterrows():
        company_name = row["COMPANY_NAME"]  # Get the company name from the row
        if company_name not in companies:
            company = {"company_name": company_name}  # Create a company object with the name
            companies[company_name] = companyDb.insert_one(
                company).inserted_id  # Insert the company into the company database and store its ID
        # Create an employee object with information from the row
        employee = {
            "company_name": company_name,
            "first_name": row["FIRST_NAME"],
            "last_name": row["LAST_NAME"],
            "phone_number": row["PHONE_NUMBER"].replace(".", ""),  # removing the dots(.) in the phone number
            "employee_id": row["EMPLOYEE_ID"],
            "salary": row["SALARY"],
            "manager_id": row["MANAGER_ID"],
            "department_id": row["DEPARTMENT_ID"]
        }
        employees.append(employee)  # Add the employee to the list of employees
    employeeDb.insert_many(employees)  # Insert all employees into the employee database
    return jsonify({"message": "Data is successfully stored in the Database"}), 201  # Return a success response


# Function to get all employees from a specific company (or all companies if company_name is None)
def get_all_employees(company_name):
    if company_name is None:
        employees = list(employeeDb.find())  # Get all employees if company_name is None
    else:
        employees = list(employeeDb.find({"company_name": company_name}))  # Get employees from the specified company
    if len(employees) == 0:
        return jsonify({"message": "No employees Found"})  # Return a message if no employees are found
    for employee in employees:
        del employee["_id"]  # Remove the MongoDB _id field from each employee
    return jsonify(employees), 200  # Return the list of employees


# Function to get all companies from the company database
def get_all_companies():
    companies = list(companyDb.find())  # Get all companies from the company database
    if len(companies) == 0:
        return jsonify({"message": "No companies Found"}), 403  # Return a message if no companies are found
    for company in companies:
        del company["_id"]  # Remove the MongoDB _id field from each company
    return jsonify(companies), 200  # Return the list of companies
