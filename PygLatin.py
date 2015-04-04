word = raw_input("Input a word in English: ")

list_of_characters = list(word)
last_position = len(word)-1
first_letter = word[0];
last_letter = word[last_position]

list_of_characters[0] = last_letter
list_of_characters[last_position] = first_letter

pigable = ''.join(list_of_characters) + 'ay'
print pigable