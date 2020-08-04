
import random


def validate_input(guessed_letters):

    while True:
        my_guess = input("Your guess: ")
        if not my_guess.isalpha():
            print("enter only a LETTER!")
        elif len(my_guess) > 1:
            print("enter only a SINGLE letter!")
        elif my_guess in guessed_letters:
            print("you already guessed that letter!")
        else:
            break

    guessed_letters += my_guess
    return my_guess, guessed_letters


def main():
    with open("words_to_guess.txt", "r") as f:
        words = f.read().split()

    guess_this_word = random.choice(words).lower()
    l = len(guess_this_word)
    unfinished_word_list = list("_" * l)
    unfinished_word_string = ''.join(unfinished_word_list)
    guessed_letters = ''

    attempts = 8
    while attempts != 0:
        print("\n", unfinished_word_string)
        try_again = True

        my_guess,guessed_letters = validate_input(guessed_letters)

        for i in range(l):
            if guess_this_word[i] == my_guess:
                unfinished_word_list[i] = my_guess
                unfinished_word_string = ''.join(unfinished_word_list)
                try_again = False
        if try_again:
            attempts -= 1
            print(f"{attempts} attempts remaining")
            print("Try again")
        if guess_this_word == unfinished_word_string:
            print(f"You won! The word was {guess_this_word}")
            exit(1)
    print(f"Too many guesses, the word was {guess_this_word}!")


main()
