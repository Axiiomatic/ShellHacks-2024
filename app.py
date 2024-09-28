# app.py
import streamlit as st

home, budget, quiz, tutorial = st.columns(4, vertical_alignment="top", gap="medium")
with home:
    st.page_link("app.py", label="Home", icon="🏠")

with budget:
    st.page_link("pages/budget-dashboard.py", label="Budgeting", icon="🧾")

with quiz:
    st.page_link("pages/quizzes.py", label="Quiz Me", icon="✏")

with tutorial:
    st.page_link("pages/tutorial.py", label="Tutorial")

st.markdown("""
<style>
   h1 {
      font-size: 2em;
      text-align: center;
      text-transform: uppercase;
   }

   p {

}
</style>
""", unsafe_allow_html=True)
with open('style.css') as f:
    css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


st.title("Treasure Keeper")
st.write("We help first-generation students with financial issues. Make this a paragraph long.")
