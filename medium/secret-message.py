"""
Secret Message

You are trying to send a secret message, and you've decided to encode it by replacing every letter in your message with its corresponding letter in a backwards version of the alphabet.  
What do your messages look like? 
 
Task:  
Create a program that replaces each letter in a message with its corresponding letter in a backwards version of the English alphabet. 
 
Input Format:  
A string of your message in its normal form. 
 
Output Format:  
A string of your message once you have encoded it (all lower case). 
 
Sample Input:  
Hello World 
 
Sample Output:  
svool dliow
"""

import string

msg = input()
en = list(string.ascii_lowercase)

chars = [i for i in msg]

def revposition(letter):
    if letter == " ":
        return " "
    index = en.index(letter.lower())
    max = len(en)-1 # Maximum index for list
    return "".join(en[max-index:max+1-index])

encoded = "".join(revposition(c) for c in chars)
print(encoded)