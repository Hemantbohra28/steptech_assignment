from flask import Flask, render_template, request, jsonify

from flask_mysqldb import MySQL

 

app = Flask(__name__)

 

# MySQL Configuration

app.config['MYSQL_HOST'] = 'localhost'

app.config['MYSQL_USER'] = 'root'

app.config['MYSQL_PASSWORD'] = '224570'

app.config['MYSQL_DB'] = 'users'

 

mysql = MySQL(app)

 

# Task 1: Flask API Development

 

@app.route('/hello')

def hello():

    return "Hello, World!"

 

@app.route('/users')

def users():

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM users")

    users = cur.fetchall()

    cur.close()

    return render_template('users.html', users=users)

 

@app.route('/new_user', methods=['GET', 'POST'])

def new_user():

    if request.method == 'POST':

        name = request.form['name']

        email = request.form['email']

        role = request.form['role']

 

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", (name, email, role))

        mysql.connection.commit()

        cur.close()

 

        return 'User added successfully'

 

    return render_template('new_user.html')

 

@app.route('/users/<int:user_id>')

def user(user_id):

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))

    user = cur.fetchone()

    cur.close()

    if user:

        return jsonify(user)

    else:

        return 'User not found', 404

 

# Task 2: Database Interaction

 

# SQL queries

 

# Insert sample data

sample_data_inserted = False

def insert_sample_data():
    global sample_data_inserted
    if not sample_data_inserted:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", ('Hemant', 'hemant@gmail.com', 'admin'))
        cur.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", ('Ak', 'AK@gmail.com', 'user'))
        mysql.connection.commit()
        cur.close()
        sample_data_inserted = True

@app.before_request
def before_request():
    insert_sample_data()


 

# Retrieve all users

def get_all_users():

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM users")

    users = cur.fetchall()

    cur.close()

    return users

 

# Retrieve a specific user by their ID

def get_user_by_id(user_id):

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))

    user = cur.fetchone()

    cur.close()

    return user

 

if __name__ == '__main__':app.run(debug=True)