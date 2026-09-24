"""
Craps Dice Game

Rules:
- Roll two dice.
- If the sum is 7 or 11 on the first roll -> player wins.
- If the sum is 2, 3, or 12 on the first roll (craps) -> casino wins.
- Otherwise, the sum (4, 5, 6, 8, 9, or 10) becomes the "goal" number.
  The player keeps rolling until they either roll the goal number again
  (player wins) or roll a 7 (player loses).
"""

import random


def roll_dice():
    """Roll two dice and return their sum."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"You rolled {die1} + {die2} = {total}")
    return total


def play_game():
    """Play one full round of craps and print the result."""
    print("Rolling the dice for the first time...")
    first_roll = roll_dice()

    if first_roll == 7 or first_roll == 11:
        print("You win! 🎉")
        return
    elif first_roll in (2, 3, 12):
        print("Craps! The casino wins.")
        return
    else:
        goal = first_roll
        print(f"Your goal number is now {goal}.")
        print("Keep rolling until you hit the goal number or a 7...")

        while True:
            current_roll = roll_dice()

            if current_roll == goal:
                print("You hit your goal number! You win! 🎉")
                break
            elif current_roll == 7:
                print("You rolled a 7 before your goal. You lose.")
                break
            # otherwise, keep rolling


def main():
    print("=== Welcome to Craps! ===")
    play_game()

    while True:
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again == "y":
            print()
            play_game()
        elif again == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()