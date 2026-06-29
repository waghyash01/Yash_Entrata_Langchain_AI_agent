from quiz_chain import generate_quiz
from history import save_quiz, view_history


def get_option_text(q, option):
    return {
        "A": q.options.A,
        "B": q.options.B,
        "C": q.options.C,
        "D": q.options.D,
    }.get(option, "")


def main():
    print("=" * 60)
    print(" AI Quiz Builder")
    print("=" * 60)

    print("\n1. Take New Quiz")
    print("2. View Quiz History")

    choice = input("\nChoose an option (1/2): ").strip()

    if choice == "2":
        view_history()
        return

    elif choice != "1":
        print(" Invalid choice.")
        return

    topic = input("\nEnter Topic: ").strip()

    while not topic:
        topic = input(" Topic cannot be empty. Enter Topic: ").strip()

    print("\nGenerating Quiz... Please wait.\n")

    quiz = generate_quiz(topic)

    score = 0
    user_answers = []

    for i, q in enumerate(quiz.questions, start=1):

        print("\n" + "=" * 60)
        print(f"Question {i} of {len(quiz.questions)}")
        print("=" * 60)

        print(q.question)
        print()

        print(f"A. {q.options.A}")
        print(f"B. {q.options.B}")
        print(f"C. {q.options.C}")
        print(f"D. {q.options.D}")

        while True:
            answer = input("\nSelect an option (A/B/C/D): ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print(" Invalid input.")
            print("Please enter only A, B, C or D.")

        user_answers.append(answer)

        if answer == q.correct_answer:
            score += 1

    total_questions = len(quiz.questions)

    print("\n")
    print("=" * 60)
    print("🎉 QUIZ COMPLETED")
    print("=" * 60)

    print(f"\n You answered {score}/{total_questions} questions correctly!")

    if score == total_questions:
        feedback = "Outstanding! Perfect score! 🎉"
    elif score >= 4:
        feedback = "Excellent work! You have a strong understanding of the topic. "
    elif score == 3:
        feedback = "Good job! You know the basics, but there's room for improvement. "
    elif score == 2:
        feedback = "Nice effort! Consider reviewing the topic and trying again. "
    else:
        feedback = "Keep practicing! Every quiz is an opportunity to learn. "

    print(f" Feedback: {feedback}")

    save_quiz(
        topic,
        score,
        total_questions,
        feedback,
        quiz,
        user_answers,
    )


    # BONUS 3: Improved Quiz Review
  
    print("\n" + "=" * 70)
    print("📖 Detailed Quiz Review (Why answers were correct/incorrect)")
    print("=" * 70)

    for i, q in enumerate(quiz.questions):

        print(f"\nQuestion {i+1}")
        print(q.question)
        print()

        user_ans = user_answers[i]
        correct_ans = q.correct_answer

        print(f"Your Answer    : {user_ans} - {get_option_text(q, user_ans)}")
        print(f"Correct Answer : {correct_ans} - {get_option_text(q, correct_ans)}")

        if user_ans == correct_ans:

            print("\n✅ Correct!")
            print("Reason: Your answer matches the correct concept.")
        else:

            print("\n❌ Incorrect.")
            print("Why it is wrong:")
            print(f"- You selected: {get_option_text(q, user_ans)}")
            print(f"- Correct is : {get_option_text(q, correct_ans)}")

        print("\n📘 Explanation:")
        print(q.explanation)

        print("-" * 70)

    print("\n📝 Complete quiz history has been saved.")
    print("Thank you for using AI Quiz Builder! 👋")


if __name__ == "__main__":
    main()