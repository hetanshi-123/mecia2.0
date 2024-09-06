# from flask import Flask, request, jsonify
# import mysql.connector
# from mysql.connector import Error

# app = Flask(__name__)

# # Database configuration
# db_config = {
#     'host': 'localhost',
#     'database': 'trash2treasure',
#     'user': 'your_username',
#     'password': 'your_password'
# }

# # Route for handling registration
# @app.route('/register', methods=['POST'])
# def register():
#     try:
#         # Extract data from request
#         data = request.get_json()
#         name = data.get('name')
#         email = data.get('email')
#         contact_no = data.get('contact_no')
#         address = data.get('address')
        
#         # Connect to the database
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor()

#         # Insert data into the database
#         query = """
#         INSERT INTO users (name, email, contact_no, address)
#         VALUES (%s, %s, %s, %s)
#         """
#         values = (name, email, contact_no, address)
#         cursor.execute(query, values)
#         connection.commit()

#         return jsonify({'message': 'Registration successful!'}), 200

#     except Error as e:
#         print(f"Error: {e}")
#         return jsonify({'message': 'Registration failed!'}), 500

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# if __name__ == '__main__':
#     app.run(debug=True)

import mysql.connector

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="22111101@2005",
            database="REGISTRATIONS"
        )
        if conn.is_connected():
            print("Successfully connected to the database")
            return conn
    except mysql.connector.Error as err:
        print("Error: {err}")
        return None

def insert_user(Name, Email, Contact_no, Address):
    conn = connect_to_database()
    if conn is None:
        return "Connection failed"
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO USER(Name, Email, Contact_no, Address) VALUES (%s, %s, %d, %s)"
        values = (Name, Email, Contact_no, Address)
        cursor.execute(query, values)
        conn.commit()
        return "User registered successfully"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Failed to register user"
    finally:
        cursor.close()
        conn.close()

