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

---
## **permissions.py Code breakdown and explanation**
<img width="1300" height="1150" alt="Permission py" src="https://github.com/user-attachments/assets/618beb1d-645b-4c69-9043-9db3fe2a0652" />

---
## **serializers.py Code breakdown and explanation**
<img width="1300" height="1150" alt="Serializers py" src="https://github.com/user-attachments/assets/b68a5648-661f-458a-8436-6295b49761f0" />

---
## **views.py Code breakdown and explanation**
<img width="1300" height="1150" alt="views2 py" src="https://github.com/user-attachments/assets/837f1915-0c85-47cc-9338-0464e2771e87" />

---
## **grade_service.py Code breakdown and explanation**
<img width="1300" height="1150" alt="Grade_Service py1" src="https://github.com/user-attachments/assets/a50b8e85-695f-49b5-add4-c946fdd6749c" />
<img width="1300" height="1150" alt="Grade_Service py2" src="https://github.com/user-attachments/assets/53dcb9d2-21bd-4578-9ab0-c002c512d5c6" />
<img width="1300" height="1150" alt="Grade_Service py3" src="https://github.com/user-attachments/assets/c4e0213e-c1a6-495f-96bf-7d3896b185f4" />

---
## **Core_filters.py Code breakdown and explanation**
<img width="1300" height="1150" alt="Core_filters py" src="https://github.com/user-attachments/assets/82be6e42-14e5-491b-ab04-d243f8f93ce5" />

---
## **admin.py Code breakdown and explanation**
<img width="1300" height="1150" alt="admin2 py" src="https://github.com/user-attachments/assets/1c67e310-9c71-4e4e-bd9a-1320ad474c93" />

---
## **managers.py Code breakdown and explanation**
<img width="1300" height="1150" alt="managers py" src="https://github.com/user-attachments/assets/69cd0434-d51e-4f59-bee1-bd8583151b07" />

---
## **models.py Code breakdown and explanation**
<img width="1300" height="1150" alt="models2 py1" src="https://github.com/user-attachments/assets/174d43f8-03d2-459c-878c-921202e81f36" />
<img width="1300" height="1150" alt="models2 py2" src="https://github.com/user-attachments/assets/d69fdeb9-e7d1-4160-8e5e-3e78b3715a22" />

---
## **views.py Code breakdown and explanation**
<img width="1300" height="1150" alt="views2 py1" src="https://github.com/user-attachments/assets/21662961-2eeb-4300-82d9-4f447abc8ef2" />
<img width="1300" height="1150" alt="views2 py2" src="https://github.com/user-attachments/assets/69e7f780-d4a0-4883-830c-34df310a026a" />

---
## **base.py Code breakdown and explanation**
<img width="1300" height="1150" alt="base py1" src="https://github.com/user-attachments/assets/4f68525d-85e1-4bda-a27e-110f17ab9d2b" />
<img width="1300" height="1150" alt="base py2" src="https://github.com/user-attachments/assets/ef3aa879-65a9-4c2d-b6f5-b9f61d92771b" />
<img width="1300" height="1150" alt="base py3" src="https://github.com/user-attachments/assets/a0693598-3fde-4b6a-b8aa-9ebda91d9192" />

---
## **test_academic_core.py Code breakdown and explanation**
<img width="1300" height="1150" alt="test_academic_core py1" src="https://github.com/user-attachments/assets/c7143ed2-e0c0-4566-83d8-a81a39437fab" />
<img width="1300" height="1150" alt="test_academic_core py2" src="https://github.com/user-attachments/assets/26742402-374a-4dd8-93f2-5dc7723888b5" />



---
<!-- THIS WAS THE PROJECT I DID:

## Project 4 — Student Grade Management

### Features
Admin/Teacher/Student roles · Course and enrollment management · Grade CRUD (exam/quiz/homework/project) · GPA formula · Attendance tracker · Import quiz bank from Trivia API · Semester filter · Transcript CSV · Permission isolation (teacher ↔ own courses, student ↔ own grades)

### Database Models
```
User(AbstractUser): role, full_name
Course: teacher(FK), name, code, credits, semester, year
Enrollment: student(FK), course(FK), enrolled_at
Grade: enrollment(FK), assignment_name, type, score, max_score, graded_at
Attendance: enrollment(FK), date, status
```

### REST Endpoints
`GET /api/courses/` · `GET /api/courses/<id>/grades/` · `POST /api/grades/` · `GET /api/students/<id>/gpa/` · `GET /api/attendance/<enrollment>/`

### External API
Open Trivia DB — `https://opentdb.com/api.php?amount=10&category=X&difficulty=Y`

### Signature: Schedule Conflict Detector
Course enrollment interval-overlap algorithm.
**Variant (seed%2):** `0` = strict; `1` = a 15-minute buffer is allowed. -->




















