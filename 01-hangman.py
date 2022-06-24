import sys

no_of_tries = 5
word = "kamila"
used_letters = []

user_word = []


def find_indexes(word: str, letter: str):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def show_state_of_game():
    print()
    print(user_word)
    print("Attempt left:", no_of_tries)
    print("Letters used:", used_letters)
    print()


for _ in word:
    user_word.append("_")

while True:
    letter = input("Enter a letter: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("There is no such letter.")
        no_of_tries -= 1

        if no_of_tries == 0:
            print("End of the game :(")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print("Bravo, that's the word!")
            sys.exit(0)

    show_state_of_game()
