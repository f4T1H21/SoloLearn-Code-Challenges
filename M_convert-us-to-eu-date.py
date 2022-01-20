"""
Convert US to EU date

You and your friends are going to Europe! You have made plans to travel around Europe with your friends, but one thing you need to take into account so that everything goes according to play, is that the format of their date is different than from what is used in the United States. Your job is to convert all your dates from MM/DD/YYYY to DD/MM/YYYY. 
 
Task:  
Create a function that takes in a string containing a date that is in US format, and return a string of the same date converted to EU. 
 
Input Format:  
A string that contains a date formatting 11/19/2019 or November 19, 2019. 
 
Output Format:  
A string of the same date but in a different format: 19/11/2019. 
 
Sample Input:  
7/26/2019 
 
Sample Output:  
26/7/2019
"""

import calendar

date = input()

if "/" in date:
    splitted = date.split('/')
    print(f"{splitted[1]}/{splitted[0]}/{splitted[2]}")

else:
    months = {month: number for number, month in enumerate(calendar.month_name) if month}
    splitted = date.split()
    print("{}/{}/{}".format(
        splitted[1].strip(','),
        months.get(splitted[0]),
        splitted[2]
    ))