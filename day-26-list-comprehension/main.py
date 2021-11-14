import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# with open("nato_phonetic_alphabet.csv") as alphabet:
#     print(alphabet)

df = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

full_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(full_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

entry = input("Please enter a word to convert to the phonetic alphabet: ").upper()
converted_entry = [full_dict[letter] for letter in entry]
print(converted_entry)
