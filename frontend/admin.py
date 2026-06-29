import streamlit as st
import requests

API_URL = "http://127.0.0.1:8001"


def show():
    st.header("Admin Panel")

    # Check if admin logged in
    if "token" not in st.session_state:
        st.subheader("Admin Login")

        email = st.text_input("Admin Email")
        password = st.text_input("Password", type="password")

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

    # If logged in
    token = st.session_state.get("token")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    st.success("Logged in as Admin")

    # View Students
    if st.button("View Students"):
        res = requests.get(
            f"{API_URL}/admin/students",
            headers=headers
        )
        st.json(res.json())

    # View Companies
    if st.button("View Companies"):
        res = requests.get(
            f"{API_URL}/admin/companies",
            headers=headers
        )
        st.json(res.json())

    # Approve Company
    company_id = st.text_input("Company ID")

    if st.button("Approve Company"):
        if company_id:
            res = requests.put(
                f"{API_URL}/admin/companies/{company_id}/approve",
                headers=headers
            )
            st.json(res.json())
        else:
            st.error("Enter Company ID")
    # delete company
    company_id_delete = st.text_input(
        "Company ID to Delete",
        key="delete_company_id"
        )

    if st.button("Delete Company"):
        res = requests.delete(
            f"{API_URL}/admin/companies/{company_id_delete}",
            headers=headers
        )
        st.json(res.json())

    # Logout
    if st.button("Logout"):
        del st.session_state["token"]
        st.success("Logged out")
        st.rerun()
