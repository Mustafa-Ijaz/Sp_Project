"""Mustafa Ijaz
"""
import csv
outlook=[]
play=[]
with open("data.csv") as csvfile:
    f=csv.reader(csvfile)
    for row in f:
        print(row)
        outlook.append(row[0])
        play.append(row[4])

    outlook.pop(0)
    play.pop(0)
    print(outlook)
    print(play)
    dict_fre= {}
    str1 = ""
    NO=0
    YES=0
    overcast=0
    sunny=0
    rainy=0
    var1=0
    var2=0

for i, j in zip(outlook, play):

    if i == "overcast":
        overcast+=1
        if j == "yes":
            YES+=1
            str1 = i + "," + j
            if str1 in dict_fre:
                dict_fre[str1] += 1
            else:
                dict_fre[str1] = 1
        elif j == "no":
            NO+=1
            str1 = i + "," + j
            if str1 in dict_fre:
                dict_fre[str1] += 1
            else:
                dict_fre[str1] = 1
    elif i == "sunny":
        sunny+=1
        if j == "yes":
            YES += 1
            str1 = i + "," + j
            if str1 in dict_fre:
                dict_fre[str1] += 1
            else:
                dict_fre[str1] = 1
            temp= dict_fre[str1]
            var1=temp
        elif j == "no":
            NO += 1

            str1 = i + "," + j
            if str1 in dict_fre:
                dict_fre[str1] += 1
            else:
                dict_fre[str1] = 1
            temp = dict_fre[str1]
            var2 = temp
    elif i == "rainy":
        rainy+=1
        if j == "yes":
            YES += 1

            str1 = i + "," + j
            if str1 in dict_fre:
                dict_fre[str1] += 1
            else:
                dict_fre[str1] = 1

        elif j == "no":
            NO += 1

            str1 = i + "," + j
            if str1 in dict_fre:
                dict_fre[str1] += 1
            else:
                dict_fre[str1] = 1

print(dict_fre)
print("Sunny yes",var1)
print("Sunny No ",var2)


print("Total Yes are",YES)
print("Total NO are",NO)
Total = YES+NO
print("Total ",Total)
sunnyY=var1/YES
sunnyN=var2/NO
print("Sunny yes prob",sunnyY)
print("Sunny No prob",sunnyN)
probYes=YES/Total
probNo=NO/Total
print("probability of Yes is ",probYes)
print("probability of No is ",probNo)
print("Total Num of Overcast",overcast)
print("Total Num of Sunny",sunny)
print("Total Num of Rainy",rainy)
print("probability of Overcast is ",overcast/Total)
probSunny=sunny/Total
print("probability of Sunny is ",probSunny)
print("probability of Rainy is ",rainy/Total)
tempY=(sunnyY*probYes)/probSunny
tempN=(sunnyN*probNo)/probSunny
if(tempY>tempN):
    print("Probability YES|Sunny", tempY)
else:
    print("Probability No|Sunny",tempN)
print("hello")
