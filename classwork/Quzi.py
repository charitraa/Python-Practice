quiz = [(
    "what is capital of france?",
    "c",
    ["a) LONDON",
     "b) Berlin",
     "c) Paris",
     "d) Rome"]),
    (
    "what is 2+2?",
    "b",
    ["a) 3",
     "b) 4",
     "c) 5",
     "d) 6"]),
    (
    "what is the largest planet in our solar system?",
    "d",
    ["a) Earth",
     "b) Mars",
     "c) Venus",
     "d) Jupiter"]),
    (
    "what wrote Romeo and Juliet?",
    "c",
    ["a) Charles Dickens",
     "b) Jane Austen",
     "c) Willian Shakespeare",
     "d) MArk Twain"]),

]

# function to run the quiz


def run_quiz(quiz):
    score = 0
    for question, correctAnswer, options in quiz:
        print(question)
        for option in options:
            print(option)
        userAnswer = input("Enter the correct answer (e.g :, 'a','b','c','d')")
        if userAnswer == correctAnswer:
            print('correcr!\n')
            score += 1
            print(f"CORRECT,the correct answer is {correctAnswer}\n")
    return score


# main progresss
if __name__ == "__main__":
    print("Welcome to simple quiz \n")
    totalQuestion = len(quiz)
    user_score = run_quiz(quiz)
    print(f"you got {user_score} out of {totalQuestion} questions correct.")
    percentage = (user_score/totalQuestion)*100
    print(f"your score is {percentage}%")
