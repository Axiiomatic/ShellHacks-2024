# app.py
import streamlit as st

with open( "static/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

home, budget, quiz, tutorial = st.columns(4, vertical_alignment="top", gap="medium")
with home:
    st.page_link("app.py", label="Home", icon="🏠")

with budget:
    st.page_link("pages/budget-dashboard.py", label="Budgeting", icon="🧾")

with quiz:
    st.page_link("pages/quizzes.py", label="Quiz Me", icon="✏")

with tutorial:
    st.page_link("pages/tutorial.py", label="Tutorial")


st.title("Treasure Keeper")
st.write("We help first-generation students with financial issues. Make this a paragraph long.")

st.button("Stone and Steel")

def login():
    st.session_state.logged_in = True

if 'logged_in' not in st.session_state.keys():
    st.button("Log in", on_click=login)

if 'logged_in' in st.session_state.keys() and st.session_state.logged_in:
    st.text_input("Name: ", key="name")
    st.text_input("Pronouns: ", key="pronouns")
    st.selectbox("Ethnicity: ", (
        "Latin American",
        "African American",
        "Middle Eastern",
        "Pacific Islander",
        "White",
        "Prefer Not To Say",
    ), key="ethnicity")
    st.selectbox("Working Status: ", ("N/A", "Full-Time Employed", "Part-Time Employed"), key="work_status")

    if "work_status" in st.session_state.keys() and st.session_state.work_status != "N/A":
        st.number_input("Last Year's Income: ", key="income")
        st.text_input("Job Title: ", key="job_title")

    st.selectbox(
        "Residency Status: ",
        ("International Student", "In-State Resident Student", "Out-of-State Resident Student"),
        key="resident_status"
    )
    st.selectbox(
        "Student Status: ",
        ("Full-time Student", "Part-time Student"),
        key="student_status"
    )
