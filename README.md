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

---
## Technical Details
### Libraries Used
- **Streamlit** - Web Interface
- **LangChain** - Framework for managing LLM interactions and memory
- **Langchain_groq** - LLaMA 3 integration via Groq API
- **Pandas** - CSV data storage
- **Dotenv** - Secure environment variable management

### Model Used
- **LLaMA 3** by Meta, served through **Groq API** (llama-3-8b or llama-3.3-70b-versatile)
---
## Prompt Design
Prompt engineering plays a key role in the project. The following strategies were used:
- **Contextual Instructions**:
  ```Example:
  You are an expert tech interviewer. Based on the following tech stack: {user_input},
  generate 3 to 5 technical questions that test different levels of experience.

---
## Challenges & Solutions
### Technical Questions Flow
- **Challenge** - LLaMA generated all questions at once.
- **Solution** - Parsed the generated text and displayed questions one at a time using session state.
### Deployment Errors
- **Challenge** - Errors due to missing environment variables or modules on Streamlit Cloud.
- **Solution** - Added requirements.txt, .env management, and set secrets via Streamlit Cloud settings.

--
## Deployment Guide
- Push your project to GitHub.
- Go to [Streamlit Cloud](https://streamlit.io/cloud)
- Click "**New app**", choose your repo and branch.
- Set app.py as the main file.
- Add your GROQ_API_KEY under **Secrets**.
-Click **Deploy** – You’ll get a live link to share!


  
  





