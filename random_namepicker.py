import random

def name_picker():
    names = input("Enter names separated by commas: ").split(",")
    random_name = random.choice([name.strip() for name in names])
    print(f"Randomly selected name: {random_name}")

name_picker()