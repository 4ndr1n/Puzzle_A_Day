from ast import For, Global
from pyexpat import XML_PARAM_ENTITY_PARSING_ALWAYS
from signal import pthread_sigmask
from turtle import Shape
import numpy as np
import pandas as pd

# Variables
MonthX = 0
MonthY = 0

DayX = 2
DayY = 0

tempVal = 0

xsis = 0
ysis = 0

storage = []

passcond = 0

# User Input and formatting for the array

def dayInput():
    global DayInput
    DayInput = int(input("Gib den gesuchten Tag ein(DD)"))

def monthInput():
    global MonthInput
    MonthInput = int(input("Gib den gesuchten Monat an(MM)"))

absolutePlace = (ysis,xsis,1)

# Spielfeld als 3D Array implementiert. 1D = X-Achse, 2D = Y-Achse, 
# 3D = Gefüllt oder nicht. 9 ist Spielfeldrand in der zweiten Spalte. 
# The first row helps with counting the lines. The second row indicates
# the shape, that fills this sqare. The third row indicates formtype. The fourth row represents the row on the board. The fifth row marks 
# the column of the board.

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

# Implementierung der Figuren, die auf das Spielfeld gelegt werden können.
# Dictionaries werden verwendet wegen den verschiedenen Orientierungen, die die 
# Figuren haben können. Die Figuren wurden im Uhrzeigersinn gedreht und erfasst,
# dann gewendet wenn nötig und dann wieder im Uhrzeigersinn gedreht und erfasst.
# Die Namen sollen die die Form der Figuren nachahmen.

Cshape ={1:np.array([[1,1], [1,0], [1,1]]),
        2:np.array([[1,1,1], [1,0,1]]),
        3:np.array([[1,1], [0,1], [1,1]]),
        4:np.array([[1,0,1], [1,1,1]])}

BigLshape ={1:np.array([[1,0,0], [1,0,0], [1,1,1]]),
        2:np.array([[1,1,1], [1,0,0], [1,0,0]]),
        3:np.array([[1,1,1], [0,0,1], [0,0,1]]),
        4:np.array([[0,0,1], [0,0,1], [1,1,1]])}

smallLshape ={1:np.array([[1,0], [1,0], [1,0], [1,1]]),
        2:np.array([[1,1,1,1], [1,0,0,0]]),
        3:np.array([[1,1], [0,1], [0,1],[0,1]]),
        4:np.array([[0,0,0,1], [1,1,1,1]])}

brokenTshape ={1:np.array([[0,1], [1,1], [0,1], [0,1]]),
        2:np.array([[0,0,1,0], [1,1,1,1]]),
        3:np.array([[1,0], [1,0], [1,1], [1,0]]),
        4:np.array([[1,1,1,1], [0,1,0,0]]),
        5:np.array([[1,0], [1,1], [1,0], [1,0]]),
        6:np.array([[0,1], [0,1], [1,1], [1,0]]),
        7:np.array([[0,1,0,0], [1,1,1,1]]),
        8:np.array([[1,1,1,1], [0,0,1,0]])}

FilledOShape ={1:np.array([[1,1], [1,1], [1,1]]),
        2:np.array([[1,1,1],[1,1,1]])}

filledPshape ={1:np.array([[1,1], [1,1], [1,0]]),
        2:np.array([[1,1,1], [0,1,1]]),
        3:np.array([[0,1], [1,1], [1,1]]),
        4:np.array([[1,1,0], [1,1,1]]),
        5:np.array([[1,1], [1,1], [0,1]]),
        6:np.array([[0,1,1], [1,1,1]]),
        7:np.array([[1,0], [1,1], [1,1]]),
        8:np.array([[1,1,1], [1,1,0]])}

brokenYshape ={1:np.array([[1,0], [1,1], [0,1], [0,1]]),
        2:np.array([[0,0,1,1], [1,1,1,0]]),
        3:np.array([[1,0], [1,0], [1,1], [0,1]]),
        4:np.array([[0,1,1,1], [1,1,0,0]]),
        5:np.array([[0,1], [1,1], [1,0], [1,0]]),
        6:np.array([[1,1,1,0], [0,0,1,1]]),
        7:np.array([[0,1], [0,1], [1,1], [1,0]]),
        8:np.array([[1,1,0,0], [0,1,1,1]])}

Sshape ={1:np.array([[1,1,0], [0,1,0], [0,1,1]]),
        2:np.array([[0,0,1], [1,1,1], [1,0,0]]),
        3:np.array([[0,1,1], [0,1,0], [1,1,0]]),
        4:np.array([[1,0,0], [1,1,1], [0,0,1]])}

# implementierung von constraints

## Counts the number of open squares. If there are only two, 1 is returned. 
class Constraints():
    def Endingconstraint():
        count = 0
        for x in arr:
            w = 0
            for y in x:
                if (np.any(arr[0][w][1])):
                    pass
                else:
                    count += 1
                w += 1
        if w == 2:
            return 1
        else:
            return 0
# Checks if the square is already occupied.
    def Occupancie(x, y):
        if arr[x][y][1] == 1:
            return 1
        else:
            return 0
    def Occcheck(Storage):
        for x in Storage:
            for y in x:
                if y == 2:
                    return False
                else:
                    return True

dayInput()
monthInput()


while DayInput > 7:
    DayInput -= 7
    DayX += 1
    DayY = dayInput
    print(DayX,DayY)
DayInput -= 1
DayY=DayInput

if MonthInput >6:
    MonthX += 1
    MonthInput -= 7
    MonthY = MonthInput
else:
    monthInput -= 1
    MonthY=monthInput

#  changes the value to 9 to indicate the searched for date.
arr[MonthX][MonthY][2]=9
arr[MonthX][MonthY][1]=1
arr[DayX][DayY][2]=9
arr[DayX][DayY][1]=1

# generates the list of the shapes and changes it acordingly.

ShapeList = np.array([Cshape,BigLshape,smallLshape,brokenTshape,FilledOShape,filledPshape,brokenYshape,Sshape])


#  adds a shape to the matrix
n = 0
Shape = ShapeList[n]
Shape = Shape.get(1)

MShape = Shape.shape

ap0 = absolutePlace[0]

ap1 = absolutePlace[1]

m = 0

for x in range(MShape[1]):
    n = 0
    for y in range(MShape[0]):
        storage.append(Constraints.Occupancie((ap0+m),(ap1+n)))
        n += 1
    m+=1

temparray = np.array(storage)
Storage = temparray.reshape(MShape[0],MShape[1])

# compares the shape of the two arrays to make sure they line up.
assert Storage.shape == Shape.shape

Storage += Shape

passcond = Constraints.Occcheck(Storage)


print(Storage,passcond)

# Test area