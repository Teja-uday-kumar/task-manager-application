📝 Task Manager Application
 Project Description

The Task Manager Application is a full-stack web application built using Django that allows users to manage their daily tasks efficiently.
Users can create an account, log in securely, and perform operations such as adding, viewing, editing, and deleting their own tasks.

Each user has a private dashboard, ensuring that tasks are accessible only to the user who created them.

🚀 Features

User Registration and Login

Secure Authentication and Session Management

User-specific Task Dashboard

Add New Tasks

Edit Existing Tasks

Delete Tasks

Success and Error Messages

Clean and Responsive User Interface

🛠️ Technologies Used
Frontend

HTML

CSS

Django Templates

Backend

Python

Django Framework

Database

MySQL (Local Development)

PostgreSQL (Production)

Tools & Deployment

Git & GitHub

Render

Gunicorn

WhiteNoise

⚙️ Installation

Follow the steps below to run the project locally:

1️⃣ Clone the Repository
git clone https://github.com/yourusername/task-manager-application.git
cd task-manager-application

2️⃣ Create and Activate Virtual Environment
python -m venv myenv
myenv\Scripts\activate   # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Database

Create a MySQL database and update database settings in settings.py.

CREATE DATABASE taskmanager_db;

5️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Run the Server
python manage.py runserver


Open your browser and go to:

http://127.0.0.1:8000/

▶️ Usage

Open the application in your browser.

Register a new user account.

Log in using your credentials.

Access the dashboard to manage tasks.

Add, update, or delete tasks as needed.

Log out when finished.

⭐ Conclusion

This project demonstrates a real-world Django application workflow, including authentication, CRUD operations, and production-ready deployment practices.
