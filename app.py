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
    "ethnicity": "",
    "work_status": "",
    "income": 0,
    "job_title": "",
    "resident_status": "",
    "student_status": "",
    "enrollment_status": ""
}

for data, default_value in user_data_dict.items():
    if data not in st.session_state:
        st.session_state[data] = default_value

home, budget, quiz, advising = st.columns(4, vertical_alignment="top", gap="small")

home.page_link("app.py", label="Home")


budget.page_link("pages/budget-dashboard.py", label="Budgeting")

quiz.page_link("pages/quizzes.py", label="Quiz Me")

advising.page_link("pages/advising.py", label="Advising")

st.title("Treasure Keeper")
st.write("Unlock your finances!\nWe help first-generation students and those with financial issues through interactive challenges and questionares. Ready to meet your new instructors and learn how to unlock all of your financial skills?. ")

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
        "",
        "American Indian or Alaska Native",
        "Asian",
        "Black or African American",
        "Hispanic or Latino",
        "Native Hawaiian or Other Pacific Islander",
        "White",
        "Prefer Not To Say"
    ), key="_ethnicity", on_change=keep, args=["ethnicity"])
    unkeep("work_status")
    st.selectbox("Working Status: ", ("", "N/A", "Full-Time Employed", "Part-Time Employed"),
                 key="_work_status", on_change=keep, args=["work_status"])

    if "work_status" in st.session_state.keys() and st.session_state.work_status != "" and st.session_state.work_status != "N/A":
        unkeep("income")
        st.number_input("Last Year's Income: ", key="_income", on_change=keep, args=["income"])
        unkeep("job_title")
        st.text_input("Job Title: ", key="_job_title", on_change=keep, args=["job_title"])


    unkeep("resident_status")
    st.selectbox(
        "Residency Status: ",
        ("", "U.S. Citizen", "Permanent resident (Green Card holder)", "International Student (F-1 visa, J-1 visa, etc)", "Foreign Worker (H-1B visa, H-1B1 visa, etc)", "N/A"),
        key="_resident_status", on_change=keep, args=["resident_status"]
    )

    unkeep("student_status")
    st.selectbox(
        "Student Status: ",
        ("", "In-State Student", "Out-of-State Student", "International Student", "N/A"),
        key="_student_status", on_change=keep, args=["student_status"]
    )
    if "student_status" in st.session_state.keys() and st.session_state.student_status != "" and st.session_state.student_status != "N/A":
        unkeep("enrollment_status")
        st.selectbox(
            "Enrollment Status: ",
            ("", "Full-time Student", "Part-Time Student"),
            key="_enrollment_status", on_change=keep, args=["enrollment_status"]
        )
    


st.audio("menu.mp3", format="audio/mpeg", loop=True, autoplay=True)

# Add image to bottom right corner of the screen
st.html(f"""
    <div id="title_div">
    <img src="app/static/title_bg.png" id="title_bg_right"/>
        <img src="app/static/title_bg.png" id="title_bg_left"/>
    </div>
    """)