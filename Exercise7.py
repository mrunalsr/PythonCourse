#We have to paint the wall find no of tin boxes needed to paint the wall. Consider 1 box will paint 7sq.m
#we have to take input of height and width from user
#formula :- no of tin required are = hright*width/coverage
import math


def Calculate(hei,wid):
    no_of_box = (hei*wid)/7
    return no_of_box


height = int(input("Enter the height of wall : "))
width = int(input("Enter the width of wall : "))
result=Calculate(height,width)
print("No of cans required to paint this wall is : ",math.ceil(result))