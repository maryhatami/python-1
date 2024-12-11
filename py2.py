import random

def ask_question():
    # Randomly choose addition or subtraction
    operation = random.choice(['+', '-'])
    
    # Generate two random numbers
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Print the problem
    print(f"What is {num1} {operation} {num2}?")
    
    # Get the user's answer
    answer = int(input("Your answer: "))
    
    # Check if the answer is correct
    if operation == '+':
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2

    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")

# Run the quiz
ask_question()
