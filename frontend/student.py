<<<<<<< HEAD
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8001"


def show():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    st.header("Student Portal")

    if st.session_state["logged_in"]:
        option = st.selectbox(
            "Choose",
            ["View Jobs", "Apply Job", "My Applications", "Logout"]
        )
    else:
        option = st.selectbox(
            "Choose",
            ["Register", "Login"],
            key="student_option"
        )

    # Register
    if option == "Register":
        name = st.text_input("Name", key="reg_name")
        email = st.text_input("Email", key="reg_email")
        password = st.text_input("Password", type="password", key="reg_password")
        cgpa = st.number_input("CGPA", key="reg_cgpa")
        branch = st.text_input("Branch", key="reg_branch")
        year = st.number_input("Graduation Year", key="reg_year")

        if st.button("Register", key="reg_btn"):
            data = {
                "name": name,
                "email": email,
                "password": password,
                "cgpa": cgpa,
                "branch": branch,
                "graduation_year": year
            }

            res = requests.post(
                f"{API_URL}/students/register",
                json=data
            )

            st.json(res.json())

    # Login
    elif option == "Login":
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

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

    # Logout
    elif option == "Logout":
        st.session_state.clear()
        st.success("Logged out")
        st.rerun()
=======
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8001"


def show():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    st.header("Student Portal")

    if st.session_state["logged_in"]:
        option = st.selectbox(
            "Choose",
            ["View Jobs", "Apply Job", "My Applications", "Logout"]
        )
    else:
        option = st.selectbox(
            "Choose",
            ["Register", "Login"],
            key="student_option"
        )

    # Register
    if option == "Register":
        name = st.text_input("Name", key="reg_name")
        email = st.text_input("Email", key="reg_email")
        password = st.text_input("Password", type="password", key="reg_password")
        cgpa = st.number_input("CGPA", key="reg_cgpa")
        branch = st.text_input("Branch", key="reg_branch")
        year = st.number_input("Graduation Year", key="reg_year")

        if st.button("Register", key="reg_btn"):
            data = {
                "name": name,
                "email": email,
                "password": password,
                "cgpa": cgpa,
                "branch": branch,
                "graduation_year": year
            }

            res = requests.post(
                f"{API_URL}/students/register",
                json=data
            )

            st.json(res.json())

    # Login
    elif option == "Login":
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

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

    # Logout
    elif option == "Logout":
        st.session_state.clear()
        st.success("Logged out")
        st.rerun()
>>>>>>> 9ae8fc84428353b2bcc0126879f357f56f165a61
