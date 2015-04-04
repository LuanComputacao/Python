pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first = word[0]
    last = word[len(word)]
    new_word = last + word[1:(len(word) - 1)] + last + pyg
    print new_word
else:
    print 'empty'