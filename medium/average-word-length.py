"""
Average Word Length

You are in a college level English class, your professor wants you to write an essay, but you need to find out the average length of all the words you use. It is up to you to figure out how long each word is and to average it out. 
 
Task:  
Takes in a string, figure out the average length of all the words and return a number representing the average length. Remove all punctuation. Round up to the nearest whole number. 
 
Input Format:  
A string containing multiple words. 
 
Output Format:  
A number representing the average length of each word, rounded up to the nearest whole number. 
 
Sample Input:  
this phrase has multiple words 
 
Sample Output:  
6
"""

import string

def roundup(x: float):
    if int(str(x).split(".")[1]) == 0:
        return int(x)

    else:
        return int(x) + 1

text = input()

newtext = text.translate(str.maketrans('', '', string.punctuation))

words = newtext.split()

averagelen = sum(map(len, words))/len(words)

print(roundup(averagelen))