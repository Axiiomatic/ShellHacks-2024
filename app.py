# app.py
import streamlit as st

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
