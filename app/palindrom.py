# str = input("Enter a String:")

def is_palindrome(str):
    str1 = str.lower().replace(" ","") 
    return str1 == str1[::-1]
