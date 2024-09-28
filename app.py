# app.py
import streamlit as st

with open( "static/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

st.title("Treasure Keeper")
st.write("We help first-generation students with financial issues. Make this a paragraph long.")
