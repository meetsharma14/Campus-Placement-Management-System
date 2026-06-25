import streamlit as st
import requests

API_URL = "http://127.0.0.1:8001"

def show():
    st.header("Admin Panel")

    if st.button("View Students", key="view_students"):
        res = requests.get(f"{API_URL}/admin/students")
        st.json(res.json())

    if st.button("View Companies", key="view_companies"):
        res = requests.get(f"{API_URL}/admin/companies")
        st.json(res.json())
        
    company_id = st.text_input("Company ID")

    if st.button("Approve Company"):
        res = requests.put(
            f"{API_URL}/admin/companies/{company_id}/approve"
        )
        st.json(res.json())
