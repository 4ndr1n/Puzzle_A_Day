import numpy as np
"""
test = open(r'/Users/Andrin/Desktop/newdoc.csv','w')

stringarray = ["mol", "luege"]

x = "{} ; {}"
print(x.format(stringarray[0],stringarray[1]))
test.write(x.format(stringarray[0],stringarray[1]))
"""

def dayInput():
    x = 1
    while(x == 1):
        DayInput = int(input("Gib den gesuchten Tag ein(DD)"))
        if DayInput >=1 and DayInput <=31:
            x = 0
        else:
            print("Enter a valid day (1-31)")



dayarr = np.arange(1,32)
print(dayarr)