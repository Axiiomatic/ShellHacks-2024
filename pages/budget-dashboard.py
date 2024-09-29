#budget-dashboard.py

import streamlit as st

with open( "static/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

home, budget, quiz, advising = st.columns(4, vertical_alignment="top", gap="small")

home.page_link("app.py", label="Home")

budget.page_link("pages/budget-dashboard.py", label="Budgeting")

quiz.page_link("pages/quizzes.py", label="Quiz Me")

advising.page_link("pages/advising.py", label="Advising")

st.title("Budget Dashboard")
st.write("Allow user to input their budget, see an overview, plan purchases and monthly payments.")

st.audio("menu.mp3", format="audio/mpeg", loop=True, autoplay=True)
