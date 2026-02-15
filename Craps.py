import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"Player rolled {die1} + {die2} = {total}")
    return total

def play_game():
    first_roll = roll_dice()

    if first_roll in [7,11]:
        print("You Win1")
    elif first_roll in [2, 3, 12]:
        print("Casino wins1 (Craps)")
    else:
        goal =first_roll
        print(f"Goal number is {goal}")

        while True:
            current_roll = roll_dice()
            if current_roll == goal:
                print("You rolled the goal number1 You win!")
                break
            elif current == 7:
                print("You rolled a 7! You lose.")

                break

            play_game()

