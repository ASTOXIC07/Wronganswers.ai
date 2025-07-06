# main.py – WrongAnswer.AI 🚫✅
# Learn from your mistakes like a real AI
# Built with Python + Streamlit

import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="WrongAnswer.AI", layout="centered")
st.title("🤖 WrongAnswer.AI – Learn from Your Mistakes")

st.markdown("""
Track your wrong answers, understand your mistake patterns, and avoid repeating them — just like an AI learning from failures.
""")

# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = []

# --- Input Form ---
st.subheader("✍️ Log a Mistake")

subject = st.selectbox("Subject", ["Maths", "Physics", "Chemistry", "Biology", "English", "Other"])
question = st.text_area("What was the question?")
mistake_type = st.selectbox("Type of Mistake", ["Concept Confusion", "Careless", "Misread", "Guessing", "Forgot"])
correct_answer = st.text_input("What was the correct answer?")
your_reason = st.text_input("Why did you make this mistake?")

if st.button("➕ Save Mistake"):
    st.session_state.data.append({
        "Date": datetime.date.today(),
        "Subject": subject,
        "Question": question,
        "Mistake Type": mistake_type,
        "Correct Answer": correct_answer,
        "Your Reason": your_reason
    })
    st.success("📌 Mistake saved successfully!")

# --- Analysis Section ---
if st.session_state.data:
    st.subheader("📊 Mistake Analytics")

    df = pd.DataFrame(st.session_state.data)

    st.markdown("### 🔢 Mistake Types")
    st.bar_chart(df["Mistake Type"].value_counts())

    st.markdown("### 📚 Subject-wise Mistakes")
    st.bar_chart(df["Subject"].value_counts())

    st.markdown("### 🕓 Recent Mistakes")
    st.dataframe(df.tail(5), use_container_width=True)

    # Download option
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download Mistake Log", csv, "wrong_answers.csv", "text/csv")
else:
    st.info("No mistakes logged yet. Start by adding one above ⬆️")
