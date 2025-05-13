def word_counter():
    text = input("Enter text: ").strip()
    words = text.split()
    word_count = len(words)
    char_count = len(text)

    print(f"Word count: {word_count}")
    print(f"Character count: {char_count}")

word_counter()