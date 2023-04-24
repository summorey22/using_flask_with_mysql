from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

# Initialize the Flask application
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'name_of_your_database'

# Configure MySQL
mysql = MySQL(app)

# Index page
@app.route('/')
def index():
    return render_template('index.html')

# Fetch data from MySQL database table and return as JSON
@app.route('/data')
def get_data():
    cursor = mysql.connection.cursor()

    # Execute query
    query = "SELECT * FROM sample"
    cursor.execute(query)

    # Fetch results
    results = cursor.fetchall()

    # Close connection
    cursor.close()

    # Return results as JSON
    return jsonify(results)