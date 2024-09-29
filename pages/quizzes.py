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
    a1 = st.radio("What does DEI stand for in the context of financial literacy?", ["A) Diversity, Ethics, and Inclusion", "B) Diversity, Equity, and Investment", "C) Diversity, Equity, and Inclusion", "D) Development, Equality, and Independence"])
    st.write("correct") if a1 == "C) Diversity, Equity, and Inclusion" else st.write("Incorrect")

with q2:
    a2 = st.radio("Why is financial literacy especially important for minority communities?", ["A) To increase individual wealth in majority communities", "B) To bridge the racial wealth gap and create opportunities for economic mobility", "C) To teach minority communities about taxes", "D) To increase consumer debt and credit card use"])
    st.write("correct") if a2 == "B) To bridge the racial wealth gap and create opportunities for economic mobility" else st.write("Incorrect")

with q3:
    a3 = st.radio("Which of the following is a barrier to financial success often faced by minority communities?", ["A) High interest savings accounts", "B) Lack of access to affordable financial services", "C) Employer-matched retirement funds", "D) Low housing costs"])
    st.write("correct") if a3 == "B) Lack of access to affordable financial services" else st.write("Incorrect")

with q4:
    a4 = st.radio("How can DEI efforts in financial institutions improve access to financial education for minorities?", ["A) By offering financial workshops only to the wealthy", "B) By providing culturally relevant financial education and support", "C) By reducing the number of financial aid programs", "D) By focusing on high-income earners"])
    st.write("correct") if a4 == "B) By providing culturally relevant financial education and support" else st.write("Incorrect")

with q5:
    a5 = st.radio("What is the racial wealth gap?", ["A) The income differences between men and women", "B) The gap in wealth accumulation between different racial and ethnic groups", "C) The difference in spending habits between individuals", "D) The inequality of bank fees between regions"])
    st.write("correct") if a5 == "B) The gap in wealth accumulation between different racial and ethnic groups" else st.write("Incorrect")

with q6:
    a6 = st.radio("What role do community development financial institutions (CDFIs) play in supporting minority financial literacy", ["A) They charge higher interest rates for minority clients", "B) They provide education, loans, and services tailored to underserved communities", "C) They invest in large corporations only", "D) They only work with high-income clients"])
    st.write("correct") if a6 == "B) They provide education, loans, and services tailored to underserved communities" else st.write("Incorrect")

with q7:
    a7 = st.radio("Which of the following is a key strategy to enhance financial literacy in minority communities?", ["A) Decreasing the number of local financial institutions", "B) Increasing targeted financial education programs and resources", "C) Eliminating credit scores as a requirement", "D) Raising interest rates on loans for minorities"])
    st.write("correct") if a7 == "B) Increasing targeted financial education programs and resources" else st.write("Incorrect")

with q8:
    a8 = st.radio("What is one potential impact of not addressing financial literacy gaps for minorities?", ["A) Decreased interest rates on loans", "B) An increase in home ownership", "C) Perpetuation of economic disparities and lack of upward mobility", "D) Equal employment opportunities"])
    st.write("correct") if a8 == "C) Perpetuation of economic disparities and lack of upward mobility" else st.write("Incorrect")

with q9:
    a9 = st.radio("Which of the following is a common financial challenge for minority-owned businesses?", ["A) Access to venture capital and affordable business loans", "B) Excessive access to loans", "C) Over-saturation in high-income markets", "D) Having too much investment in diverse sectors"])
    st.write("correct") if a9 == "A) Access to venture capital and affordable business loans" else st.write("Incorrect")

with q10:
    a10 = st.radio("How can financial institutions incorporate DEI to better serve minority communities?", ["A) By eliminating small business loans for minorities", "B) By hiring a diverse workforce and creating inclusive products and services", "C) By raising fees for minority clients", "D) By focusing solely on large corporations"])
    st.write("correct") if a9 == "B) By hiring a diverse workforce and creating inclusive products and services" else st.write("Incorrect")
