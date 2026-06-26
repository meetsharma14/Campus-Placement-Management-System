import streamlit as st
import student
import company
import admin

st.set_page_config(page_title="Campus Placement System")

st.title("Campus Placement Management System")

menu = ["Student", "Company", "Admin"]
choice = st.sidebar.selectbox("Select Role", menu)

if choice == "Student":
    student.show()

elif choice == "Company":
    company.show()

elif choice == "Admin":
    admin.show()