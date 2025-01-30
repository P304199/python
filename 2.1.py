#program to capitalize alternate letters of word

#alternate capitalization

def capitalize_alternate_letters(word):
    result = []
    for i, char in enumerate(word):
        if i % 2 == 0:
            result.append(char.upper())  
            result.append(char.lower())  
    return ''.join(result)

# function
word = input("Enter a word: ")
result_word = capitalize_alternate_letters(word)
print("Result:", result_word)