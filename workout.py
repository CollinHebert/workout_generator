import random

def workout_generator():
    greeting = input("Welcome to Workout Routine Generator! Choose your workout type (cardio/strength/flexibility): ").lower()

    strength = ["Push-ups", "Squats", "Lunges", "Plank", "Dumbbell Press"]
    cardio = ["Jumping Jacks", "Burpees", "Running in Place", "Jump Rope", "High Knees"]
    flexibility = ["Yoga Stretch", "Hamstring Stretch", "Toe Touches", "Cat-Cow Stretch", "Shoulder Rolls"]

    #Here, I had the right idea. Finish it out with if statements.. I just didn't know how to execute it.
    #The == operator in Python is the equality operator. It checks if two values are equal and returns True if they are, otherwise, it returns False.
    #random.choice() is a function from Python’s built-in random module. It selects and returns a random item from a given sequence, such as a list, tuple, or string.
    if greeting == "strength":
        workout = random.choice(strength)

    elif greeting == "cardio":
        workout = random.choice(cardio)

    elif greeting == "flexibility":
        workout = random.choice(flexibility)

    else:
        print("Please enter your desired workout again: ")
        return
    print(f"Your workout is: {workout}")

workout_generator()
#this is a test to fix commit 2