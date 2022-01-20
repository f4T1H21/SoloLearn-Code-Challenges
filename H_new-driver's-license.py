"""
Nee Driver's License

You have to get a new driver's license and you show up at the office at the same time as 4 other people. The office says that they will see everyone in alphabetical order and it takes 20 minutes for them to process each new license. All of the agents are available now, and they can each see one customer at a time. How long will it take for you to walk out of the office with your new license? 
 
Task  
Given everyone's name that showed up at the same time, determine how long it will take to get your new license. 
 
Input Format  
Your input will be a string of your name, then an integer of the number of available agents, and lastly a string of the other four names separated by spaces. 
 
Output Format  
You will output an integer of the number of minutes that it will take to get your license. 
 
Sample Input 
'Eric' 
2 
'Adam Caroline Rebecca Frank' 
 
Sample Output  
40
"""

def find_index(lst, char):
    for sub_lst in lst:
        if char in sub_lst:
            return (lst.index(sub_lst), sub_lst.index(char))
    raise ValueError(f"'{char}' is not in list!")


myname = input()
agents = int(input())
names = input().split()

names.append(myname)
names.sort()

grup_sayisi = len(names) / agents
if str(grup_sayisi).split('.')[1] != '0':
    grup_sayisi = int(grup_sayisi) + 1
else:
    grup_sayisi = int(grup_sayisi)

c = 0
yliste = []
for grup in range(grup_sayisi):
    yliste.append([names[i] for i in range(c, c+agents) if i < len(names)])
    c += agents

myplace = find_index(yliste, myname)
print((myplace[0]+1)*20)

#1 Inputları al
#2 İsimleri alfabetik sırala
#3 Toplam isim sayısını Müsait olan görevli sayısına bölerek kaç grup çıktığını bul
#4 bu grupları grupla
#5 bizim kaçıncı grupta olduğumuzu bul
#6 20 ile çarp