#quizzes.py

import streamlit as st
import streamlit_book as stb

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

st.title("Quiz")
st.write("Standalone quizzes on financial literacy that test what you learned in the tutorial. they also give points. ")

stb.multiple_choice("I typically ask recruiters to point out which of these area pokemon",
                    {"ditto":True,
                     "jupyter":False,
                     "pyspark":False,
                     "scikit":False,
                     "metapod":True,
                     "vulpix":True}
                   )
