def mad_lib():
    print("welcome")
    noun = input("Enter a noun:")
    verb = input("Enter a verb:")
    adjective = input("Enter an adjective:")
    place = input("Enter a place:")

    story = f"One day a {adjective} {noun} decided to {verb} to the {place}."
    print(story)
    print("Here is your story")

mad_lib()