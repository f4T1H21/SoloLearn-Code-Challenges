"""
That's odd...

You want to take a list of numbers and find the sum of all of the even numbers in the list. Ignore any odd numbers. 
 
Task: 
Find the sum of all even integers in a list of numbers. 
 
Input Format:  
The first input denotes the length of the list (N). The next N lines contain the list elements as integers. 
 
Output Format:  
An integer that represents the sum of only the even numbers in the list. 
 
Sample Input:  
9 
1 
2 
3 
4 
5 
6 
7 
8 
9 
 
Sample Output:  
20
"""

import random

nums = int(input())

if random.randrange(0,2,1) == 0:
    #This list is created using lambda with a generator inside a filter.
    evens = list(filter(lambda x: x%2==0, (int(input()) for i in range(nums))))

else: #If the result of randrange is 1
    #This list is created using list comprehension and walrus.
    evens = [num for i in range(nums) if (num := int(input())) %2 == 0]

print(sum(evens))