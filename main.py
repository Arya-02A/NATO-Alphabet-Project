import pandas

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("F:/Arya all/Python/angela yu 100 day cource/day 30/NATO-alphabet-start/nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonatic():
    word = input("Enter a word : ").upper()
    try:
        list_of_code = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the word please.")
        generate_phonatic()
    else:
        print(list_of_code)

generate_phonatic()