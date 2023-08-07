# Brainer-Hub-assignment

## Introduction

This repository contains a well-written Python application that uses Flask and MongoDB to manage employee data and company information. The application provides REST APIs to upload employee data from CSV or Excel files, retrieve employees from specific companies, and fetch all company information. This README will guide you through the process of setting up and running the application.

## Getting Started

### Prerequisites

To run the Python application, you need to have the following dependencies installed on your system:

1. Python (version 3.6 or higher)
2. Flask (web framework for Python)
3. pymongo (Python driver for MongoDB)
4. pandas (data manipulation library)

You can install these dependencies using `pip`, the Python package manager. Open a terminal or command prompt and run the following commands:

```bash
pip install Flask pymongo pandas
```

### MongoDB Configuration

The application is configured to use a MongoDB Atlas cluster to store data. To set up your MongoDB cluster, follow these steps:

1. Sign up or log in to your MongoDB Atlas account at https://www.mongodb.com/cloud/atlas.
2. Create a new cluster by following the instructions provided by MongoDB Atlas.
3. After setting up the cluster, create a new database named "PythonAssignment" with two collections: "Company" and "Employee."

### Running the Application

1. Clone this repository to your local machine.
2. Open the terminal or command prompt and navigate to the root directory of the cloned repository.

#### Configure MongoDB Credentials

Before running the application, make sure to update the credentials in `database.py`:

```python
# database.py

username = "your_mongodb_username"
password = "your_mongodb_password"
```

Replace `your_mongodb_username` and `your_mongodb_password` with your actual MongoDB Atlas credentials.

#### Start the Flask Application

Run the `app.py` file to start the Flask application:

```bash
python app.py
```

The application will start, and you should see an output similar to:

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

The application is now up and running on `http://127.0.0.1:5000/`.

## REST APIs

The application provides the following REST APIs:

### 1. Upload Employee Data

**Endpoint:** `/file/upload`
**Method:** `POST`
**Description:** Upload a CSV or Excel file containing employee data to the database.

### 2. Retrieve Employees

**Endpoint:** `/file/employee`
**Method:** `GET`
**Description:** Retrieve all employees or employees from a specific company.

**Query Parameters:**
- `name` (optional): Specify the company name to get employees from a specific company.

### 3. Retrieve All Companies

**Endpoint:** `/file/company`
**Method:** `GET`
**Description:** Retrieve a list of all companies.

## Usage

1. Use any API testing tool (e.g., Postman, cURL, or web browser) to interact with the provided APIs.
2. Upload employee data by sending a POST request to `/file/upload` with a valid CSV or Excel file.
3. Retrieve employees from a specific company or all employees by sending a GET request to `/file/employee` with optional query parameter `name`.
4. Fetch all companies by sending a GET request to `/file/company`.

## Conclusion

Congratulations! You now have a fully functional Python application that uses Flask and MongoDB to manage employee data and company information. Feel free to explore and extend the application based on your specific requirements. If you encounter any issues or have any questions, please don't hesitate to reach out for assistance.

Happy coding!
