def multiplicate_table():
    number = int(input("Enter a number to generate its multiplications: "))
    limit = int(input("Enter the limit you want to go up to: "))

    print(f"Multiplication for {number}")
    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

multiplicate_table()