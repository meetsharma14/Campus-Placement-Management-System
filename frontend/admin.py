import streamlit as st
import requests

API_URL = "http://127.0.0.1:8001"


def show():
    st.title("Admin Panel")

    # =========================
    # LOGIN
    # =========================
    if "token" not in st.session_state:
        st.subheader("Admin Login")

        email = st.text_input("Admin Email")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):
            res = requests.post(
                f"{API_URL}/admin/login",
                json={
                    "email": email,
                    "password": password
                }
            )

            data = res.json()

            if "token" in data:
                st.session_state["token"] = data["token"]
                st.success("Admin login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

        return

    token = st.session_state["token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    # =========================
    # SIDEBAR MENU
    # =========================
    menu = st.sidebar.radio(
        "Admin Menu",
        [
            "Dashboard",
            "Students",
            "Companies",
            "Jobs",
            "Applications",
            "Logout"
        ]
    )

    # =========================
    # DASHBOARD
    # =========================
    if menu == "Dashboard":
        st.subheader("System Analytics")

        res = requests.get(
            f"{API_URL}/admin/analytics",
            headers=headers
        )

        analytics = res.json()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Students",
            analytics["total_students"]
        )
        col2.metric(
            "Companies",
            analytics["total_companies"]
        )
        col3.metric(
            "Jobs",
            analytics["total_jobs"]
        )
        col4.metric(
            "Applications",
            analytics["total_applications"]
        )

    # =========================
    # STUDENTS
    # =========================
    elif menu == "Students":
        st.subheader("Manage Students")

        res = requests.get(
            f"{API_URL}/admin/students",
            headers=headers
        )

        students = res.json()

        for student in students:
            st.subheader(student["name"])
            st.write(f"Email: {student['email']}")
            st.write(f"Branch: {student.get('branch')}")
            st.write(f"CGPA: {student.get('cgpa')}")

            if st.button(
                "Delete Student",
                key=f"student_{student['id']}"
            ):
                delete_res = requests.delete(
                    f"{API_URL}/admin/students/{student['id']}",
                    headers=headers
                )
                response_data = delete_res.json()

                if "message" in response_data:
                    st.success(response_data["message"])
                elif "error" in response_data:
                    st.error(response_data["error"])
                elif "detail" in response_data:
                    st.error(response_data["detail"])
                else:
                    st.json(response_data)

                st.rerun()

            st.divider()

    # =========================
    # COMPANIES
    # =========================
    elif menu == "Companies":
        st.subheader("Manage Companies")

        res = requests.get(
            f"{API_URL}/admin/companies",
            headers=headers
        )

        companies = res.json()

        for company in companies:
            st.subheader(company["company_name"])
            st.write(f"HR Email: {company['hr_email']}")
            st.write(f"Approved: {company['approved']}")

            col1, col2 = st.columns(2)

            with col1:
                if st.button(
                    "Approve",
                    key=f"approve_{company['id']}"
                ):
                    approve_res = requests.put(
                        f"{API_URL}/admin/companies/{company['id']}/approve",
                        headers=headers
                    )
                    response_data = approve_res.json()

                    if "message" in response_data:
                        st.success(response_data["message"])
                    elif "error" in response_data:
                        st.error(response_data["error"])
                    elif "detail" in response_data:
                        st.error(response_data["detail"])
                    else:
                        st.json(response_data)

                    st.rerun()

            with col2:
                if st.button(
                    "Delete",
                    key=f"delete_{company['id']}"
                ):
                    delete_res = requests.delete(
                        f"{API_URL}/admin/companies/{company['id']}",
                        headers=headers
                    )
                    st.success(
                        delete_res.json()["message"]
                    )
                    st.rerun()

            st.divider()

    # =========================
    # JOBS
    # =========================
    elif menu == "Jobs":
        st.subheader("Manage Jobs")

        res = requests.get(
            f"{API_URL}/jobs"
        )

        jobs = res.json()

        for job in jobs:
            st.subheader(job["title"])
            st.write(f"Company: {job['company_name']}")
            st.write(f"Branch: {job['branch']}")
            st.write(f"Salary: {job['salary']} LPA")

            st.info(job["description"])

            if st.button(
                "Delete Job",
                key=f"job_{job['id']}"
            ):
                delete_res = requests.delete(
                    f"{API_URL}/admin/jobs/{job['id']}",
                    headers=headers
                )
                response_data = delete_res.json()

                if "message" in response_data:
                    st.success(response_data["message"])
                elif "error" in response_data:
                    st.error(response_data["error"])
                elif "detail" in response_data:
                    st.error(response_data["detail"])
                else:
                    st.json(response_data)

                st.rerun()

            st.divider()

    # =========================
    # APPLICATIONS
    # =========================
    elif menu == "Applications":
        st.subheader("Manage Applications")

        res = requests.get(
            f"{API_URL}/admin/applications",
            headers=headers
        )

        applications = res.json()

        for app in applications:
            st.subheader(app["job_title"])
            st.write(f"Student: {app['student_name']}")
            st.write(f"Company: {app['company_name']}")
            st.write(f"Current Status: {app['status']}")

            status = st.selectbox(
                "Update Status",
                [
                    "Applied",
                    "Shortlisted",
                    "Rejected",
                    "Selected"
                ],
                key=f"status_{app['id']}"
            )

            if st.button(
                "Save Status",
                key=f"save_{app['id']}"
            ):
                update_res = requests.put(
                    f"{API_URL}/admin/applications/{app['id']}?status={status}",
                    headers=headers
                )

                response_data = update_res.json()

                if "message" in response_data:
                    st.success(response_data["message"])
                elif "error" in response_data:
                    st.error(response_data["error"])
                elif "detail" in response_data:
                    st.error(response_data["detail"])
                else:
                    st.json(response_data)

                st.rerun()
                
            st.divider()

    # =========================
    # LOGOUT
    # =========================
    elif menu == "Logout":
        st.session_state.clear()
        st.success("Logged out")
        st.rerun()
