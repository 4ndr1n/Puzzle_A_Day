from matplotlib.pyplot import axis
import numpy as np
"""
test = open(r'/Users/Andrin/Desktop/newdoc.csv','w')

stringarray = ["mol", "luege"]

x = "{} ; {}"
print(x.format(stringarray[0],stringarray[1]))
test.write(x.format(stringarray[0],stringarray[1]))
"""

arr = np.array([[[1,0,0,1,1,0,0], 
                 [2,0,0,1,2,0,0], 
                 [3,0,0,1,3,0,0], 
                 [4,0,0,1,4,0,0], 
                 [5,0,0,1,5,0,0], 
                 [6,0,0,1,6,0,0], 
                 [7,1,9,1,7,0,0]],
                [[8,0,0,2,1,0,0], 
                 [9,0,0,2,2,0,0], 
                 [10,0,0,2,3,0,0], 
                 [11,0,0,2,4,0,0], 
                 [12,0,0,2,5,0,0], 
                 [13,0,0,2,6,0,0], 
                 [14,1,9,2,7,0,0]], 
                [[15,0,0,3,1,0,0], 
                 [16,0,0,3,2,0,0], 
                 [17,0,0,3,3,0,0], 
                 [18,0,0,3,4,0,0], 
                 [19,0,0,3,5,0,0], 
                 [20,0,0,3,6,0,0], 
                 [21,0,0,3,7,0,0]],
                [[22,0,0,4,1,0,0], 
                 [23,0,0,4,2,0,0], 
                 [24,0,0,4,3,0,0], 
                 [25,0,0,4,4,0,0], 
                 [26,0,0,4,5,0,0], 
                 [27,0,0,4,6,0,0], 
                 [28,0,0,4,7,0,0]],
                [[29,0,0,5,1,0,0], 
                 [30,0,0,5,2,0,0], 
                 [31,0,0,5,3,0,0], 
                 [32,0,0,5,4,0,0], 
                 [33,0,0,5,5,0,0], 
                 [34,0,0,5,6,0,0], 
                 [35,0,0,5,7,0,0]], 
                [[36,0,0,6,1,0,0], 
                 [37,0,0,6,2,0,0], 
                 [38,0,0,6,3,0,0], 
                 [39,0,0,6,4,0,0], 
                 [40,0,0,6,5,0,0], 
                 [41,0,0,6,6,0,0], 
                 [42,0,0,6,7,0,0]],
                [[43,0,0,7,1,0,0], 
                 [44,0,0,7,2,0,0], 
                 [45,0,0,7,3,0,0], 
                 [46,1,9,7,4,0,0], 
                 [47,1,9,7,5,0,0], 
                 [48,1,9,7,6,0,0], 
                 [49,1,9,7,7,0,0]]
                 ])

def dayInput(day):
    DayInput = day
    DayX = 2
    DayY = 0
    # Input gets reformatted
    while DayInput > 7:
        DayInput -= 7
        DayX += 1
        DayY = dayInput
    DayInput -= 1
    DayY=DayInput
    # Input gets inserted into "arr"
    arr[DayX][DayY][2]=9
    arr[DayX][DayY][1]=1

def monthInput(month):
    MonthInput = month
    MonthX = 0
    MonthY = 0
    # Input gets checked and saved
    # Input gets reformatted
    if MonthInput >6:
        MonthX += 1
        MonthInput -= 7
        MonthY = MonthInput
    else:
        MonthInput -= 1
        MonthY=MonthInput
    # Input gets inserted into "arr"
    arr[MonthX][MonthY][2]=9
    arr[MonthX][MonthY][1]=1


ddayarr = np.arange(1,32)
sdayarr = np.arange(1,31)

Februar = [2]
thirtiones = np.concatenate((np.arange(1,8,2), np.arange(8,13,2)),axis=0)
thirties = np.concatenate((np.arange(4,7,2),np.arange(9,13,2)),axis=0)

dates = np.array([],ndmin=0)

print(dates)
for i in thirtiones:
    for y in ddayarr:
        dayInput(y)
        monthInput(i)
        x = np.array(y,i)
        np.vstack((dates,x))

print(dates)

for i in thirties:
    for y in sdayarr:
        dayInput(y)
        monthInput(i)
        print(y, i)
        