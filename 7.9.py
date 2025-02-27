import re

def hindi_tokenizer(text):
    # Unicode block for Hindi characters 
    hindi_regex = r'[\u0900-\u097F]+'  

    # Regular expression for punctuations
    punctuation_regex = r'[.,!?;:(){}[\]"\'<>@#%&*+=~_/\\|`^$]'

    # Regular expression for matching dates 
    date_regex = r'\b(?:\d{2}[-/]\d{2}[-/]\d{4}|\d{4}[-/]\d{2}[-/]\d{2})\b'

    # Regular expression for matching URLs 
    url_regex = r'\b(?:https?://[^\s]+)\b'

    # Regular expression for matching emails
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    # Regular expression for matching numbers 
    number_regex = r'\b(?:\d{1,3}(?:,\d{3})*(?:\.\d+)?|\d+(?:/\d+)?|\d+\.\d+)\b'

    # Regular expression for matching social media usernames 
    username_regex = r'@\w+'

    # Combining all regex into one
    combined_regex = f"({hindi_regex}|{punctuation_regex}|{date_regex}|{url_regex}|{email_regex}|{number_regex}|{username_regex})"
    
    # Using findall to get all tokens
    tokens = re.findall(combined_regex, text)

    return tokens

# input 
text = input("Enter a sentence or text in Hindi (with dates, URLs, emails, numbers, etc.): ")

# Tokenize 
tokens = hindi_tokenizer(text)


print("Tokens:")
print(tokens)
