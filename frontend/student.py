import streamlit as st
import requests
from jose import jwt

API_URL = "https://campus-placement-management-system-ui9r.onrender.com"
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
    # Session setup
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    token = st.session_state.get("token")

    headers = {}
    if token:
        headers = {
            "Authorization": f"Bearer {token}"
        }

    st.header("Student Portal")

    # Sidebar logout
    if st.session_state["logged_in"]:
        if st.sidebar.button(
            "Logout",
            key="student_logout"
        ):
            st.session_state.clear()
            st.success("Logged out successfully")
            st.rerun()

    # Menu
    if st.session_state["logged_in"]:
        option = st.selectbox(
            "Choose",
            [
                "Complete Profile",
                "View Jobs",
                "My Applications"
            ]
        )
    else:
        option = st.selectbox(
            "Choose",
            [
                "Register",
                "Login"
            ]
        )

    # =========================
    # Register
    # =========================
    if option == "Register":
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Register"):
            res = requests.post(
                f"{API_URL}/students/register",
                json={
                    "name": name,
                    "email": email,
                    "password": password
                }
            )

            if res.status_code == 200:
                st.success("Registration successful")
                st.json(res.json())
            else:
                st.error("Registration failed")
                st.write(res.text)

    # =========================
    # Login
    # =========================
    elif option == "Login":
        email = st.text_input("Email")
        password = st.text_input(
            "Password",
            type="password"
        )

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

    # =========================
    # Complete Profile
    # =========================
    elif option == "Complete Profile":
        cgpa = st.number_input("CGPA")
        branch = st.text_input("Branch")
        year = st.number_input("Graduation Year")
        resume = st.file_uploader(
            "Upload Resume (PDF)",
            type=["pdf"]
        )

        if st.button("Save Profile"):
            profile_res = requests.put(
                f"{API_URL}/students/profile",
                json={
                    "cgpa": cgpa,
                    "branch": branch,
                    "graduation_year": year
                },
                headers=headers
            )

            if profile_res.status_code == 200:
                st.success("Profile updated")

                if resume:
                    files = {
                        "file": (
                            resume.name,
                            resume,
                            "application/pdf"
                        )
                    }

                    upload_res = requests.post(
                        f"{API_URL}/resume/upload",
                        files=files,
                        headers=headers
                    )

                    st.json(upload_res.json())
            else:
                st.error(profile_res.text)

    # =========================
    # View Jobs
    # =========================
    elif option == "View Jobs":
        res = requests.get(
            f"{API_URL}/jobs"
        )

        jobs = res.json()

        if jobs:
            for job in jobs:
                st.subheader(job["title"])
                st.write(
                    f"🏢 Company: {job['company_name']}"
                )
                st.write(
                    f"🎓 Branch: {job['branch']}"
                )
                st.write(
                    f"📊 Minimum CGPA: {job['min_cgpa']}"
                )
                st.write(
                    f"💰 Salary: {job['salary']} LPA"
                )

                st.info(job["description"])

                if st.button(
                    f"Apply for {job['title']}",
                    key=job["id"]
                ):
                    apply_res = requests.post(
                        f"{API_URL}/jobs/{job['id']}/apply",
                        headers=headers
                    )

                    response_data = apply_res.json()

                    if "message" in response_data:
                        st.success(
                            response_data["message"]
                        )
                    elif "error" in response_data:
                        st.error(
                            response_data["error"]
                        )
                    elif "detail" in response_data:
                        st.error(
                            response_data["detail"]
                        )

                st.divider()
        else:
            st.warning("No jobs available")

    # =========================
    # My Applications
    # =========================
    elif option == "My Applications":
        student_id = get_student_id(token)

        if student_id:
            res = requests.get(
                f"{API_URL}/students/{student_id}/applications",
                headers=headers
            )

            if res.status_code == 200:
                applications = res.json()

                if applications:
                    for app in applications:
                        st.subheader(
                            app["job_title"]
                        )
                        st.write(
                            f"Company: {app['company_name']}"
                        )
                        st.write(
                            f"Status: {app['status']}"
                        )

                        if app["status"] == "Applied":
                            st.info(
                                "Pending review"
                            )

                        st.divider()
                else:
                    st.warning(
                        "No applications found"
                    )
            else:
                st.error(res.text)
        else:
            st.error("Invalid token")

