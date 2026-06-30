# Campus Placement Management System

A full-stack web application for managing campus placements built with **FastAPI**, **PostgreSQL**, and **Streamlit**.

## Features

### Student Portal

* Register / Login
* Complete Profile
* Upload Resume (PDF)
* View Available Jobs
* Apply for Jobs
* Track Application Status

### Company Portal

* Register / Login
* Create Jobs
* Manage Job Listings

### Admin Panel

* Admin Login
* View All Students
* View All Companies
* Approve Companies
* Delete Companies
* Delete Students
* Delete Jobs
* View Applications
* Update Application Status
* Dashboard Analytics

---

## Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT Authentication
* Passlib Argon2(Password Hashing)

### Frontend

* Streamlit

---

## Project Structure

```bash
Campus Placement Management System/
│── app/
│   │── main.py
│   │── database.py
│   │── models/
│   │── routes/
│   │── utils/
│
│── frontend/
│   │── app.py
│   │── student.py
│   │── company.py
│   │── admin.py
│
│── uploads/
│── requirements.txt
│── README.md
```

---

## Installation

### Clone repository

```bash
git clone https://github.com/your-username/campus-placement-management-system.git
cd campus-placement-management-system
```

---

## Backend Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn app.main:app --reload --port 8001
```

Backend URL:

```bash
https://campus-placement-management-system-ui9r.onrender.com
```

Swagger UI:

```bash
http://127.0.0.1:8001/docs 
```

---

## Frontend Setup

Go to frontend folder:

```bash
cd frontend
```

Run Streamlit:

```bash
streamlit run app.py
```

Frontend URL:

```bash
[http://localhost:8501](https://campus-placement-management-system-mvyk3pwn2rgcovf3mxcbxx.streamlit.app/)
```

---

## API Endpoints

### Student

* POST `/students/register`
* POST `/students/login`
* POST `/resume/upload`
* POST `/jobs/{job_id}/apply`
* GET `/students/{student_id}/applications`

### Company

* POST `/companies/register`
* POST `/companies/login`
* POST `/jobs`

### Admin

* POST `/admin/login`
* GET `/admin/students`
* GET `/admin/companies`
* PUT `/admin/companies/{company_id}/approve`
* DELETE `/admin/companies/{company_id}`
* DELETE `/admin/jobs/{job_id}`
* GET `/admin/applications`

---

## Authentication

JWT-based authentication is used for:

* Student
* Company
* Admin

Roles:

* student
* company
* admin

---

## Future Improvements

* Interview Scheduling
* Email Notifications
* Placement Analytics Graphs
* Resume Parsing
* AI-based Job Recommendations
* Company Shortlisting

---

## Author

Meet Sharma
B.Tech CSE Student
