import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.3-70b-versatile")


# Memory and Conversation
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory, verbose=False)

# Streamlit page setup
st.set_page_config(page_title="TalentScout - Hiring Assistant")
st.title("🤖 TalentScout - Smart Hiring Assistant")

# Initialize session state
if "stage" not in st.session_state:
    st.session_state.stage = "greeting"
    st.session_state.data = {}
    st.session_state.chat_history = []
    st.session_state.tech_questions = []
    st.session_state.current_question_index = 0
    st.session_state.collecting_tech_answers = False

# Save to CSV
def save_to_csv(data, file='candidates.csv'):
    df = pd.DataFrame([data])
    if os.path.exists(file):
        df.to_csv(file, mode='a', header=False, index=False)
    else:
        df.to_csv(file, index=False)

# Show greeting on first load
if st.session_state.stage == "greeting":
    bot_reply = "Hi! I’m TalentScout 🤖. Let’s start your screening. What’s your full name?"
    st.session_state.chat_history.append(("bot", bot_reply))
    st.session_state.stage = "name"

# User input
user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))

    if any(word in user_input.lower() for word in ["exit", "bye", "quit"]):
        bot_reply = "👋 Thank you for your time! We’ll be in touch soon."
        st.session_state.chat_history.append(("bot", bot_reply))
        st.session_state.stage = "done"
        save_to_csv(st.session_state.data)
        st.rerun()

    data = st.session_state.data
    stage = st.session_state.stage

    # Conversation flow
    if stage == "name":
        data["Full Name"] = user_input
        bot_reply = "Great! What’s your email address?"
        st.session_state.stage = "email"

    elif stage == "email":
        data["Email"] = user_input
        bot_reply = "Thanks! What’s your phone number?"
        st.session_state.stage = "phone"

    elif stage == "phone":
        data["Phone"] = user_input
        bot_reply = "How many years of experience do you have?"
        st.session_state.stage = "experience"

    elif stage == "experience":
        data["Experience"] = user_input
        bot_reply = "What position are you applying for?"
        st.session_state.stage = "position"

    elif stage == "position":
        data["Position"] = user_input
        bot_reply = "Where are you currently located?"
        st.session_state.stage = "location"

    elif stage == "location":
        data["Location"] = user_input
        bot_reply = "Tell me about your tech stack (e.g., Python, React, SQL)..."
        st.session_state.stage = "tech_stack"

    elif stage == "tech_stack":
        data["Tech Stack"] = user_input
        tech_prompt = f"""
        You are a senior technical interviewer. Based on this tech stack: {user_input},
        generate 3 to 5 technical interview questions assessing beginner to advanced knowledge.
        Only return the questions as a numbered list.
        """
        response = conversation.predict(input=tech_prompt)
        questions = [q.strip() for q in response.split("\n") if q.strip()]
        st.session_state.tech_questions = questions
        st.session_state.collecting_tech_answers = True
        st.session_state.stage = "tech_questions"
        st.session_state.data["Generated Questions"] = questions
        st.session_state.data["Tech Q&A"] = []

    elif stage == "tech_questions":
        index = st.session_state.current_question_index
        st.session_state.data["Tech Q&A"].append({
            "question": st.session_state.tech_questions[index],
            "answer": user_input
        })
        if index + 1 < len(st.session_state.tech_questions):
            st.session_state.current_question_index += 1
        else:
            st.session_state.stage = "done"
            save_to_csv({
                **st.session_state.data,
                "Tech Q&A": str(st.session_state.data["Tech Q&A"])
            })
            bot_reply = "Thanks! We've recorded all your answers. We'll get back to you soon."
            st.session_state.chat_history.append(("bot", bot_reply))
            st.rerun()

    if st.session_state.stage == "tech_questions":
        q_idx = st.session_state.current_question_index
        bot_reply = st.session_state.tech_questions[q_idx]

    st.session_state.chat_history.append(("bot", bot_reply))
    st.rerun()

# Display chat
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)
