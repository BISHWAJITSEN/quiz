import random


def load_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
            "correct_answer": "C"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A. Earth", "B. Venus", "C. Jupiter", "D. Mars"],
            "correct_answer": "C"
        },
        # Add more questions here
    ]
    return questions


def play_quiz():
    score = 0
    questions = load_quiz()
    random.shuffle(questions)  # Shuffle the order of questions

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your choice (A, B, C, or D): ").strip().upper()

        if user_answer == q["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {q['correct_answer']}")

    return score


def main():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions.")

    play_again = "yes"

    while play_again.lower() == "yes":
        score = play_quiz()
        print(f"Your Score: {score}/{len(load_quiz())}")
        play_again = input("Do you want to play again? (yes/no): ")

    print("Thank you for playing!")


if __name__ == "__main__":
    main()
