<<<<<<< HEAD
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8001"

def show():
    st.header("Company Portal")

    option = st.selectbox(
        "Choose",
        ["Register", "Login", "Create Job"]
    )

    if option == "Register":
        company_name = st.text_input("Company Name", key="company_name")
        hr_email = st.text_input("HR Email", key="company_email")
        password = st.text_input("Password", type="password", key="company_password")

        if st.button("Register"):
            data = {
                "company_name": company_name,
                "hr_email": hr_email,
                "password": password
            }

            res = requests.post(
                f"{API_URL}/companies/register",
                json=data
            )

            st.json(res.json())

    elif option == "Login":
        hr_email = st.text_input("HR Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):
            res = requests.post(
                f"{API_URL}/companies/login",
                json={
                    "hr_email": hr_email,
                    "password": password
                }
            )

            st.json(res.json())

    elif option == "Create Job":
        title = st.text_input("Job Title", key="job_title")
        description = st.text_area("Description", key="job_desc")
        min_cgpa = st.number_input("Minimum CGPA")
        branch = st.text_input("Branch", key="job_branch")
        salary = st.number_input("Salary")

        if st.button("Create Job"):
            data = {
                "title": title,
                "description": description,
                "min_cgpa": min_cgpa,
                "branch": branch,
                "salary": salary
            }

            res = requests.post(
                f"{API_URL}/jobs",
                json=data
            )

=======
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8001"

def show():
    st.header("Company Portal")

    option = st.selectbox(
        "Choose",
        ["Register", "Login", "Create Job"]
    )

    if option == "Register":
        company_name = st.text_input("Company Name", key="company_name")
        hr_email = st.text_input("HR Email", key="company_email")
        password = st.text_input("Password", type="password", key="company_password")

        if st.button("Register"):
            data = {
                "company_name": company_name,
                "hr_email": hr_email,
                "password": password
            }

            res = requests.post(
                f"{API_URL}/companies/register",
                json=data
            )

            st.json(res.json())

    elif option == "Login":
        hr_email = st.text_input("HR Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):
            res = requests.post(
                f"{API_URL}/companies/login",
                json={
                    "hr_email": hr_email,
                    "password": password
                }
            )

            st.json(res.json())

    elif option == "Create Job":
        title = st.text_input("Job Title", key="job_title")
        description = st.text_area("Description", key="job_desc")
        min_cgpa = st.number_input("Minimum CGPA")
        branch = st.text_input("Branch", key="job_branch")
        salary = st.number_input("Salary")

        if st.button("Create Job"):
            data = {
                "title": title,
                "description": description,
                "min_cgpa": min_cgpa,
                "branch": branch,
                "salary": salary
            }

            res = requests.post(
                f"{API_URL}/jobs",
                json=data
            )

>>>>>>> 9ae8fc84428353b2bcc0126879f357f56f165a61
            st.json(res.json())