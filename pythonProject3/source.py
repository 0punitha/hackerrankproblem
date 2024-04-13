import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Create SQLite database and table
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        roll_number TEXT NOT NULL UNIQUE
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students (id)
    )
''')
conn.commit()

# Tkinter GUI
class AttendanceApp:
    def _init_(self, root):
        self.root = root
        self.root.title("College Attendance Entry")

        self.label_name = tk.Label(root, text="Student Name:")
        self.label_name.pack()

        self.entry_name = tk.Entry(root)
        self.entry_name.pack()

        self.label_roll_number = tk.Label(root, text="Roll Number:")
        self.label_roll_number.pack()

        self.entry_roll_number = tk.Entry(root)
        self.entry_roll_number.pack()

        self.button_mark_attendance = tk.Button(root, text="Mark Attendance", command=self.mark_attendance)
        self.button_mark_attendance.pack()

    def mark_attendance(self):
        name = self.entry_name.get()
        roll_number = self.entry_roll_number.get()

        if not name or not roll_number:
            messagebox.showerror("Error", "Please enter both name and roll number.")
            return

        # Check if the student exists in the database
        cursor.execute('SELECT id FROM students WHERE roll_number = ?', (roll_number,))
        student_id = cursor.fetchone()

        if not student_id:
            messagebox.showerror("Error", "Student not found. Please check the roll number.")
            return

        # Mark attendance for the student
        today_date = datetime.now().strftime("%Y-%m-%d")
        cursor.execute('INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)',
                       (student_id[0], today_date, 'Present'))
        conn.commit()

        messagebox.showinfo("Success", f"Attendance marked for {name} (Roll Number: {roll_number}).")


if _name_ == "_main_":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()

# Close the database connection when the application is closed
conn.close()