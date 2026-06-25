import streamlit as st
import requests

API_URL = "http://127.0.0.1:8001"

def show():
    st.header("Student Portal")

    option = st.selectbox(
        "Choose",
        ["Register", "Login", "View Jobs"],
        key="student_option"
    )

    if option == "Register":
        name = st.text_input("Name", key="reg_name")
        email = st.text_input("Email", key="reg_email")
        password = st.text_input(
            "Password",
            type="password",
            key="reg_password"
        )
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
                st.success("Login successful")
            else:
                st.error("Invalid credentials")
            
            
            

    elif option == "View Jobs":
        res = requests.get(f"{API_URL}/jobs")
        st.json(res.json())