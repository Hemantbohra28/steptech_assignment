FLASK USER MANAGEMENT API

Introduction:
This Flask application serves as an API for managing user data. It includes endpoints for retrieving users, adding new users, and retrieving a specific user by their ID.
Table of Contents:
1.	Setup and Run
2.	Database Schema
3.	Populating Sample Data
4.	Dependencies and Setup
5.	Git Workflow and Contribution
   Setup and Run:
   To set up and run the Flask application, follow these steps:
    1. Clone the Repository: Clone this repository to your local machine:
         git clone https://github.com/your-username/flask-user-management.git
    2. Navigate to Project Directory: Change your current directory to the cloned project directory:
         cd flask-user-management
    3. Install Dependencies: Install the required Python dependencies using pip:
          pip install -r requirements.txt
    4. Set Up MySQL Database: Ensure you have a MySQL server running locally or on a remote server.
       Configure the MySQL connection parameters in the Flask application (app.py) according to your database setup:
            app.config['MYSQL_HOST'] = 'localhost'
                app.config['MYSQL_USER'] = 'root'
               app.config['MYSQL_PASSWORD'] = '1234'
               app.config['MYSQL_DB'] = 'users'

    5.	Run the Application: Start the Flask application:
            python app.py
        The application will be accessible at http://localhost:5000.

     Database Schema:
      The database schema consists of a single table named users with the following columns:
           id (INT): Primary key, auto-incremented.
           name (VARCHAR): Name of the user.
           email (VARCHAR): Email address of the user.
           role (VARCHAR): Role of the user.

     Populating Sample Data
The application automatically inserts sample data into the users table when it starts.
Two sample users are inserted:
Name: Hemant, Email: hemant@gmail.com, Role: admin
Name: AK, Email: AK@gmail.com, Role: user

Dependencies and Setup:
This Flask application relies on the following dependencies:
•	Flask
•	Flask-MySQLdb
    Install the dependencies using:
      pip install -r requirements.txt

Git Workflow and Contribution:
Contributions to this project are welcome! Follow these steps to contribute:
1.	Fork the Repository: Fork this repository to your GitHub account.
2.	Clone Your Fork: Clone your forked repository to your local machine.
3.	Create a New Branch: Create a new branch for your changes:
                           git checkout -b feature-branch
4.	Make Changes: Make your changes, add new features, or fix bugs.
5.	Commit Your Changes: Commit your changes with descriptive commit messages:
git add .
git commit -m "Description of changes"

6.	Push Changes: Push your changes to your forked repository:
                             git push origin feature-branch
7.	Create a Pull Request: Submit a pull request from your branch to the main   repository's master branch.
8.	Review and Merge: Your pull request will be reviewed, and if approved, it will be merged into the main branch.

