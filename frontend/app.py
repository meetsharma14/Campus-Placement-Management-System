<<<<<<< HEAD
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
=======
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
>>>>>>> 9ae8fc84428353b2bcc0126879f357f56f165a61
    admin.show()