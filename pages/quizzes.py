#quizzes.py

import streamlit as st


with open( "static/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

homeIcon, home, budgetIcon, budget, quizIcon, quiz, tutorialIcon, tutorial = st.columns(8, vertical_alignment="top", gap="small")

home.page_link("app.py", label="Home")
homeIcon.image("home.png")

budget.page_link("pages/budget-dashboard.py", label="Budgeting")
budgetIcon.image("coin.png")

quiz.page_link("pages/quizzes.py", label="Quiz Me")
quizIcon.image("showdown.png")

tutorial.page_link("pages/tutorial.py", label="Tutorial")
tutorialIcon.image("tutorial.png")

st.title("Quiz")
st.write("Standalone quizzes on financial literacy that test what you learned in the tutorial. they also give points. ")


q1, q2, q3, q4, q5, q6, q7, q8, q9, q10 = st.tabs(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

with q1:
    a1 = st.radio("Q1", ["A", "B", "C", "D"])
    st.write("correct") if a1 == "A" else st.write("Incorrect")

with q2:
    a2 = st.radio("Q2", ["A", "B", "C", "D"])
    st.write("correct") if a2 == "A" else st.write("Incorrect")

with q3:
    a3 = st.radio("Q3", ["A", "B", "C", "D"])
    st.write("correct") if a3 == "A" else st.write("Incorrect")

with q4:
    a4 = st.radio("Q4", ["A", "B", "C", "D"])
    st.write("correct") if a4 == "A" else st.write("Incorrect")

with q5:
    a5 = st.radio("Q5", ["A", "B", "C", "D"])
    st.write("correct") if a5 == "A" else st.write("Incorrect")

with q6:
    a6 = st.radio("Q6", ["A", "B", "C", "D"])
    st.write("correct") if a6 == "A" else st.write("Incorrect")

with q7:
    a7 = st.radio("Q7", ["A", "B", "C", "D"])
    st.write("correct") if a7 == "A" else st.write("Incorrect")

with q8:
    a8 = st.radio("Q8", ["A", "B", "C", "D"])
    st.write("correct") if a8 == "A" else st.write("Incorrect")

with q9:
    a9 = st.radio("Q9", ["A", "B", "C", "D"])
    st.write("correct") if a9 == "A" else st.write("Incorrect")

with q10:
    a10 = st.radio("Q10", ["A", "B", "C", "D"])
    st.write("correct") if a9 == "A" else st.write("Incorrect")
