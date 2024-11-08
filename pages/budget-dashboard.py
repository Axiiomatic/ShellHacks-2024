import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime, timedelta
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
    background-size: cover;
    background-size: 100vw 100vh;
    background: linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.8) ), url("data:image/png;base64,%s");
    background-position:center top;
    
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('static/budget_bg.png')

hide_streamlit_style = """
            <style>
                /* Hide the Streamlit header and menu */
                header {visibility: hidden;}
                /* Optionally, hide the footer */
                .streamlit-footer {display: none;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Load custom CSS
with open("static/style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

home, budget, quiz, advising = st.columns(4, vertical_alignment="top", gap="small")

# Add custom CSS for sidebar title and expense items with light/dark mode support
st.markdown("""<style>
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
        .expense-bubble {
            background-color: rgba(255, 255, 255, 0.8);
            color: #000;  /* Set text color to black */
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
        .expense-bubble {
            background-color: #000;  /* Set background color to black */
            color: #fff;  /* Set text color to white for readability */
        }
    }
</style>""", unsafe_allow_html=True)

home.page_link("app.py", label="Home")
budget.page_link("pages/budget-dashboard.py", label="Budgeting")
quiz.page_link("pages/quizzes.py", label="Showdown")
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

# Refresh Button
if st.sidebar.button("Refresh"):
    st.session_state.expenses = []  # Clear only the expenses
    st.session_state.budget = 0      # Optionally reset budget
    st.session_state.savings_goal = 0  # Optionally reset savings goal
    st.session_state.last_budget_date = datetime.now() - timedelta(days=30)
    st.success("Page Refreshed!")  # Provide feedback to user

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
        f"{'🥗' if row['category'] == 'Food' else '🚗' if row['category'] == 'Transport' else '🎉' if row['category'] == 'Entertainment' else '🏠' if row['category'] == 'Housing' else '🛍️'} "
        f"<strong class='expense-title'>{row['category']}</strong>: ${row['amount']}</div>" 
        for _, row in aggregated_expenses.iterrows()])
    
    expenses_display.markdown(f"""
        <div class='expense-bubble' style='border-radius: 10px; padding: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); margin-bottom: 20px;'>
            <strong style='font-size: 16px;'>Expenses:</strong><br>
            {expenses_summary}
        </div>
    """, unsafe_allow_html=True)
else:
    expenses_display.markdown("<strong>Expenses:</strong><br>No expenses recorded.", unsafe_allow_html=True)

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
    expense_category = st.selectbox("Select Expense Category:", ["Food", "Transport", "Entertainment", "Housing", "Others"])
    expense_input = st.number_input("Enter an expense:", min_value=0, step=1)

    if st.button("Add Expense"):
        if expense_input > 0:
            st.session_state.expenses.append({"category": expense_category, "amount": expense_input})
            st.success(f"Expense of ${expense_input} added to {expense_category}!")

            # Update Expenses Display in Sidebar
            expense_df = pd.DataFrame(st.session_state.expenses)
            aggregated_expenses = expense_df.groupby('category').sum().reset_index()

            expenses_summary = "\n".join([f"<div class='expense-item'>"
                f"{'🥗' if row['category'] == 'Food' else '🚗' if row['category'] == 'Transport' else '🎉' if row['category'] == 'Entertainment' else '🏠' if row['category'] == 'Housing' else '🛍️'} "
                f"<strong class='expense-title'>{row['category']}</strong>: ${row['amount']}</div>" 
                for _, row in aggregated_expenses.iterrows()])
            
            expenses_display.markdown(f"""
                <div class='expense-bubble' style='border-radius: 10px; padding: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); margin-bottom: 20px;'>
                    <strong style='font-size: 16px;'>Expenses:</strong><br>
                    {expenses_summary}
                </div>
            """, unsafe_allow_html=True)

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
                "Housing": "#ffcc99",     # Light orange
                "Others": "#d3d3d3"       # Light gray
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

        # Confetti Animation on Goal Reached
        if savings_percentage >= 100:
            st.markdown("""
                <script src="https://cdnjs.cloudflare.com/ajax/libs/canvas-confetti/1.4.0/confetti.min.js"></script>
                <script>
                    var count = 200;
                    var defaults = { origin: { y: 0.7 } };

                    function fire(particleRatio, opts) {
                        confetti(Object.assign({}, defaults, opts, {
                            particleCount: Math.floor(count * particleRatio)
                        }));
                    }

                    function celebrate() {
                        setInterval(function() {
                            fire(0.25, { spread: 26, startVelocity: 55, decay: 0.9, scalar: 1.2 });
                            fire(0.2, { spread: 60 });
                            fire(0.35, { spread: 100, decay: 0.91, scalar: 1.2 });
                            fire(0.1, { spread: 120, startVelocity: 25, decay: 0.92, scalar: 1.2 });
                        }, 200);
                        
                        // Add a celebratory banner
                        const banner = document.createElement('div');
                        banner.id = 'celebration-banner';
                        banner.style.position = 'fixed';
                        banner.style.top = '0';
                        banner.style.left = '0';
                        banner.style.right = '0';
                        banner.style.background = 'rgba(255, 215, 0, 0.9)';
                        banner.style.color = '#000';
                        banner.style.fontSize = '24px';
                        banner.style.textAlign = 'center';
                        banner.style.padding = '10px';
                        banner.style.zIndex = '1000';
                        banner.innerHTML = '🎉 Congratulations! You\'ve reached your savings goal! 🎉';
                        document.body.appendChild(banner);

                        setTimeout(() => {
                            banner.style.transition = 'opacity 2s';
                            banner.style.opacity = 0;
                            setTimeout(() => banner.remove(), 2000); // Remove after fade out
                        }, 3000);
                    }
                    celebrate();
                </script>
            """, unsafe_allow_html=True)

            st.success("🎉 Congratulations! You've reached your savings goal! 🎉")

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

st.audio("budget.mp3", format="audio/mpeg", loop=True, autoplay=True)