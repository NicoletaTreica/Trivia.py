import random

# be able to:
#   1. display a question
#   2. show answer optoions
#   3. allow me to input an answer
#   4. tell me if my guess is correct or incorrect
#   5. do this with all the questions
#   6. display my score
#   7. ask me if I want to play again


# Defining our classes such as new_game, checking_answers, displaying_score, play_game_again
# class question to create self.question and multiple questions (multiple instances),
#  each question will have attributes (these are instances too) such as ABCD and which the correct answer is
# self, question, choice correct answer


# the attributes of every question are outlined
# first we will get the question, then the choiced (ABCD) and then we will be told which is the correct answer
class Question:
    def __init__(self, question: str, choice: str, correct_answer: str) -> None:
        self.question = question
        self.choice = choice
        self.correct_answer = correct_answer


# This is an instance to the Question class
# An instance holds the value of the attributes and then allows you to reuse
# eg different questions under the name questions
question_1 = Question(
    "what is the capital of France?",
    ["A. London", "B. Paris", "C. Valletta", "D. Copenhagen"],
    "B",
)

question_2 = Question(
    "How many continents are there on Earth?",
    ["A. 7", "B. 3", "C. 4", "D. 9"],
    "A",
)

question_3 = Question(
    "Which planet is closest to the Sun?",
    ["A. Mercury", "B. Earth", "C. Jupiter", "D. Mars"],
    "A",
)

question_4 = Question(
    "What is the symbol for Hydrogen in the periodic table?",
    ["A. Li", "B. He", "C. Sr", "D. H"],
    "D",
)

# this is a list that contains all of the instances
# random.shuffle makes the questions print randomly
question_list = [question_1, question_2, question_3, question_4]
random.shuffle(question_list)

# then we put it in a while true loop so that it starts again if we want it to
# and before it shows the questions again it resets the score to 0
# then it prints the attributes of the instances (eg choice)
while True:
    score = 0
    # x could be any value and it represents the values inside the list
    for x in question_list:
        # this prints the question_1 question_2... because x is the questions in the list and question is the class
        print(f"question: {x.question}")
        # \n puts the choices on different lines
        question_choices = "\n    - ".join(x.choice)
        print(f"    - {question_choices}")

        user_guess = input("Choose A/B/C/D: ")

    # supper is called
    if user_guess.upper() == x.correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

        print(f"The correct answer is: {x.correct_answer}")
    # this allows us to print the final score by printing the variable that holds the score
    print(f"Your final score is: {score}")
    # this breaks the loop or continues it based on user input
    play_again = input(
        "Type 'yes' if you would like to play again and 'no' if you would like to quit: "
    )
    if play_again.lower() == "no":
        print("Thank you for playing!")
        break
    elif play_again.lower() == "yes":
        continue
