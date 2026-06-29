import streamlit as st
import requests
from jose import jwt

API_URL = "http://127.0.0.1:8001"
SECRET_KEY = "mysecretkey"


def get_student_id(token):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )
        return payload["id"]
    except:
        return None


def show():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    token = st.session_state.get("token", None)

    headers = {}
    if token:
        headers = {
            "Authorization": f"Bearer {token}"
        }

    st.header("Student Portal")

    if st.session_state["logged_in"]:
        option = st.selectbox(
            "Choose",
            ["View Jobs", "Apply Job", "My Applications"]
        )
    else:
        option = st.selectbox(
            "Choose",
            ["Register", "Login"]
        )

    # Register
    if option == "Register":
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        cgpa = st.number_input("CGPA")
        branch = st.text_input("Branch")
        year = st.number_input("Graduation Year")
        resume = st.file_uploader(
            "Upload Resume (PDF)",
            type=["pdf"]
        )
        if st.button("Register"):
            res = requests.post(
                f"{API_URL}/students/register",
                json={
                    "name": name,
                    "email": email,
                    "password": password,
                    "cgpa": cgpa,
                    "branch": branch,
                    "graduation_year": year
                }
            )
            st.json(res.json())

    # Login
    elif option == "Login":
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            res = requests.post(
                f"{API_URL}/students/login",
                json={
                    "email": email,
                    "password": password
                }
            )

            data = res.json()

            if "token" in data:
                st.session_state["token"] = data["token"]
                st.session_state["logged_in"] = True
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    # View Jobs
    elif option == "View Jobs":
        res = requests.get(f"{API_URL}/jobs")
        st.json(res.json())

    # Apply Job
    elif option == "Apply Job":
        res = requests.get(f"{API_URL}/jobs")
        jobs = res.json()

        if jobs:
            job_options = {
                f"{job['title']} - {job['branch']}": job["id"]
                for job in jobs
            }

            selected_job = st.selectbox(
                "Select Job",
                list(job_options.keys())
            )

            job_id = job_options[selected_job]

            if st.button("Apply"):
                apply_res = requests.post(
                    f"{API_URL}/jobs/{job_id}/apply",
                    headers=headers
                )
                st.json(apply_res.json())
        else:
            st.warning("No jobs available")

    # My Applications
    elif option == "My Applications":
        student_id = get_student_id(token)
        if student_id:
            res = requests.get(
                f"{API_URL}/students/{student_id}/applications",
                headers=headers
            )

            st.json(res.json())
        else:
            st.error("Invalid token")

    # Logout
    # Sidebar logout
    if st.session_state["logged_in"]:
        if st.sidebar.button("Logout"):
            st.session_state.clear()
            st.success("Logged out successfully")
            st.rerun()

