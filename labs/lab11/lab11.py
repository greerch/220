from random import randint

"""
Name: Caroline Greer
lab11.py

Discription: Create a hangman game

Certification of authenticity:
I certify that this assignment is entirely my own work
"""

def file_words():
    file = open("wordlist.txt", "r")
    words = file.readlines()
    file.close()
    return words


def pick_word(words):
    move = randint(0, len(words) - 1)
    return words[move]


def guessed_letters(chosen, guess, acc, count):
    marker = False
    chosen = chosen.lower()
    for i in range(len(chosen)):
        if chosen[i] == guess:
            acc[i] = guess
            marker = True
    if marker:
        return "" .join(acc)
    else:
        return count + 1


def finished_game(acc):
    for i in range(len(acc)):
        if acc[i] == "_":
            return False
    return True


def play():
    file_words()
    words = file_words()
    chosen = pick_word(words)
    acc = list()
    for i in range(len(chosen)):
        acc.append("_")
    used_letters = list()
    count = 0
    guessed_words = acc
    while not finished_game(acc):
        if count <= 7:
            guess = input("what letter are you guessing?")
            holder = guessed_letters(chosen, guess, acc, count)
            if str(holder).isnumeric():
                if guess in used_letters:
                    count = count
                else:
                    count = holder
            else:
                guessed_words = holder
            print("".join(guessed_words))
            used_letters.append(guess)
            print("the amount of wrong tries you have attempted is " + str(count) + " out of 7")
            print("the letters you have already tried are: ", "," .join(used_letters))
        else:
            print("you stink, sorry!")
            return
    else:
        print("winner winner!")
        return


def main():
    print("Welcome to hangman! We are generating your word them we are good to go!")
    play()
    pass
main()
