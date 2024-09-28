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
st.html("""<button>Stone and Steel</button>""")
st.image("budget_vault_bg.png")

