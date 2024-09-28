# app.py
import streamlit as st

with open( "static/style.css") as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

homeIcon, home, budgetIcon, budget, quizIcon, quiz, tutorialIcon, tutorial = st.columns(8, vertical_alignment="top", gap="small")

st.image("budget_bg.png", )
home.page_link("app.py", label="Home")
homeIcon.image("home.png")

budget.page_link("pages/budget-dashboard.py", label="Budgeting")
budgetIcon.image("coin.png")

quiz.page_link("pages/quizzes.py", label="Quiz Me")
quizIcon.image("showdown.png")

tutorial.page_link("pages/tutorial.py", label="Tutorial")
tutorialIcon.image("tutorial.png")


st.title("Treasure Keeper")
st.write("We help first-generation students with financial issues. Make this a paragraph long.")

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

st.html("""<button>Stone and Steel</button>""")
st.image("budget_vault_bg.png")
