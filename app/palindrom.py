# str = input("Enter a String:")

def is_palindrome(str):
    return str.lower() == str[::-1].lower()