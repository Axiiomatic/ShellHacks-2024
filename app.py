# app.py
import streamlit as st

with open( "static/style.css") as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

homeIcon, home, budgetIcon, budget, quizIcon, quiz, tutorial = st.columns(7, vertical_alignment="top", gap="small")

home.page_link("app.py", label="Home")
homeIcon.image("home.png")

budget.page_link("pages/budget-dashboard.py", label="Budgeting")
budgetIcon.image("coin.png")

quiz.page_link("pages/quizzes.py", label="Quiz Me")
quizIcon.image("showdown.png")

tutorial.page_link("pages/tutorial.py", label="Tutorial")


st.title("Treasure Keeper")
st.write("We help first-generation students with financial issues. Make this a paragraph long.")
st.html("""<button background="budget_bg.png">Stone and Steel</button>""")

