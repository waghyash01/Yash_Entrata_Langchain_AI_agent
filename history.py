from datetime import datetime
import streamlit as st
from datetime import datetime

FILE = "quiz_history.txt"


def save_quiz(quiz, user_answers, score, total, feedback):

    with open(FILE, "a", encoding="utf-8") as f:

        f.write("\n" + "=" * 80 + "\n")
        f.write(f"DATE: {datetime.now()}\n")
        f.write(f"SCORE: {score}/{total}\n")
        f.write(f"FEEDBACK: {feedback}\n")

        for i, q in enumerate(quiz.questions):

            f.write(f"\nQ{i+1}: {q.question}\n")
            f.write(f"A: {q.options.A}\n")
            f.write(f"B: {q.options.B}\n")
            f.write(f"C: {q.options.C}\n")
            f.write(f"D: {q.options.D}\n")

            f.write(f"Your Answer: {user_answers[i]}\n")
            f.write(f"Correct Answer: {q.correct_answer}\n")
            f.write(f"Explanation: {q.explanation}\n")

            f.write("-" * 60 + "\n")



FILE = "quiz_history.txt"


def view_history():

    try:
        with open(FILE, "r", encoding="utf-8") as f:
            data = f.read()

        if data.strip():
            st.text_area("Quiz History", data, height=500)
        else:
            st.warning("No history found yet.")

    except FileNotFoundError:
        st.error("No history file found yet. Take a quiz first!")
