Student Attendance System
📌 Project Description

The Student Attendance System is a simple web-based application developed to manage and track student attendance efficiently.

The application allows users to add student details, mark students as Present or Absent, and view attendance reports with the calculated attendance percentage.

This project is developed as a beginner-friendly web development project to understand Python, Flask, HTML, CSS, and database management.

✨ Features

Add student details

View all students

Mark daily attendance

Mark students as Present or Absent

Select attendance date

View attendance reports

Calculate attendance percentage automatically

Store student and attendance data in SQLite database

Simple and responsive user interface

🛠️ Technologies Used

Python

Flask

HTML5

CSS3

SQLite

Jinja2

📂 Project Structure
student-attendance-system/
│
├── app.py
├── requirements.txt
├── attendance.db
│
├── templates/
│   ├── index.html
│   ├── add_student.html
│   ├── attendance.html
│   └── report.html
│
└── static/
    └── style.css

⚙️ How It Works

The application follows this workflow:

Add Students
     ↓
View Student List
     ↓
Select Attendance Date
     ↓
Mark Present / Absent
     ↓
Save Attendance
     ↓
Generate Attendance Report
     ↓
Calculate Attendance Percentage

🗄️ Database

The project uses SQLite to store information.

Students Table

Stores:

Student ID

Student Name

Roll Number

Course

Attendance Table

Stores:

Attendance ID

Student ID

Attendance Date

Attendance Status

🚀 Installation and Setup
1. Clone the repository
git clone https://github.com/your-username/student-attendance-system.git

2. Open the project folder
cd student-attendance-system

3. Create a virtual environment
python -m venv venv

4. Activate the virtual environment

For Windows:

venv\Scripts\activate


For Mac/Linux:

source venv/bin/activate

5. Install Flask
pip install -r requirements.txt

6. Run the application
python app.py

7. Open the application

Open the local Flask address shown in your terminal in a web browser.

📊 Attendance Calculation

The system calculates attendance using:

Attendance Percentage =
(Present Classes / Total Classes) × 100


For example:

Total Classes: 20
Present: 18
Absent: 2

Attendance Percentage: 90%

🎯 Learning Objectives

This project helps beginners understand:

Python programming

Flask framework

HTML and CSS

Web application development

SQLite databases

CRUD operations

Form handling

Database connectivity

Jinja2 templates

Basic attendance calculations

🔮 Future Enhancements

The project can be improved by adding:

Admin login and authentication

Teacher login

Student login

Edit and delete student records

Search functionality

Attendance history

Monthly attendance reports

Charts and graphs

PDF report generation

Excel export

Email notifications

QR-code based attendance

📸 Screenshots

Add screenshots of your application here:

Login Page
Dashboard
Student List
Mark Attendance
Attendance Report

👨‍💻 Author

Your Name

GitHub: Your GitHub Profile

📄 License

This project is created for educational and learning purposes.
