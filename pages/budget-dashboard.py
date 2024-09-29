import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime, timedelta

# Load custom CSS
with open("static/style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

home, budget, quiz, advising = st.columns(4, vertical_alignment="top", gap="small")

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


home.page_link("app.py", label="Home")

budget.page_link("pages/budget-dashboard.py", label="Budgeting")

quiz.page_link("pages/quizzes.py", label="Quiz Me")

advising.page_link("pages/advising.py", label="Advising")

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
st.write("Manage your savings goals, budget, and expenses all in one place!")

# Savings Goal Section
with st.expander("Set Your Savings Goal", expanded=False):
    savings_goal_input = st.number_input("Enter your savings goal:", min_value=0, step=10)
    if st.button("Set Savings Goal"):
        st.session_state.savings_goal = savings_goal_input
        st.success(f"Savings goal of ${st.session_state.savings_goal} set!")
        savings_goal_text.markdown(f"<span class='savings-goal'>**Savings Goal:** ${st.session_state.savings_goal}</span>", unsafe_allow_html=True)

# Budget Input Section
with st.expander("Set Your Monthly Budget", expanded=False):
    budget_input = st.number_input("Enter your monthly budget:", min_value=0, step=10)

    if st.button("Submit Budget"):
        st.session_state.budget = budget_input
        st.session_state.coins += 1  # Increment coins by 1
        st.session_state.last_budget_date = datetime.now()
        st.success(f"Budget of ${st.session_state.budget} set! You've earned 1 coin!")
        budget_display.markdown(f"**Total Budget:** ${st.session_state.budget}")

# Expense Tracking Section
with st.expander("Track Your Expenses", expanded=False):
    expense_category = st.selectbox("Select Expense Category:", ["Food", "Transport", "Entertainment", "Others"])
    expense_input = st.number_input("Enter an expense:", min_value=0, step=1)

    if st.button("Add Expense"):
        if expense_input > 0:
            st.session_state.expenses.append({"category": expense_category, "amount": expense_input})
            st.success(f"Expense of ${expense_input} added to {expense_category}!")

            # Update Expenses Display in Sidebar
            expense_df = pd.DataFrame(st.session_state.expenses)
            aggregated_expenses = expense_df.groupby('category').sum().reset_index()

            expenses_summary = "\n".join([f"<div class='expense-item'>"
                f"{'🥗' if row['category'] == 'Food' else '🚗' if row['category'] == 'Transport' else '🎉' if row['category'] == 'Entertainment' else '🛍️'} "
                f"<strong class='expense-title'>{row['category']}</strong>: ${row['amount']}</div>" 
                for _, row in aggregated_expenses.iterrows()])
            expenses_display.markdown(f"**Expenses:**<br>{expenses_summary}", unsafe_allow_html=True)

            # Display Expenses DataFrame
            st.write("**Expenses:**")
            st.dataframe(expense_df)

            # Bar chart for expenses with custom colors
            expense_summary = expense_df.groupby("category").sum().reset_index()

            # Define a color map for the categories
            color_map = {
                "Food": "#ff9999",         # Light red
                "Transport": "#66b3ff",   # Light blue
                "Entertainment": "#99ff99",# Light green
                "Others": "#ffcc99"       # Light orange
            }

            # Create a bar chart using Altair
            chart = alt.Chart(expense_summary).mark_bar().encode(
                x=alt.X('category', title='Expense Category'),
                y=alt.Y('amount', title='Amount'),
                color=alt.Color('category', scale=alt.Scale(domain=list(color_map.keys()), range=list(color_map.values()))),
                tooltip=['category', 'amount']
            ).properties(
                title='Expense Distribution'
            )

            st.altair_chart(chart, use_container_width=True)
        else:
            st.warning("Please enter a valid expense.")

# Calculate Savings Progress
if st.session_state.budget > 0:
    total_expenses = sum(item['amount'] for item in st.session_state.expenses)
    remaining_budget = st.session_state.budget - total_expenses

    st.write(f"**Total Expenses:** ${total_expenses}")
    st.write(f"**Remaining Budget:** ${remaining_budget}")

    if st.session_state.savings_goal > 0:
        savings_percentage = max((remaining_budget / st.session_state.savings_goal) * 100, 0)
        st.write(f"You have saved {savings_percentage:.2f}% of your goal!")

        # Show Progress Bar in Main Page
        progress_color = "red" if savings_percentage < 50 else "orange" if savings_percentage < 80 else "green"
        st.markdown(f"""
            <div style="background: rgba(50, 50, 50, 0.8); border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); height: 30px; position: relative;">
                <div style="background: {progress_color}; width: {savings_percentage}%; height: 100%; border-radius: 10px; 
                     transition: width 0.5s;"></div>
            </div>
            <p style="text-align: center; font-weight: bold; color: #fff;">{savings_percentage:.2f}%</p>
        """, unsafe_allow_html=True)

        # Show Progress Bar in Sidebar (thinner)
        st.sidebar.markdown(f"**Savings Progress:** {savings_percentage:.2f}%")
        st.sidebar.markdown(f"""
            <div style="background: rgba(50, 50, 50, 0.8); border-radius: 10px; height: 20px; position: relative;">
                <div style="background: {progress_color}; width: {savings_percentage}%; height: 100%; border-radius: 10px; 
                     transition: width 0.5s;"></div>
            </div>
        """, unsafe_allow_html=True)

# Sidebar: Gold Counter Section
st.sidebar.markdown("---")  # Add a separator in the sidebar
st.sidebar.markdown("<span class='savings-goal'>Your Gold</span>", unsafe_allow_html=True)  # Updated style
coin_image = "static/coin.png"  # Path to your coins image
st.sidebar.image(coin_image, width=20)  # Display the coin image

# Change the number of coins to gold color
gold_number = f"<span style='color: gold;'>{st.session_state.coins}</span>"
st.sidebar.markdown(gold_number, unsafe_allow_html=True)  # Updated style

# Optional: Add a description below the gold counter in the sidebar
st.sidebar.markdown("<p class='coin-counter'>Collect gold by setting your budget!</p>", unsafe_allow_html=True)
