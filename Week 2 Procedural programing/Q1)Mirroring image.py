def mirror(str):
    revAlphabets="zyxwvutsrqponmlkjihgfedcba"
    l=len(str)
    answer=""
    for i in range(0,l):
         answer = (answer +revAlphabets[ord(str[i]) - ord('a')])
    return answer

str=input("Enter string to be mirrored:")
answer=mirror(str)
print(answer)
    

