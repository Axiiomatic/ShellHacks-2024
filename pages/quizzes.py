#quizzes.py

import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    image-rendering: pixelated;
    background-size: 100vw 100vh;
    background-image: url("data:image/png;base64,%s");
    background-position:center top;
    
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('static/showdown_bg.png')

hide_streamlit_style = """
            <style>
                /* Hide the Streamlit header and menu */
                header {visibility: hidden;}
                /* Optionally, hide the footer */
                .streamlit-footer {display: none;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with open( "static/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

home, budget, quiz, advising = st.columns(4, vertical_alignment="top", gap="small")

home.page_link("app.py", label="Home")

budget.page_link("pages/budget-dashboard.py", label="Budgeting")

quiz.page_link("pages/quizzes.py", label="Showdown")

advising.page_link("pages/advising.py", label="Advising")

if 'coins' not in st.session_state:
    st.session_state.coins = 0    

st.title("Showdown!")
st.write("Test what you've learned! Go through a series of questions on financial literacy to prove your growth and new knowledge. If you succeed, who knows what awaits behind that door...")

st.audio("battle.mp3", format="audio/mpeg", loop=True, autoplay=True)

q1, q2, q3, q4, q5, q6, q7, q8, q9, q10 = st.tabs(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

with q1:
    a1 = st.radio("What is the primary purpose of creating a budget?", ["A) To avoid paying bills", "B) To plan how to spend money and manage income versus expenses", "C) To increase debt", "D) To save for a vacation"])
    if a1 == "B) To plan how to spend money and manage income versus expenses":
        st.write("correct") 
        st.sidebar.markdown("![Confetti](https://img1.picmix.com/output/stamp/normal/0/3/0/1/2561030_878bc.gif)", unsafe_allow_html=True) 
        st.session_state.coins += 1;
    else: st.write("Incorrect")

with q2:
    a2 = st.radio("Which of the following is a key component of a successful budget?", ["A) Ignoring savings", "B) Spending more than you earn", "C) Tracking income and expenses regularly", "D) Only accounting for fixed expenses"])
    if a2 == "C) Tracking income and expenses regularly":
        st.write("correct")
        st.sidebar.markdown("![Confetti](https://img1.picmix.com/output/stamp/normal/0/3/0/1/2561030_878bc.gif)", unsafe_allow_html=True) 
        st.session_state.coins += 1;
    else: st.write("Incorrect")

with q3:
    a3 = st.radio("What is a credit score used for?", ["A) To determine how much interest you pay on savings", "B) To evaluate an individual's creditworthiness for loans and credit cards", "C) To track your checking account balance", "D) To invest in the stock market"])
    if a3 == "B) To evaluate an individual's creditworthiness for loans and credit cards": 
        st.write("correct")
        st.sidebar.markdown("![Confetti](https://img1.picmix.com/output/stamp/normal/0/3/0/1/2561030_878bc.gif)", unsafe_allow_html=True)
        st.session_state.coins += 1;
    else: st.write("Incorrect")

with q4:
    a4 = st.radio("Which of the following actions can improve your credit score?", ["A) Maxing out your credit cards", "B) Making late payments", "C) Paying bills on time and keeping credit utilization low", "D) Opening multiple credit accounts at once"])
    if a4 == "C) Paying bills on time and keeping credit utilization low": 
        st.write("correct")
        st.sidebar.markdown("![Confetti](https://img1.picmix.com/output/stamp/normal/0/3/0/1/2561030_878bc.gif)", unsafe_allow_html=True) 
        st.session_state.coins += 1;
    else: st.write("Incorrect")

with q5:
    a5 = st.radio("What is the purpose of insurance?", ["A) To increase monthly bills", "B) To provide financial protection against unforeseen events like accidents or illness", "C) To avoid paying for healthcare", "D) To earn interest on your savings"])
    if a5 == "B) To provide financial protection against unforeseen events like accidents or illness": 
        st.write("correct")
        st.sidebar.markdown("![Confetti](https://img1.picmix.com/output/stamp/normal/0/3/0/1/2561030_878bc.gif)", unsafe_allow_html=True) 
        st.session_state.coins += 1;
    else: st.write("Incorrect")

with q6:
    a6 = st.radio("What is a deductible in an insurance policy?", ["A) The amount of money you receive after filing a claim", "B) The amount you must pay out-of-pocket before insurance covers a claim", "C) A type of insurance", "D) The monthly premium"])
    if a6 == "B) The amount you must pay out-of-pocket before insurance covers a claim": 
        st.write("correct")
        st.sidebar.markdown("![Confetti](https://img1.picmix.com/output/stamp/normal/0/3/0/1/2561030_878bc.gif)", unsafe_allow_html=True)
        st.session_state.coins += 1;
    else: st.write("Incorrect")

with q7:
    a7 = st.radio("What is the FAFSA used for?", ["A) To apply for personal loans", "B) To apply for federal student aid, including grants, loans, and work-study programs", "C) To pay taxes", "D) To open a savings account"])
    if a7 == "B) To apply for federal student aid, including grants, loans, and work-study programs":
        st.write("correct")
        st.sidebar.markdown("![Confetti](https://img1.picmix.com/output/stamp/normal/0/3/0/1/2561030_878bc.gif)", unsafe_allow_html=True)
        st.session_state.coins += 1;
    else: st.write("Incorrect")

with q8:
    a8 = st.radio("Which type of financial aid does not need to be repaid?", ["A) Student loans", "B) Grants and scholarships", "C) Credit card debt", "D) Work-study earnings"])
    if a8 == "B) Grants and scholarships":
        st.write("correct")
        st.sidebar.markdown("![Confetti](https://img1.picmix.com/output/stamp/normal/0/3/0/1/2561030_878bc.gif)", unsafe_allow_html=True)
        st.session_state.coins += 1;
    else: st.write("Incorrect")

with q9:
    a9 = st.radio("What is the main goal of investing?", ["A) To lose money", "B) To earn returns over time and grow wealth", "C) To avoid paying taxes", "D) To increase your debt"])
    if a9 == "B) To earn returns over time and grow wealth": 
        st.write("correct")
        st.sidebar.markdown("![Confetti](https://img1.picmix.com/output/stamp/normal/0/3/0/1/2561030_878bc.gif)", unsafe_allow_html=True)
        st.session_state.coins += 1;    
    else: st.write("Incorrect")

with q10:
    a10 = st.radio("Which of the following is considered a low-risk investment?", ["A) Stocks", "B) Bonds", "C) Cryptocurrencies", "D) Collectibles"])
    if a9 == "B) Bonds": 
        st.write("correct")
        st.sidebar.markdown("![Confetti](https://img1.picmix.com/output/stamp/normal/0/3/0/1/2561030_878bc.gif)", unsafe_allow_html=True)
        st.session_state.coins += 1;
    else: st.write("Incorrect")

st.write(st.session_state.coins)