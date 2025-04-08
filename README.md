# 🎓 Student Grade Portal

The **Student Grade Portal** is a user-friendly Python desktop application built with **Tkinter** and **ttkbootstrap** that helps you manage and track student grades. This GUI-based app allows you to add, update, and delete student records, display them in a list, and export the data to an Excel file with a single click.

---

## 📌 Features

✅ Add new student with grade  
✅ Update existing student’s grade  
✅ Delete student by name  
✅ Display all student records in a scrollable list  
✅ Export student data to Excel (`.xlsx`) format  
✅ Input validation and error messages  
✅ Modern dark-themed UI with `ttkbootstrap`

---
---

## 🔧 Tech Stack

- **Python 3.x**
- **Tkinter** – GUI library for creating the interface
- **ttkbootstrap** – Themed widgets for a modern look
- **pandas** – Used for exporting data to Excel
- **messagebox** – To display user alerts and confirmations

---

## 📦 Installation

> Make sure Python 3 is installed. We recommend using a virtual environment.

1. **Clone the repository**
```bash
git clone https://github.com/your-username/student-grade-portal.git
cd student-grade-portal
(Optional) Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

🚀 How to Run the App
python src/main.py

The application window will launch. You can start managing student data right away.

📤 Export Feature
Click on "Generate Excel File" and the current student list will be saved as students.xlsx in your project directory. You can open it with MS Excel or Google Sheets.

📋 Example Usage
Enter a student name and grade.

Click "Add Student".

View the student in the list.

Select the same name and a new grade, then click "Update Student".

To delete a student, enter just their name and click "Delete Student".

Click "Generate Excel File" to export data.

⚠️ Notes
Grade must be a number (e.g. 85).

Student name is case-sensitive when updating or deleting.

Deletion requires only the name.

The app overwrites students.xlsx each time it's generated.

🙋‍♂️ Author
Your Name
GitHub: @hammadhk

📃 License
This project is open-source and available under the MIT License.