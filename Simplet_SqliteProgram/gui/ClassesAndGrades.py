import sqlite3
import tkinter as tk
from tkinter import messagebox


# ----------------------------
# ADD CLASS
# ----------------------------
def AddClasses(user):
    if user["role"] not in ["teacher", "admin"]:
        messagebox.showerror("Permission Denied", "No access to add classes.")
        return

    window = tk.Toplevel()
    window.title("Add Class")
    window.geometry("300x200")

    tk.Label(window, text="Class Name").pack(pady=5)
    entry_class = tk.Entry(window)
    entry_class.pack(pady=5)

    def add():
        class_name = entry_class.get().strip()

        if not class_name:
            messagebox.showerror("Error", "Class name required")
            return

        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS classes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)

        cursor.execute(
            "INSERT INTO classes (name) VALUES (?)",
            (class_name,)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Class added!")
        window.destroy()

    tk.Button(window, text="Add Class", command=add).pack(pady=10)


# ----------------------------
# ADD GRADES
# ----------------------------
def Grades(user):
    if user["role"] not in ["teacher", "admin"]:
        messagebox.showerror("Permission Denied", "No access to add grades.")
        return

    window = tk.Toplevel()
    window.title("Add Grade")
    window.geometry("300x300")

    tk.Label(window, text="Student ID").pack()
    entry_student = tk.Entry(window)
    entry_student.pack()

    tk.Label(window, text="Class ID").pack()
    entry_class = tk.Entry(window)
    entry_class.pack()

    tk.Label(window, text="Grade").pack()
    entry_grade = tk.Entry(window)
    entry_grade.pack()

    def add_grade():
        student_id = entry_student.get().strip()
        class_id = entry_class.get().strip()
        grade = entry_grade.get().strip()

        if not student_id or not class_id or not grade:
            messagebox.showerror("Error", "All fields required")
            return

        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                class_id INTEGER NOT NULL,
                grade TEXT NOT NULL
            )
        """)

        cursor.execute("""
            INSERT INTO grades (student_id, class_id, grade)
            VALUES (?, ?, ?)
        """, (student_id, class_id, grade))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Grade added!")
        window.destroy()

    tk.Button(window, text="Save Grade", command=add_grade).pack(pady=10)


# ----------------------------
# SEE GRADES
# ----------------------------
def SeeGrades(user):
    window = tk.Toplevel()
    window.title("See Grades")
    window.geometry("400x300")

    tk.Label(window, text="Student ID").pack()
    entry_student = tk.Entry(window)
    entry_student.pack()

    result_box = tk.Text(window, height=10, width=40)
    result_box.pack(pady=10)

    def fetch():
        student_id = entry_student.get().strip()

        if not student_id:
            messagebox.showerror("Error", "Student ID required")
            return

        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT classes.name, grades.grade
            FROM grades
            JOIN classes ON grades.class_id = classes.id
            WHERE grades.student_id = ?
        """, (student_id,))

        results = cursor.fetchall()
        conn.close()

        result_box.delete("1.0", tk.END)

        if not results:
            result_box.insert(tk.END, "No grades found.\n")
            return

        for class_name, grade in results:
            result_box.insert(tk.END, f"{class_name}: {grade}\n")

    tk.Button(window, text="Get Grades", command=fetch).pack()
