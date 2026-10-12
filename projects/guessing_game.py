"""Mini Projects — guessing_game.py

Part of Python Beginner Guide: https://github.com/MehvishKiani/Python-beginner-guide
"""
import random


def guessing_game(low=1, high=100, max_tries=7, seed=None):
    rng = random.Random(seed)
    secret = rng.randint(low, high)
    print(f"I'm thinking of a number between {low} and {high}. You have {max_tries} tries.")

    for attempt in range(1, max_tries + 1):
        try:
            guess = int(input(f"Attempt {attempt}: "))
        except ValueError:
            print("Numbers only, please!")
            continue

        if guess < secret:
            print("Too low ⬇️")
        elif guess > secret:
            print("Too high ⬆️")
        else:
            print(f"🎉 Correct! You got it in {attempt} {'try' if attempt == 1 else 'tries'}.")
            return True
    print(f"😢 Out of tries. The number was {secret}.")
    return False


if __name__ == "__main__":
    guessing_game(seed=3)
