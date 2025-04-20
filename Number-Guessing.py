import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input("🔢 Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("📉 Too low! Try again.")
        elif guess > number_to_guess:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break
    else:
        print(f"😢 Sorry, you've run out of tries. The number was {number_to_guess}.")

number_guessing_game()
