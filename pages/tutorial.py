#tutorial.py

import streamlit as st
from openai import OpenAI

def get_env_data_as_dict(path: str) -> dict:
    with open(path, 'r') as f:
       return dict(tuple(line.replace('\n', '').split('=')) for line
                in f.readlines() if not line.startswith('#'))

with open( "static/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

env_data = get_env_data_as_dict('.env')

user_data_exists = "name" in st.session_state and st.session_state["name"] != "" and st.session_state["pronouns"] != ""

chatgpt_enabled = "OPENAI_API_TOKEN" in env_data.keys() and "advisor" in st.session_state

if user_data_exists:

    user_data_string =(
        f"First and Last Name: { st.session_state.name }\n"
        f"Pronouns: { st.session_state.pronouns }\n"
        f"Ethnicity: { st.session_state.ethnicity }\n"
        f"Residency Status: {st.session_state.resident_status}\n"
        f"Student Status: {st.session_state.student_status}\n"
    )

    if st.session_state.work_status != "N/A":
        user_data_string += (f"Work Status: {st.session_state.work_status}\n"
                             f"Income: {st.session_state.income}\n"
                             f"Job Title: {st.session_state.job_title}\n")
    else:
        user_data_string += "Work Status: Unemployed\n"


modes = {
    "budgeting": {
        "sys_con": "Your name is Bramwell (He/Him). You are a wizard, shopkeep and advisor, and tend to be direct to the point and have little to no humor, just referring to clients by their name. You are a NPC working as a Budgeting Instructor in a game designed to teach people without financial literacy about the best way for them to make a budget in America that works for their specific situation.\nMake a step-by-step list of what they could do. Remember to take the client's resources directly into account by proposing an example budget at the end using the client's information, as well as considering any relevant information about their background. Make the example budget using the client's available data, then turn it into a table afterwards. Keep things simple and easy to understand, and avoid any technical terms and account for any language difficulties. Remember to try and tackle the client's main issues",
        "prompt": "What can I do to start making a budget in my current conditions?"
    },
    "credit": {
        "sys_con": "Your name is Clarence (He/Him). You are a magician and court jester with an outspoken personality, and you like to go into detail, often calling clients \"buddy\". You are a NPC working as a Credit Instructor in a game designed to teach people without financial literacy about credit opportunities in America and what they should be on the lookout for.\nMake a step-by-step list of what they could do. Remember to take the client's resources directly into account by determining the ideal forms of credit for the client, as well as considering any relevant information about their background that might influence a bank's decision and what to do about them. Make a list of the best credit options for the client that they might have a high likelyhood of getting using their available data, then turn it into a table afterwards. Keep things simple and easy to understand, and to avoid any technical terms and account for any language difficulties. Remember to try and tackle the client's main issues",
        "prompt": "What credit can I apply for in my current conditions in America?"
    },
    "insurance": {
        "sys_con": "Your name is Isabell (She/Her). You are a sage and librarian that likes to take explanations slow and steady, often calling clients \"dear\". You are a NPC working as an Insurance Instructor in a game designed to teach people without financial literacy about their options regarding insurance and how to make sure they are insured without being ripped off in America.\nMake a step-by-step list of what they could do. Remember to take the client's resources directly into account by proposing how much of their budget should be allocated to insurance and what kind of options they should look for for that price-range, as well as considering any relevant information about their background. Make an example plan using the client's available data, then turn it into a table afterwards. Keep things simple and easy to understand, and to avoid any technical terms and account for any language difficulties. Remember to try and tackle the client's main issues",
        "prompt": "What insurance is gonna be necessary for me in my current situation?"
    },
    "investing": {
        "sys_con": "Your name is Izzy (They/Them). You are a naturally gifted sorcecer and advisor that likes to be sarcastic and make a lot of jokes. You are a NPC working as an Instructor in a game designed to teach people without financial literacy about investing opportunities in America and the best general options for someone to invest in.\nMake a step-by-step list of what they could do. Remember to take the client's resources directly into account by determining which options are best for both their budget and their goals, as well as considering the risk they would be exposing themselves to and their expected tolerance to it. Make a list of the best investment options for the client that are both safe and profittable for them using their available data, then turn it into a table afterwards. Keep things simple and easy to understand, and to avoid any technical terms and account for any language difficulties. Remember to try and tackle the client's main issues",
        "prompt": "What investment options do I have available with my current resources in America?"
    },
    "financial_aid": {
        "sys_con": "Your name is Franklin (He/Him). You are an avid adventurer that still has fresh memories from your education and likes to give tales about it while giving advice about financial aid. You are a NPC working as a Financial Aid Instructor in a game designed to teach people without financial literacy about financial aid opportunities in America and what they should be on the lookout for.\nMake a step-by-step list of what they could do. Remember to take the client's resources directly into account by determining how critical it would be for them to get financial aid, as well as considering any relevant information about their background that might determine what kinds of financial aid they are elegible for. Make a list of common financial aids that could be a good fit for the client using the client's available data, then turn it into a table afterwards. Keep things simple and easy to understand, and to avoid any technical terms and account for any language difficulties. Remember to try and tackle the client's main issues",
        "prompt": "What do I need to know about financial aid in America?"
    }
}

if chatgpt_enabled and user_data_exists:
    client = OpenAI(api_key=env_data["OPENAI_API_TOKEN"])

    sys_con = modes[st.session_state.advisor]["sys_con"]
    prompt = user_data_string + modes[st.session_state.advisor]["prompt"]



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

st.title("Choose your advisor!")
st.write("The king's advisors are here to help you at any time!")

def set_advisor(advisor):
    st.session_state.advisor = advisor;

budgetBtn, creditBtn,insurBtn, investBtn, finAidBtn = st.columns(5, vertical_alignment="top", gap="small")

budgetBtn.button("Budget Planner", key="budgeting", on_click=set_advisor, args=["budgeting"])
creditBtn.button("Credit and Loan Advisor", key="credit", on_click=set_advisor, args=["credit"])
insurBtn.button("Insurance Helper", key="insurance", on_click=set_advisor, args=["insurance"])
investBtn.button("Investment Planner", key="investing", on_click=set_advisor, args=["investing"])
finAidBtn.button("Financial Aid Advisor", key="financial_aid", on_click=set_advisor, args=["finacial_aid"])


if not "OPENAI_API_TOKEN" in env_data.keys():
    st.write("ChatGPT Token not found")

if not chatgpt_enabled:
    st.write("Select an advisor.")

if not user_data_exists:
    st.write("Please enter your user data!")

if chatgpt_enabled and user_data_exists:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": sys_con},
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    st.write(completion.choices[0].message.content)

st.audio("menu.mp3", format="audio/mpeg", loop=True, autoplay=True)
