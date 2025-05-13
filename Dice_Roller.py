import random

def dice_roller():
    print("Welcome to the Dice Roller!")
    dice_count = int(input("How many dice do you want to roll? "))
    results = [random.randint(1, 6) for _ in range(dice_count)]
    print(f"You rolled: {', '.join(map(str, results))}")
    print(f"Total: {sum(results)}")

dice_roller()