
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8001"

def show():
    st.header("Admin Panel")

    token = st.session_state.get("token")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    if st.button("View Students", key="view_students"):
        res = requests.get(
            f"{API_URL}/admin/students",
            headers=headers
        )
        st.json(res.json())

    if st.button("View Companies", key="view_companies"):
        res = requests.get(
            f"{API_URL}/admin/companies",
            headers=headers
        )
        st.json(res.json())

    company_id = st.text_input("Company ID", key="company_id")

    if st.button("Approve Company", key="approve_company"):
        res = requests.put(
            f"{API_URL}/admin/companies/{company_id}/approve",
            headers=headers
        )
        st.json(res.json())
