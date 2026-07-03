import sqlite3


def AddClasses(user):
    if user["role"] != "teacher" and user["role"] != "admin":
        print("You do not have permission to add classes.")
        return
    print("Add classes page")
    print("Adding a class to the database.")

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    class_name = input("Enter the class name: ")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)
    cursor.execute("""
    INSERT INTO classes (name ) VALUES (?)
    """, (class_name,))

    conn.commit()
    conn.close()


def Grades(user):
    if user["role"] != "teacher" and user["role"] != "admin":
        print("You do not have permission to add grades.")
        return
    print("Add grades page")
    print("Adding a grade to the database.")

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    student_id = input("Enter the student ID: ")
    class_id = input("Enter the class ID: ")
    grade = input("Enter the grade: ")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            class_id INTEGER NOT NULL,
            grade TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (class_id) REFERENCES classes(id)
        )
        """)
    cursor.execute("""
        INSERT INTO grades (student_id, class_id, grade) VALUES (?, ?, ?)
        """, (student_id, class_id, grade))

    conn.commit()
    conn.close()


def SeeGrades(user):
   # if user["role"] != "student" and user["role"] != "admin":
    # print("You do not have permission to see grades.")
    # return
    print("See grades page")
    print("Fetching grades from the database.")

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    student_id = input("Enter the student ID: ")

    cursor.execute("""
        SELECT classes.name, grades.grade FROM grades
        JOIN classes ON grades.class_id = classes.id
        WHERE grades.student_id = ?
        """, (student_id,))

    results = cursor.fetchall()
    if results:
        for class_name, grade in results:
            print(f"Class: {class_name}, Grade: {grade}")
    else:
        print("No grades found for the specified student.")
