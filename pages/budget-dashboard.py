import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime, timedelta

# Load custom CSS
with open("static/style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

# Add custom CSS for sidebar title and expense items with light/dark mode support
st.markdown("""
    <style>
    .sidebar .sidebar-title {
        font-size: 32px;  
        font-weight: bold;
        color: #fff;  
        text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00; 
    }
    .sidebar .expense-item {
        font-size: 14px; 
        font-weight: bold; 
        line-height: 1.5; 
    }

    /* Light Mode Styles */
    @media (prefers-color-scheme: light) {
        .sidebar .expense-title,
        .sidebar .coin-counter,
        .sidebar .savings-goal,
        .sidebar {
            color: #000 !important;  /* Set all sidebar text to black */
        }
    }

    /* Dark Mode Styles */
    @media (prefers-color-scheme: dark) {
        .sidebar .expense-title,
        .sidebar .coin-counter,
        .sidebar .savings-goal,
        .sidebar {
            color: #fff !important;  /* Set all sidebar text to white */
        }
    }
    </style>
""", unsafe_allow_html=True)

# Navigation icons
homeIcon, home, budgetIcon, budget, quizIcon, quiz, tutorialIcon, tutorial = st.columns(8, vertical_alignment="top", gap="small")

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''
home.page_link("app.py", label="Home")
<<<<<<< HEAD
#home.markdown(hide_img_fs, unsafe_allow_html=True)
=======
home.markdown(hide_img_fs, unsafe_allow_html=True)
>>>>>>> a9b19e540cab8669f8ca22dfafaa79ed545dfd70
homeIcon.image("home.png")
budget.page_link("pages/budget-dashboard.py", label="Budgeting")
budgetIcon.image("coin.png")
quiz.page_link("pages/quizzes.py", label="Quiz Me")
quizIcon.image("showdown.png")
tutorial.page_link("pages/tutorial.py", label="Tutorial")
tutorialIcon.image("tutorial.png")

# Initialize session state
if 'budget' not in st.session_state:
    st.session_state.budget = 0
if 'coins' not in st.session_state:
    st.session_state.coins = 0
if 'last_budget_date' not in st.session_state:
    st.session_state.last_budget_date = datetime.now() - timedelta(days=30)
if 'expenses' not in st.session_state:
    st.session_state.expenses = []
if 'savings_goal' not in st.session_state:
    st.session_state.savings_goal = 0

# Sidebar with title
st.sidebar.markdown("<h1 class='sidebar-title'>Finance Board</h1>", unsafe_allow_html=True)

# Initialize savings goal display
savings_goal_text = st.sidebar.empty()
savings_goal_text.markdown(f"<span class='savings-goal'>**Savings Goal:** ${st.session_state.savings_goal}</span>", unsafe_allow_html=True)

# Initialize budget display
budget_display = st.sidebar.empty()
budget_display.markdown(f"**Total Budget:** ${st.session_state.budget}")

# Initialize expenses display
expenses_display = st.sidebar.empty()

# Aggregate expenses by category
if st.session_state.expenses:
    expense_df = pd.DataFrame(st.session_state.expenses)
    aggregated_expenses = expense_df.groupby('category').sum().reset_index()

    expenses_summary = "\n".join([f"<div class='expense-item'>"
        f"{'🥗' if row['category'] == 'Food' else '🚗' if row['category'] == 'Transport' else '🎉' if row['category'] == 'Entertainment' else '🛍️'} "
        f"<strong class='expense-title'>{row['category']}</strong>: ${row['amount']}</div>" 
        for _, row in aggregated_expenses.iterrows()])
    expenses_display.markdown(f"**Expenses:**<br>{expenses_summary}", unsafe_allow_html=True)
else:
    expenses_display.markdown("**Expenses:**<br>No expenses recorded.", unsafe_allow_html=True)

# Title
st.title("Budget Dashboard")
st.write("Allow user to input their budget, see an overview, plan purchases and monthly payments.")

st.audio("menu.mp3", format="audio/mpeg", loop=True, autoplay=True)
