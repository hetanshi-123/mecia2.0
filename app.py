# from flask import Flask, request, jsonify
# import db_connect

# app = Flask(__name__)

# @app.route('/REGISTRATION', methods=['POST'])
# def Register():
#     data = request.get_json()
#     name = data.get('name')
#     email = data.get('email')
#     contact_no = data.get('contactNo')
#     address = data.get('address')

#     message = db_connect.insert_user(name, email, contact_no, address)
#     return jsonify({'message': message})

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, request, redirect, url_for, render_template
# import mysql.connector

# app = Flask(_
# _name__)

# # Database connection configuration
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '22111101@2005',
#     'database': 'REGISTRATION'
# }

# @app.route('/register', methods=['POST'])
# def register():
#     print()
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         contact_no = request.form['contact No.']
#         address = request.form['address']
#         print(request)
#         # Connect to the database
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor()
        
#         # Insert data into the database
#         cursor.execute(
#             "INSERT INTO Users (name, email, contact_no, address) VALUES (%s, %s, %s, %s)",
#             (name, email, contact_no, address)
#         )
#         conn.commit()
        
#         cursor.close()
#         conn.close()
        
#         return redirect(url_for('success'))
    
#     return render_template('registration.html')

# @app.route('/success')
# def success():
#     return 'Registration successful!'

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/Register')
def register():
    return render_template('r.html')

@app.route('/Register', methods=['POST'])
def Register():
    # Extract data from the form
    Name = request.form.get('Name')
    Email = request.form.get('Email')
    Contact_no = request.form.get('Contact_no')
    Address = request.form.get('Address')
    
    return f'Name: {Name}, Email: {Email}, Contact No : {Contact_no} , Address :{Address}'

if __name__ == '__main__':
    app.run(debug=True)
