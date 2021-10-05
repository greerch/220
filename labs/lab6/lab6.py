"""
Name: Caroline Greer
lab6.py

Discription: Solve the problems for lab 6

Certification of authenticity:
I certify that this assignment is entirely my own work
"""

def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter name in first-last order: ")
    name_split = name.split()
    print(name_split[1], ',', name_split[0]) # how can I make there not be a space

def company_name():
    domain = input("Enter a three-part internet domain name: ")
    domain_split = domain.split('.')
    print(domain_split[1])

def initials():
    number_names = eval(input("Enter the number of names that will be entered: "))
    for i in range(number_names):
        first_name = input("Enter the first name of student " + str(number_names) + ":" )
        last_name = input("Enter " + str(first_name) + "'s last name:")
        print(first_name + "'s initials are " + first_name[0] + last_name[0])

def names():
    list_of_names = input("Enter people's names, separated by commas: ")
    individual_names = list_of_names.split(',')
    print("The initials are ", end="")
    for i in range(len(individual_names)):
        name_order = individual_names[i].split()
        first_name = name_order[0]
        last_name = name_order[1]
        initials = first_name[0] + last_name[0]
        print(initials, end=" ")

def thirds():
    number_sentences = eval(input("How many sentences will be entered: "))
    enter_sentences = input("Print " + str(number_sentences) + " sentences: ")
    for num in range(2, len(enter_sentences), 3):
        characters = len(enter_sentences)
        print(enter_sentences[num], end="")

def word_average():
    number_sentences = eval(input("How many sentences will be entered: "))
    for i in range(number_sentences):
        sentence = input("Enter a sentence: ")
        word_count = sentence.split()
        num_words = len(word_count)
        character_count = 0
        for words in word_count:
             character_count = character_count + len(words)
        average = character_count / num_words
        print("The word average is: ", average)

def pig_latin():
    original_sentence = input("Enter a sentence to convert: ")
    original_sentence = original_sentence.lower()
    sentence_split = original_sentence.split()
    for element in sentence_split:
        body = element[1:]
        end = element[0]
        print(body + end + "ay", end=" ")


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()

main()
