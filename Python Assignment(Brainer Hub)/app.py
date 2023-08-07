from flask import Flask, request, \
    jsonify  # Import Flask and request module for handling HTTP requests and jsonify for responses
from flask_cors import CORS  # Import CORS for enabling Cross-Origin Resource Sharing
import service.operations as op  # Import your operations module

# start the
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for handling requests from different origins
cors = CORS(app)


# Endpoint to upload a .csv or .xlsx file containing employee data
@app.route("/file/upload", methods=["POST"])
def upload_csv_or_excel():
    try:
        file = request.files['file']  # Get the uploaded file from the request
    except:
        return jsonify({"message": "File not found"}), 400  # an error response if the file is not found

    return op.upload_file(file)  # Delegate the file upload operation to operations module


# Endpoint to retrieve employees (optionally for a specific company)
@app.route("/file/employee", methods=["GET"])
def get_employees():
    company_name = request.args.get('name', None)  # Get the 'name' query parameter from the request
    return op.get_all_employees(company_name)  # Delegate the employee retrieval operation to operations module


# Endpoint to retrieve all companies
@app.route("/file/company", methods=["GET"])
def get_companies():
    return op.get_all_companies()  # Delegate the company retrieval operation to operations module


# Run the Flask app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # Start the app in debug mode
