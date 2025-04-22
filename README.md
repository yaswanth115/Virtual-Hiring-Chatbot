# TalentScout - Virtual Hiring Assistant

---

## Project Overview

**TalentScout** is an AI-powered hiring assistant chatbot developed using **Streamlit**, **LangChain**, and **Groq's LLaMA 3** model. It engages candidates in a natural conversation to collect essential information (name, contact, experience, location, etc.) and dynamically generates technical questions based on the candidate’s tech stack. The interaction is stored in a CSV file (or can be extended to use a database) for recruiters to review later.

This chatbot streamlines the initial screening process and provides a smart, friendly experience for candidates.

---

## ⚙️ Installation Instructions

Follow the steps below to set up and run the project locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/virtual-hiring-chatbot.git
   cd virtual-hiring-chatbot
2. **Create and Activate Virtual Environment**
   ```
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
4. **Set Up the Environment Variables**
   ```
   GROQ_API_KEY=gsk_your_actual_groq_api_key_here
5. **Run the Application**
   ```bash
   streamlit run app.py

---
##  Usage Guide
1. Launch the app using Streamlit.
2. The chatbot will greet the user and begin asking for:
   - Full Name
   - Email
   - Phone Number
   - Year of Experience
   - Postion Applied for
   - Location
   - Tech Stack
3. Based on the tech stack provided, the bot generates and asks technical questions one at a time.
4. After the user responds to all questions or exits, their details are saved in candidates.csv.



