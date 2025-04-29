import os
import random


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    """
    main counts how many vowels and consonants are present, and displays both counts.

    Returns:
        Nothing
    """
    # sentence = "This is a sample string that will be used for counting vowels and consonants."
    sentence = "How many vowels and consonants are in this sentence?"

    vowels = "aeiou"
    consonants = "qwrtypsdfghjklzxcvbnm"

    vowels_counter = 0
    consonants_counter = 0
    other_symbols_counter = 0

    for c in sentence:
        if c.lower() in vowels:
            vowels_counter += 1
        elif c.lower() in consonants:
            consonants_counter += 1
        else:
            other_symbols_counter += 1

    print(f"The sentence has {len(sentence)} characters")
    print(f"The number of vowels in the string is: {vowels_counter}")
    print(f"The number of consonants in the string is: {consonants_counter}")
    print(f"The number of other symbols in the string is: {other_symbols_counter}")


if __name__ == "__main__":
    cls()
    main()
