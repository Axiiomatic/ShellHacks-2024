import streamlit as st

# Add CSS for animations and styling
st.markdown("""
<style>
    @keyframes correct-animation {
        0% { transform: scale(1); opacity: 0; }
        50% { transform: scale(1.2); opacity: 1; }
        100% { transform: scale(1); }
    }
    @keyframes incorrect-animation {
        0% { transform: scale(1); opacity: 0; }
        50% { transform: scale(0.8); opacity: 1; }
        100% { transform: scale(1); }
    }
    .correct {
        color: green;
        font-size: 24px;
        animation: correct-animation 0.5s ease forwards;
    }
    .incorrect {
        color: red;
        font-size: 24px;
        animation: incorrect-animation 0.5s ease forwards;
    }
    .success-bar {
        background-color: #4caf50;
        color: white;
        padding: 10px;
        border-radius: 5px;
        font-size: 20px;
        margin-top: 20px;
    }
    .coins {
        color: gold;
        font-size: 32px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

with open("static/style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

home, budget, quiz, advising = st.columns(4, vertical_alignment="top", gap="small")

home.page_link("app.py", label="Home")
budget.page_link("pages/budget-dashboard.py", label="Budgeting")
quiz.page_link("pages/quizzes.py", label="Quiz Me")
advising.page_link("pages/advising.py", label="Advising")

if 'coins' not in st.session_state:
    st.session_state.coins = 0

# Track the current question index
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0    

st.title("Quiz")
st.write("Standalone quizzes on financial literacy that test what you learned in advising. They also give points.")

st.audio("battle.mp3", format="audio/mpeg", loop=True, autoplay=True)

questions = [
    ("What is the primary purpose of creating a budget?", 
     ["A) To avoid paying bills", 
      "B) To plan how to spend money and manage income versus expenses", 
      "C) To increase debt", 
      "D) To save for a vacation"], 
     "B) To plan how to spend money and manage income versus expenses"),
    
    ("Which of the following is a key component of a successful budget?", 
     ["A) Ignoring savings", 
      "B) Spending more than you earn", 
      "C) Tracking income and expenses regularly", 
      "D) Only accounting for fixed expenses"], 
     "C) Tracking income and expenses regularly"),
    
    ("What is a credit score used for?", 
     ["A) To determine how much interest you pay on savings", 
      "B) To evaluate an individual's creditworthiness for loans and credit cards", 
      "C) To track your checking account balance", 
      "D) To invest in the stock market"], 
     "B) To evaluate an individual's creditworthiness for loans and credit cards"),
    
    ("Which of the following actions can improve your credit score?", 
     ["A) Maxing out your credit cards", 
      "B) Making late payments", 
      "C) Paying bills on time and keeping credit utilization low", 
      "D) Opening multiple credit accounts at once"], 
     "C) Paying bills on time and keeping credit utilization low"),
    
    ("What is the purpose of insurance?", 
     ["A) To increase monthly bills", 
      "B) To provide financial protection against unforeseen events like accidents or illness", 
      "C) To avoid paying for healthcare", 
      "D) To earn interest on your savings"], 
     "B) To provide financial protection against unforeseen events like accidents or illness"),
    
    ("What is a deductible in an insurance policy?", 
     ["A) The amount of money you receive after filing a claim", 
      "B) The amount you must pay out-of-pocket before insurance covers a claim", 
      "C) A type of insurance", 
      "D) The monthly premium"], 
     "B) The amount you must pay out-of-pocket before insurance covers a claim"),
    
    ("What is the FAFSA used for?", 
     ["A) To apply for personal loans", 
      "B) To apply for federal student aid, including grants, loans, and work-study programs", 
      "C) To pay taxes", 
      "D) To open a savings account"], 
     "B) To apply for federal student aid, including grants, loans, and work-study programs"),
    
    ("Which type of financial aid does not need to be repaid?", 
     ["A) Student loans", 
      "B) Grants and scholarships", 
      "C) Credit card debt", 
      "D) Work-study earnings"], 
     "B) Grants and scholarships"),
    
    ("What is the main goal of investing?", 
     ["A) To lose money", 
      "B) To earn returns over time and grow wealth", 
      "C) To avoid paying taxes", 
      "D) To increase your debt"], 
     "B) To earn returns over time and grow wealth"),
    
    ("Which of the following is considered a low-risk investment?", 
     ["A) Stocks", 
      "B) Bonds", 
      "C) Cryptocurrencies", 
      "D) Collectibles"], 
     "B) Bonds")
]

def check_answer(answer, correct_answer):
    return answer == correct_answer

if st.session_state.current_question < len(questions):
    question, options, correct_answer = questions[st.session_state.current_question]
    
    # Display question number
    st.write(f"Question {st.session_state.current_question + 1} of {len(questions)}")

    with st.form(key=f'quiz{st.session_state.current_question + 1}'):
        selected_option = st.radio(question, options)
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            if check_answer(selected_option, correct_answer):
                st.markdown('<div class="correct">Correct!</div>', unsafe_allow_html=True)
                st.session_state.coins += 1  # Increment coins for a correct answer
                st.session_state.current_question += 1  # Move to the next question
            else:
                st.markdown('<div class="incorrect">Incorrect. Please try again.</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="success-bar">You\'ve completed the quiz! 🎉</div>', unsafe_allow_html=True)
    st.write(f"Total Coins: <span class='coins'>{st.session_state.coins}</span>", unsafe_allow_html=True)
