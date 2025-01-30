#write a program to get length in feet from userand convert it into different measuring units.
length=int(input("length in feet:"))
option=int(input("choose from 1 to 7:"))
def convert_length(length):
    #conversions
    
        1= length * 12          #inches
        2= length/ 5280         #miles
        3= length / 3           #yards
        4= length * 304.8       #millimeters
        5= length * 30.48       #centimeters
        6= length / 3280.84     #kilometers
        7= length* 0.3048       #meters
    
    
