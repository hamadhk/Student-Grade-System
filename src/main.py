import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
from tkinter import messagebox
import pandas as pd

# initialiazing dictionary
student_grades = {}

def modify_student(action):
    name = name_entry.get().strip()
    grade = grade_entry.get().strip()
    if name and grade.isdigit():
        grade = int(grade)
        if action == "add":
            student_grades[name] = grade
            messagebox.showinfo("Success", f"Added name:{name.upper()} with grade:{grade}")
        elif action == "update":
            if name in student_grades:
                student_grades[name] = grade
                messagebox.showinfo("Success", f"Updated name:{name.upper()} with grade:{grade}")
            else:
                messagebox.showerror("Error", "Student Not Found!")
        update_display()
    else:
        messagebox.showerror("Error", "Invalid Input! Please enter a valid input.")

def delete_student():
    name = name_entry.get().strip()
    if not name:
        messagebox.showerror("Error", "Please enter a valid input!")
        return
    if name in student_grades:
        del student_grades[name]
        messagebox.showinfo("Success", f"Deleted {name.upper()}")
        update_display()
    else:
        messagebox.showerror("Error", "Student Not Found")

def update_display():
    display_box.delete(0, tk.END)
    if student_grades:
        try:
            for name,grade in student_grades.items():
                display_box.insert(tk.END, f"{name} : {grade}")
        except:
            messagebox.showerror("Error", "An Error Occured")

def generate_excel_file():
    if not student_grades:
        messagebox.showerror("Error", "No student data to export!")
        return
    try:
        df = pd.DataFrame(list(student_grades.items()), columns=["Student Name", "Grade"])
        df.to_excel("students.xlsx", index=False)
        messagebox.showinfo("Success", "Student data has been saved to students.xlsx!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate an Excel file:\n{e}")

root = tk.Tk()
style = Style(theme="darkly")
root.title("Student Grade Portal")
root.geometry("800x600")

# creating ui elements
name_label = ttk.Label(root, text="Student Name :")
name_label.pack(pady=5)
name_entry = ttk.Entry(root)
name_entry.pack()

grade_label = ttk.Label(root, text="Student Grade :")
grade_label.pack(pady=5)
grade_entry = ttk.Entry(root)
grade_entry.pack()

add_button = ttk.Button(root, text="Add Student", command =lambda: modify_student("add"), bootstyle = "success-outlined", padding= 10, width=20)
add_button.pack(pady=10)

update_button = ttk.Button(root, text="Update Student", command =lambda: modify_student("update"), bootstyle = "success-outlined", padding= 10, width=20)
update_button.pack(pady=10)

delete_button = ttk.Button(root, text="Delete Student", command =delete_student, bootstyle = "success-outlined", padding= 10, width=20)
delete_button.pack(pady=10)

export_button = ttk.Button(root, text="Generate Excel File", command =generate_excel_file, bootstyle = "success-outlined", padding= 10, width=20)
export_button.pack(pady=10)

# display content
display_box = tk.Listbox(root, width=100, height=20)
display_box.pack(pady=10)

root.mainloop()