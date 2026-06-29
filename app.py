import streamlit as st
from quiz_chain import generate_quiz
from history import save_quiz, view_history

st.set_page_config(page_title="AI Quiz Builder", layout="centered")

st.title(" AI Quiz Builder (RAG + FAISS)")

if "quiz" not in st.session_state:
    st.session_state.quiz = None

if "answers" not in st.session_state:
    st.session_state.answers = []


menu = st.sidebar.radio("Menu", ["Take Quiz", " View History"])

if menu == " View History":
    st.subheader("Quiz History")
    view_history()
    st.stop()

topic = st.text_input("Enter Topic")

if st.button("Generate Quiz") and topic.strip():

    with st.spinner("Generating quiz..."):
        st.session_state.quiz = generate_quiz(topic)
        st.session_state.answers = []


if st.session_state.quiz:

    quiz = st.session_state.quiz

    st.subheader(" Quiz")

    for i, q in enumerate(quiz.questions):

        st.markdown(f"### Q{i+1}: {q.question}")

        options = ["A", "B", "C", "D"]

        answer = st.radio(
            "Select answer:",
            options,
            key=f"q_{i}"
        )

        if len(st.session_state.answers) < len(quiz.questions):
            st.session_state.answers.append(answer)
        else:
            st.session_state.answers[i] = answer

        st.write("---")


if st.session_state.quiz and st.button("Submit Quiz"):

    quiz = st.session_state.quiz
    answers = st.session_state.answers

    score = sum(
        1 for i, q in enumerate(quiz.questions)
        if answers[i] == q.correct_answer
    )

    total = len(quiz.questions)

    if score == total:
        feedback = "Perfect score! "
    elif score >= 4:
        feedback = "Excellent! "
    elif score >= 3:
        feedback = "Good job "
    else:
        feedback = "Keep practicing "

    st.success(f"Score: {score}/{total}")
    st.info(feedback)

   
    save_quiz(
        quiz,
        answers,
        score,
        total,
        feedback
    )

    st.subheader(" Review")

    for i, q in enumerate(quiz.questions):

        st.markdown(f"### Q{i+1}")
        st.write(q.question)

        st.write(f"Your Answer: {answers[i]}")
        st.write(f"Correct Answer: {q.correct_answer}")
        st.write(f"Explanation: {q.explanation}")

        if answers[i] == q.correct_answer:
            st.success("Correct ")
        else:
            st.error("Wrong ")

        st.write("---")
