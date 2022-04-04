from signal import pthread_sigmask
from turtle import Shape
import numpy as np

# Spielfeld als 3D Array implementiert. 1D = X-Achse, 2D = Y-Achse, 3D = Gefüllt oder nicht. 9 ist Spielfeldrand in der zweiten Spalte. The first row helps with counting the lines. The second row indicates the shape, that fills this sqare. The third row indicates the searched for value. The fourth row represents the row on the board. The fifth row marks the column of the board

arr = np.array([[[1,0,1,1,1,0,0], 
                 [2,0,0,1,2,0,0], 
                 [3,0,0,1,3,0,0], 
                 [4,0,0,1,4,0,0], 
                 [5,0,0,1,5,0,0], 
                 [6,0,0,1,6,0,0], 
                 [7,9,0,1,7,0,0]],
                [[8,0,0,2,1,0,0], 
                 [9,0,0,2,2,0,0], 
                 [10,0,0,2,3,0,0], 
                 [11,0,0,2,4,0,0], 
                 [12,0,0,2,5,0,0], 
                 [13,0,0,2,6,0,0], 
                 [14,9,0,2,7,0,0]], 
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
                 [46,9,0,7,4,0,0], 
                 [47,9,0,7,5,0,0], 
                 [48,9,0,7,6,0,0], 
                 [49,9,0,7,7,0,0]]
                 ])

# Implementierung der Figuren, die auf das Spielfeld gelegt werden können. Klassen werden verwendet wegen den verschiedenen Orientierungen, die die Formen haben können.

class Sshape(object):
    def __init__(self):
        pass

    def Form1(self):
        self.Form1 = [[1,1,0], [0,1,0], [0,1,1]]
        return self.Form1

    def Form2(self):
        self.Form2 = [[0,0,1], [1,1,1], [1,0,0]]
        return self.Form2
    
    def Form3(self):
        self.Form3 = [[0,1,1], [0,1,0], [1,1,0]]
        return self.Form3

    def Form4(self):
        self.Form4 = [[1,0,0], [1,1,1], [0,0,1]]
        return self.Form4

class Cshape(object):
    def __init__(self) -> None:
        pass

    def Form1(self):
        self.Form1 = [[1,1], [1,0], [1,1]]
        return self.Form1
    
    def Form2(self):
        self.Form2 = [[1,1,1], [1,0,1]]
        return self.Form2
    
    def Form3(self):
        self.Form3 = [[1,1], [0,1], [1,1]]
        return self.Form3
    def Form4(self):
        self.Form4 = [[1,0,1], [1,1,1]]
        return self.Form4

class BigLshape(object):
    def __init__(self) -> None:
        pass

    def Form1(self):
        self.Form1 = [[1,0,0], [1,0,0], [1,1,1]]
        return self.Form1
    
    def Form2(self):
        self.Form2 = [[1,1,1], [1,0,0], [1,0,0]]
        return self.Form2
    
    def Form3(self):
        self.Form3 = [[1,1,1], [0,0,1], [0,0,1]]
        return self.Form3

    def Form4(self):
        self.Form4 = [[0,0,1], [0,0,1],[1,1,1]]
        return self.Form4

class smallLshape(object):
    def __init__(self) -> None:
        pass

    def Form1(self):
        self.Form1 = [[1,0], [1,0], [1,1]]
        return self.Form1
    
    def Form2(self):
        self.Form2 = [[1,1,1,1], [1,0,0,0]]
        return self.Form2
    
    def Form3(self):
        self.Form3 = [[1,1], [0,1], [0,1],[0,1]]
        return self.Form3

    def Form4(self):
        self.Form4 = [[0,0,0,1], [1,1,1,1]]
        return self.Form4

class brokenTshape(object):
    def __init__(self) -> None:
        pass
    
    def Form1(self):
        self.Form1 = [[0,1], [1,1], [0,1], [0,1]]
        return self.Form1
    
    def Form2(self):
        self.Form2 = [[0,0,1,0], [1,1,1,1]]
        return self.Form2
    
    def Form3(self):
        self.Form3 = [[1,0], [1,0], [1,1], [1,0]]
        return self.Form3

    def Form4(self):
        self.Form4 = [[1,1,1,1], [0,1,0,0]]
        return self.Form4

    def Form5(self):
        self.Form5 = [[1,0], [1,1], [1,0], [1,0]]
        return self.Form5

    def Form6(self):
        self.Form6 = [[0,1], [0,1], [1,1], [1,0]]
        return self.Form6

    def Form7(self):
        self.Form2 = [[0,1,0,0], [1,1,1,1]]
        return self.Form7
    
    def Form8(self):
        self.Form4 = [[1,1,1,1], [0,0,1,0]]
        return self.Form8
    
class filledOshape(object):
    def __init__(self) -> None:
        pass

    def Form1(self):
        self.Form1 = [[1,1], [1,1], [1,1]]
        return self.Form1
    
    def Form2(self):
        self.Form2 = [[1,1,1], [1,1,1]]
        return self.Form2

class filledPshape(object):
    def __init__(self) -> None:
        pass
    
    def Form1(self):
        self.Form1 = [[1,1], [1,1], [1,0]]
        return self.Form1
    
    def Form2(self):
        self.Form2 = [[1,1,1], [0,1,1]]
        return self.Form2
    
    def Form3(self):
        self.Form3 = [[0,1], [1,1], [1,1]]
        return self.Form3

    def Form4(self):
        self.Form4 = [[1,1,0], [1,1,1]]
        return self.Form4
    
    def Form5(self):
        self.Form5 = [[1,1], [1,1], [0,1]]
        return self.Form5
    
    def Form6(self):
        self.Form6 = [[0,1,1], [1,1,1]]
        return self.Form6
    
    def Form7(self):
        self.Form7 = [[1,0], [1,1], [1,1]]
        return self.Form7

    def Form8(self):
        self.Form8 = [[1,1,1], [1,1,0]]
        return self.Form8

class brokenYshape(object):
    def __init__(self) -> None:
        pass

    def Form1(self):
        self.Form1 = [[1,0], [1,1], [0,1], [0,1]]
        return self.Form1
    
    def Form2(self):
        self.Form2 = [[0,0,1,1], [1,1,1,0]]
        return self.Form2
    
    def Form3(self):
        self.Form3 = [[1,0], [1,0], [1,1], [0,1]]
        return self.Form3

    def Form4(self):
        self.Form4 = [[0,1,1,1], [1,1,0,0]]
        return self.Form4
    
    def Form5(self):
        self.Form5 = [[0,1], [1,1], [1,0], [1,0]]
        return self.Form5
    
    def Form6(self):
        self.Form6 = [[1,1,1,0], [0,0,1,1]]
        return self.Form6
    
    def Form7(self):
        self.Form7 = [[0,1], [0,1], [1,1], [1,0]]
        return self.Form7

    def Form8(self):
        self.Form8 = [[1,1,0,0], [0,1,1,1]]
        return self.Form8

class Execution():
    def __init__(self) -> None:
        pass



# implementierung von constraints

# Counts the number of open squares. If there are only two, 1 is returned. 
def Outputchecker():
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
        return 0
    else:
        return count


# Checks if the square is already occupied.
def Occupancie(x, y):
    if (np.any(arr[x][y][1])):
        return 1
    else:
        pass


# Take an input and return an output

class Origin():
    def __init__(self) -> None:
        pass

    def Input(self):
        