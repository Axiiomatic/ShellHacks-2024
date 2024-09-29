# app.py
import streamlit as st

with open( "static/style.css") as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

def keep(key):
    #print(f"Copying underscore {key} to final: {st.session_state['_' + key]}")
    # Copy from temporary widget key to permanent key
    st.session_state[key] = st.session_state['_'+key]

def unkeep(key):
    #print(f"Copying final {key} to underscore: {st.session_state[key]}")
    # Copy from permanent key to temporary widget key
    st.session_state['_'+key] = st.session_state[key]

user_data_dict =  {
    "name" : "",
    "pronouns": "",
    "ethnicity": "Latin American",
    "work_status": "N/A",
    "income": 0,
    "job_title": "",
    "resident_status": "International Student",
    "student_status": "Full-time Student",
}

for data, default_value in user_data_dict.items():
    if data not in st.session_state:
        st.session_state[data] = default_value

homeIcon, home, budgetIcon, budget, quizIcon, quiz, tutorialIcon, tutorial = st.columns(8, vertical_alignment="top", gap="small")

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''
home.page_link("app.py", label="Home")
home.markdown(hide_img_fs, unsafe_allow_html=True)
homeIcon.image("home.png")

budget.page_link("pages/budget-dashboard.py", label="Budgeting")
budgetIcon.image("coin.png")

quiz.page_link("pages/quizzes.py", label="Quiz Me")
quizIcon.image("showdown.png")

tutorial.page_link("pages/tutorial.py", label="Tutorial")
tutorialIcon.image("tutorial.png")


st.title("Treasure Keeper")
st.write("We help first-generation students with financial issues through interactive challenges and questionares. . Make this a paragraph long. ")

def login():
    st.session_state.logged_in = True

if 'logged_in' not in st.session_state.keys():
    st.button("Log in", on_click=login)
    st.session_state.coins = 0

if 'logged_in' in st.session_state.keys() and st.session_state.logged_in:
    unkeep("name")
    st.text_input("Name: ", key="_name", on_change=keep, args=['name'])
    unkeep("pronouns")
    st.text_input("Pronouns: ", key="_pronouns", on_change=keep, args=['pronouns'])
    unkeep("ethnicity")
    st.selectbox("Ethnicity: ", (
        "Latin American",
        "African American",
        "Middle Eastern",
        "Pacific Islander",
        "White",
        "Prefer Not To Say",
    ), key="_ethnicity", on_change=keep, args=["ethnicity"])
    unkeep("work_status")
    st.selectbox("Working Status: ", ("N/A", "Full-Time Employed", "Part-Time Employed"),
                 key="_work_status", on_change=keep, args=["work_status"])

    if "work_status" in st.session_state.keys() and st.session_state.work_status != "N/A":
        unkeep("income")
        st.number_input("Last Year's Income: ", key="_income", on_change=keep, args=["income"])
        unkeep("job_title")
        st.text_input("Job Title: ", key="_job_title", on_change=keep, args=["job_title"])


    unkeep("resident_status")
    st.selectbox(
        "Residency Status: ",
        ("International Student", "In-State Resident Student", "Out-of-State Resident Student"),
        key="_resident_status", on_change=keep, args=["resident_status"]
    )

    unkeep("student_status")
    st.selectbox(
        "Student Status: ",
        ("Full-time Student", "Part-time Student"),
        key="_student_status", on_change=keep, args=["student_status"]
    )

st.audio("menu.mp3", format="audio/mpeg", loop=True, autoplay=True)