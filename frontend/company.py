import streamlit as st
import requests

API_URL = "http://127.0.0.1:8001"


def show():
    st.header("Company Portal")

    # Session setup
    if "company_logged_in" not in st.session_state:
        st.session_state["company_logged_in"] = False

    # Always define token
    token = st.session_state.get("token", None)

    headers = {}
    if token:
        headers = {
            "Authorization": f"Bearer {token}"
        }

    # Menu
    if st.session_state["company_logged_in"]:
        option = st.selectbox(
            "Choose",
            ["Create Job"]
        )
    else:
        option = st.selectbox(
            "Choose",
            ["Register", "Login"]
        )

    # Register
    if option == "Register":
        company_name = st.text_input("Company Name")
        hr_email = st.text_input("HR Email")
        password = st.text_input("Password", type="password")

        if st.button("Register"):
            res = requests.post(
                f"{API_URL}/companies/register",
                json={
                    "company_name": company_name,
                    "hr_email": hr_email,
                    "password": password
                }
            )
            st.json(res.json())

    # Login
    elif option == "Login":
        hr_email = st.text_input("HR Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            res = requests.post(
                f"{API_URL}/companies/login",
                json={
                    "hr_email": hr_email,
                    "password": password
                }
            )

            data = res.json()

            if "token" in data:
                st.session_state["token"] = data["token"]
                st.session_state["role"] = "company"
                st.session_state["company_logged_in"] = True
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    # Create Job
    elif option == "Create Job":
        title = st.text_input("Job Title")
        description = st.text_area("Description")
        min_cgpa = st.number_input("Minimum CGPA")
        branch = st.text_input("Branch")
        salary = st.number_input("Salary")

        if st.button("Create Job"):
            res = requests.post(
                f"{API_URL}/jobs",
                json={
                    "title": title,
                    "description": description,
                    "min_cgpa": min_cgpa,
                    "branch": branch,
                    "salary": salary
                },
                headers=headers
            )

            st.json(res.json())

    # Logout
    # Sidebar logout
    if st.session_state["company_logged_in"]:
        if st.sidebar.button("Logout"):
            st.session_state.clear()
            st.success("Logged out successfully")
            st.rerun()


