# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:18:04 2019

@author: cslab051
"""

#Mahrukh Ijaz
#FA-16/BSCS/125
import csv
content=[]
with open("data.txt","r") as csvfile:
    freereader=csv.reader(csvfile)
    for row in freereader:
        content.append(row)        
print(content)

outlook=[]
play=[]

for i in content[1:]:
    outlook.append(i[0])
    play.append(i[4])
    
print()
print(outlook)

print()
print(play)

#frequency=[]
#count1=0
#for i in outlook:
#    for j in outlook:
#        if i==j:
#            count1+=1
#    frequency.append(count1)
#    count1=0
#    
#print()
#print(frequency)
#
#count2=0
#frequency1=[]
#for i in play:
#    for j in play:
#        if i==j:
#            count2+=1
#    frequency1.append(count2)
#    count2=0


#print()
#print(frequency1)

dict_frequency={}
str=""

for i,j in zip(outlook,play):
    
    if i=="overcast":
        if j=="yes":
            str=i+","+j
            if str in dict_frequency:
                dict_frequency[str]+=1
            else:
                dict_frequency[str]=1
        elif j=="no":
            str=i+","+j
            if str in dict_frequency:
                dict_frequency[str]+=1
            else:
                dict_frequency[str]=1
    elif i=="sunny":
        if j=="yes":
            
            str=i+","+j
            if str in dict_frequency:
                dict_frequency[str]+=1
            else:
                dict_frequency[str]=1
        elif j=="no":

            str=i+","+j
            if str in dict_frequency:
                dict_frequency[str]+=1
            else:
                dict_frequency[str]=1
    elif i=="rainy":
        if j=="yes":
            
            str=i+","+j
            if str in dict_frequency:
                dict_frequency[str]+=1
            else:
                dict_frequency[str]=1
        elif j=="no":
            
            str=i+","+j
            if str in dict_frequency:
                dict_frequency[str]+=1
            else:
                dict_frequency[str]=1

print()
print(dict_frequency)

count_no=0
count_yes=0
count_overcast=0
count_sunny=0
count_rainy=0

for key in dict_frequency:
    if "no" in key:
        count_no+=dict_frequency[key]
        
    elif "yes" in key:
        count_yes+=dict_frequency[key]
    
    if "overcast" in key:
        count_overcast+=dict_frequency[key]
        
    elif "sunny" in key:
        count_sunny+=dict_frequency[key]
        
    elif "rainy" in key:
        count_rainy+=dict_frequency[key]

print("no",count_no)
print("yes",count_yes)

total=count_no+count_yes
prob_no=count_no/total
prob_yes=count_yes/total


print("overcast",count_overcast)
print("sunny",count_sunny)
print("rainy",count_rainy )

prob_overcast=count_overcast/total
prob_sunny=count_sunny/total
prob_rainy=count_rainy/total

sunny_no=dict_frequency["sunny,no"]
prob_sunny_no=sunny_no/count_no

sunny_yes=dict_frequency["sunny,yes"]
prob_sunny_yes=sunny_yes/count_yes

overcast_yes=dict_frequency["overcast,yes"]
prob_overcast_yes=overcast_yes/count_yes
print(prob_overcast_yes)

rainy_no=dict_frequency["rainy,no"]
prob_rainy_no=rainy_no/count_no
print(prob_rainy_no)

rainy_yes=dict_frequency["rainy,yes"]
prob_rainy_yes=rainy_yes/count_yes
print(prob_rainy_yes)

print("p(no|sunny_no)",(prob_sunny_no*prob_no)/prob_sunny)
print("p(yes|sunny_yes)",(prob_sunny_yes*prob_yes)/prob_sunny)

print("p(no|rainy_no)",(prob_rainy_no*prob_no)/prob_rainy)
print("p(yes|rainy_yes)",(prob_rainy_yes*prob_yes)/prob_rainy)

print("p(yes|overcast_yes)",(prob_overcast_yes*prob_yes)/prob_overcast)

