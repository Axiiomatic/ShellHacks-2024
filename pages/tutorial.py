#tutorial.py

import streamlit as st

with open( "static/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

home, budget, quiz, tutorial = st.columns(4, vertical_alignment="top", gap="medium")
with home:
    st.page_link("app.py", label="Home", icon="home.png")

with budget:
    st.page_link("pages/budget-dashboard.py", label="Budgeting", icon="coin.png")

with quiz:
    st.page_link("pages/quizzes.py", label="Quiz Me", icon="showdown.png")

with tutorial:
    st.page_link("pages/tutorial.py", label="Tutorial")

st.title("Showdown Tutorial")
st.write("Explains how to use the project, showdown mechanics, and how to use the extension to practice saving")