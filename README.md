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




