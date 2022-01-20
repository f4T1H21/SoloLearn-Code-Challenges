"""
Military Time

You want to convert the time from a 12 hour clock to a 24 hour clock. If you are given the time on a 12 hour clock, you should output the time as it would appear on a 24 hour clock.   
 
Task:   
Determine if the time you are given is AM or PM, then convert that value to the way that it would appear on a 24 hour clock. 
 
Input Format:  
A string that includes the time, then a space and the indicator for AM or PM. 
 
Output Format:  
A string that includes the time in a 24 hour format (XX:XX) 
 
Sample Input:  
1:15 PM 
 
Sample Output:  
13:15
"""

import re

clock_tvelwe = str(input())

def convert(clock):
    pattern = r"([0-1][0-9])\:([0-5][0-9]) ([A,P])M"
    match = re.match(pattern, clock)
    if match.group(3) == "A":
        if match.group(1) == "12":
            return "00:"+ match.group(2)
        else:
            return clock[:-2]

    elif match.group(3) == "P":
        if match.group(1) == "12":
            return clock[:-2]
        else:
            return str(int(match.group(1)) + 12) + ":" + match.group(2)

print(convert(clock_tvelwe))