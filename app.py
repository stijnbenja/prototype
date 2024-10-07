import streamlit as st
import random
import time

# Set up the chat interface title
st.image('https://www.dyme.app/img/logo.png',width=60)
st.title("Personal Financial Advisor Chatbot")

st.write("Welcome to Dyme's Generative AI-powered financial advisor.")
st.write("Ask any questions about your finances, such as saving strategies, investment options, or debt repayment plans.")

# Simulated user financial data
user_data = {
    'salary': 3000,  # Monthly salary
    'monthly_expenses': 2000,
    'savings_goal': 10000,
    'current_savings': 1500,
    'debt': 5000
}

# Function to generate personalized financial advice
def generate_financial_advice(user_input):
    responses = [
        "Based on your income and expenses, we recommend saving 20% of your monthly salary.",
        "You could consider paying off €250 towards your debt this month to reach your goal of being debt-free in 2 years.",
        "It's a great time to invest in low-risk options. You can allocate 10% of your monthly savings towards investments.",
        "To reach your savings goal of €10,000 in 12 months, you should try to save €700 each month.",
        "Reducing your subscription services could free up an extra €100 per month."
    ]
    # Return a random response to simulate dynamic responses
    return random.choice(responses)

# Store the chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Capture user's message using st.chat_input
user_input = st.chat_input("Your message")

# If user sends a message
if user_input:
    # Append the user's message to the chat history and display it immediately
    with st.chat_message("user"):
        st.write(user_input)
    
    st.session_state.chat_history.append({"role": "user", "message": user_input})
    
    # Simulate a typing effect for the chatbot
    response_text = generate_financial_advice(user_input)
    
    # Simulate a delay before the bot's response and display it immediately
    bot_avatar = "D"  # Custom bot emoji/avatar
    with st.chat_message(bot_avatar):  # Use the custom avatar instead of the default "bot"
        message_placeholder = st.empty()
        full_message = ""
        for i in range(1, len(response_text) + 1):
            full_message = response_text[:i]
            message_placeholder.write(full_message)  # Simulate typing by streaming the response letter by letter
            time.sleep(0.025)  # Adjust typing speed if needed
        
    # Append the bot's message to the chat history
    st.session_state.chat_history.append({"role": "bot", "message": response_text})

# Display chat history in the correct order (oldest to newest)
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        with st.chat_message("user"):
            st.write(chat["message"])
    else:
        bot_avatar = "d"  # Custom bot emoji/avatar
        with st.chat_message(bot_avatar):
            st.write(chat["message"])

# Sidebar showing user financial summary
st.sidebar.title("User Financial Summary")
st.sidebar.write(f"Monthly Salary: €{user_data['salary']}")
st.sidebar.write(f"Monthly Expenses: €{user_data['monthly_expenses']}")
st.sidebar.write(f"Current Savings: €{user_data['current_savings']}")
st.sidebar.write(f"Debt: €{user_data['debt']}")
