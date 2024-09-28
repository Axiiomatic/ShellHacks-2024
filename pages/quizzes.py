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

def answer(question):
    "Correct" if a1 == "A" else "Incorrect, Answer A"
    "Correct" if a2 == "B" else "Incorrect, Answer B"    
    "Correct" if a3 == "A" else "Incorrect, Answer A"
    "Correct" if a4 == "B" else "Incorrect, Answer B"    
    "Correct" if a5 == "A" else "Incorrect, Answer A"
    "Correct" if a6 == "B" else "Incorrect, Answer B"    
    "Correct" if a7 == "A" else "Incorrect, Answer A"
    "Correct" if a8 == "B" else "Incorrect, Answer B"
    "Correct" if a9 == "A" else "Incorrect, Answer A"
    "Correct" if a10 == "B" else "Incorrect, Answer B"


q1, q2, q3, q4, q5, q6, q7, q8, q9, q10 = st.tabs(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
q1 = q1.radio("Q1", ["A", "B", "C", "D"], on_change=answer(q1,"A"))
q2 = q2.radio("Q2", ["A", "B", "C", "D"], on_change=answer(q2, "B"))
q3 = q3.radio("Q3", ["A", "B", "C", "D"], on_change=answer(q3, "A"))
q4 = q4.radio("Q4", ["A", "B", "C", "D"], on_change=answer(q4, "C"))
q5 = q5.radio("Q5", ["A", "B", "C", "D"], on_change=answer(q5, "D"))
q6 = q6.radio("Q6", ["A", "B", "C", "D"], on_change=answer(q6, "C"))
q7 = q7.radio("Q7", ["A", "B", "C", "D"], on_change=answer(q7, "B"))
q8 = q8.radio("Q8", ["A", "B", "C", "D"], on_change=answer(q8, "B"))
q9 = q9.radio("Q9", ["A", "B", "C", "D"], on_change=answer(q9, "D"))
q10 = q10.radio("Q10", ["A", "B", "C", "D"], on_change=answer(q10, "A"))

def answer(question, answer): {str(question)}.write("Correct") if {str(question)} == answer else {str(question)}.write("Incorrect, Answer "+{answer})