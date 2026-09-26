from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import date

app = Flask(__name__)

DATABASE = "attendance.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_number TEXT NOT NULL UNIQUE,
            course TEXT NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            attendance_date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students (id)
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = get_db_connection()
    students = conn.execute(
        "SELECT * FROM students ORDER BY id DESC"
    ).fetchall()
    conn.close()

    return render_template("index.html", students=students)


@app.route("/add", methods=("GET", "POST"))
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        roll_number = request.form["roll_number"]
        course = request.form["course"]

        conn = get_db_connection()

        try:
            conn.execute(
                "INSERT INTO students (name, roll_number, course) VALUES (?, ?, ?)",
                (name, roll_number, course)
            )
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return "Roll number already exists."

        conn.close()

        return redirect(url_for("index"))

    return render_template("add_student.html")


@app.route("/attendance", methods=("GET", "POST"))
def attendance():
    conn = get_db_connection()

    students = conn.execute(
        "SELECT * FROM students ORDER BY roll_number"
    ).fetchall()

    if request.method == "POST":
        attendance_date = request.form["attendance_date"]

        for student in students:
            status = request.form.get(f"status_{student['id']}")

            if status:
                conn.execute(
                    """
                    INSERT INTO attendance
                    (student_id, attendance_date, status)
                    VALUES (?, ?, ?)
                    """,
                    (student["id"], attendance_date, status)
                )

        conn.commit()
        conn.close()

        return redirect(url_for("report"))

    conn.close()

    return render_template(
        "attendance.html",
        students=students,
        today=date.today().isoformat()
    )


@app.route("/report")
def report():
    conn = get_db_connection()

    students = conn.execute(
        "SELECT * FROM students ORDER BY roll_number"
    ).fetchall()

    reports = []

    for student in students:
        total = conn.execute(
            """
            SELECT COUNT(*) AS count
            FROM attendance
            WHERE student_id = ?
            """,
            (student["id"],)
        ).fetchone()["count"]

        present = conn.execute(
            """
            SELECT COUNT(*) AS count
            FROM attendance
            WHERE student_id = ? AND status = 'Present'
            """,
            (student["id"],)
        ).fetchone()["count"]

        percentage = (present / total * 100) if total > 0 else 0

        reports.append({
            "name": student["name"],
            "roll_number": student["roll_number"],
            "course": student["course"],
            "total": total,
            "present": present,
            "absent": total - present,
            "percentage": round(percentage, 2)
        })

    conn.close()
