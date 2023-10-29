
# Define a list of true/false questions and answers as tuples (question, correct answer)
true_false_quiz = [
    ("The Earth is flat.", False),
    ("The capital of France is Paris.", True),
    ("Python is a compiled language.", False),
    ("Water boils at 100 degrees Celsius at sea level.", True),
    ("The moon is made of cheese.", False),
    ("The sun rises in the west.", False),
]

# Function to run the true/false quiz


def run_true_false_quiz(quiz):
    score = 0

    for question, correct_answer in quiz:
        print(question)
        user_answer = input(
            "True or False? (Enter 'T' or 'F'): ").strip().lower()

        if (user_answer == "t" and correct_answer) or (user_answer == "f" and not correct_answer):
            print("Correct!\n")

            score += 1
        else:
            print("Wrong!\n")

    return score


# Main program
if __name__ == "__main__":
    print("Welcome to the True/False Quiz!\n")
    total_questions = len(true_false_quiz)
    user_score = run_true_false_quiz(true_false_quiz)

    print(f"You got {user_score} out of {total_questions} questions correct.")
    percentage = (user_score / total_questions) * 100
    print(f"Your score is {percentage}%.")
