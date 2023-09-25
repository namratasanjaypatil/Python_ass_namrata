string = input('Enter a string : ')

def palindrome(string):
    if string == string[len(string)::-1]:
        print(string,'is a palindrome string')
    else:
        print(string,'is not a palindrome string')
    
palindrome(string)