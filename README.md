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
##**Navigating trough the website**
<img width="1300" height="1150" alt="Web1" src="https://github.com/user-attachments/assets/519edc47-4882-4ff9-af1f-e676a8111cc0" />
<img width="1300" height="1150" alt="Web2" src="https://github.com/user-attachments/assets/99fc72f9-0b7b-42a4-b2c6-5df847da2395" />
<img width="1300" height="1150" alt="Web3" src="https://github.com/user-attachments/assets/f40f206d-d4be-4819-af74-118178104d16" />
<img width="1300" height="1150" alt="Web4" src="https://github.com/user-attachments/assets/8ae6288d-39de-4c89-9871-4362be632207" />

---
##**Navigating through API, Grades, GPA**

- **View Course API Data:** 127.0.0.1:8000/api/courses/

- **View Live Course Grades:** 127.0.0.1:8000/api/courses/1/grades/

- **View Student calculated GPA:** 127.0.0.1:8000/api/students/1/gpa/ 

- **View Student Attendances:** 127.0.0.1:8000/api/attendance/1/

*(The 1 in this case works like the student's IP)*

---
## **Guide and explanation of structure**
<img width="1300" height="1150" alt="1 1" src="https://github.com/user-attachments/assets/fe47a445-6c86-4649-80ca-f6696a23c656" />
<img width="1300" height="1150" alt="1 2" src="https://github.com/user-attachments/assets/7230fb12-30cd-4e1c-af2e-7305e529650e" />
<img width="1300" height="1150" alt="1 3" src="https://github.com/user-attachments/assets/575e28e6-7257-4459-98dd-c15d45f75883" />
<img width="1300" height="1150" alt="1 4" src="https://github.com/user-attachments/assets/f1c43817-1eca-4d3a-af88-9b65b2b12df7" />

---
## **admin.py Code breakdown and explanation**
<img width="1300" height="1150" alt="Admin py" src="https://github.com/user-attachments/assets/36cd8f06-e407-4c03-ab55-99e7b79d6dd7" />

---
## **forms.py Code breakdown and explanation**
<img width="1300" height="1150" alt="Forms py" src="https://github.com/user-attachments/assets/b6bd0e74-a376-4817-a347-671a77dc94a1" />

---
## **models.py Code breakdown and explanation**
<img width="1300" height="1150" alt="Models py" src="https://github.com/user-attachments/assets/ded7b06b-87be-44e1-b6b8-6b13d7a0616e" />

---
## **urls.py Code breakdown and explanation**
<img width="1300" height="1150" alt="Urls py" src="https://github.com/user-attachments/assets/ef0a19b7-a8f3-4827-ba9f-9e321ac0f98b" />

---
## **views.py Code breakdown and explanation**
<img width="1300" height="1150" alt="Views py" src="https://github.com/user-attachments/assets/279118cc-4509-4d30-9e30-ed0dd1dd3d84" />













