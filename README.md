Student Grade Management Platform

An academic cataloging, attendance, and student performance tracking portal built with Django 5.x and Django REST Framework.

Website: https://mamamiamaria2.pythonanywhere.com/

---

Key Features

**User Roles:** Separate access for Admin, Teacher, and Student accounts.

**Admin Panel:** Allows administrators and teachers to manage courses, enrollments, and grades.

**REST API:** Built with Django REST Framework to provide JSON API endpoints.

**Schedule Validation:** Prevents students from enrolling in courses with overlapping times.

**CSV Reports:** Generates downloadable student transcript reports in CSV format.

---

Database Models

**User (AbstractUser):** Custom user model with three roles: **Admin**, **Teacher**, and **Student** field.

**Course:** Stores course information, including schedule, meeting days, and assigned teacher.

**Enrollment:** Connects students to the courses they are enrolled in.

**Grade:** Stores student grades for exams, quizzes, homework, and projects.

**Attendance:** Records student attendance as Present, Absent, or Late.

---
###**Navigating trough the website**
<img width="1300" height="1150" alt="Web1" src="https://github.com/user-attachments/assets/519edc47-4882-4ff9-af1f-e676a8111cc0" />
<img width="1300" height="1150" alt="Web2" src="https://github.com/user-attachments/assets/99fc72f9-0b7b-42a4-b2c6-5df847da2395" />
<img width="1300" height="1150" alt="Web3" src="https://github.com/user-attachments/assets/f40f206d-d4be-4819-af74-118178104d16" />
<img width="1300" height="1150" alt="Web4" src="https://github.com/user-attachments/assets/8ae6288d-39de-4c89-9871-4362be632207" />







