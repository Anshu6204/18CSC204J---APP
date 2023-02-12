def isPalindrome():
    str=input("Enter a string:")
    rev= str[::-1]
    if(str==rev):
        return 1
    else:
        return 0

if(isPalindrome()):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")