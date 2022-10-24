# Daylan Stoica

# @DaylanDStoica

# 24 October 2022

'''
Amoebas in a 2D grid
Problem 762

Consider a two dimensional grid of squares. The grid has 4 rows but infinitely many columns.

An amoeba in square-cell (x,y) can divide itself into two amoebas 
to occupy the squares (x+1, y) and (x+1, (y+1) mod 4), 
provided these squares are empty.

The following diagrams show two cases of an amoeba placed in square A of each grid. 
When it divides, it is replaced with two amoebas, one at each of the squares marked with B:

Originally there is only one amoeba in the square (0,0).
After N divisions there will be N+1 amoebas arranged in the grid. 
An arrangement may be reached in several different ways but it is only counted once. 
Let C(N) be the number of different possible arrangements after N divisions.

For example,
C(2) = 2,   C(10) = 1301,  C(20) = 5895236,
and the last nine digits of C(100) are 125923036.

Find C(100 000), enter the last nine digits as your answer.
'''

'''
notes:
after each division, the original amoeba is deleted, and two new amoebas appear 
at the new spots, if the spots are already empty
    two calculations to determine the location of two new amoebas

question: if the spaces are already filled, is the division not possible, 
    if yes, then the parent amoeba just disappears'''

class Amoeba:
    def __init__ ( self, pos_x = 0, pos_y = 0):
        self.pos_x = pos_x 
        self.pos_y = pos_y 
        
def divide_amoeba ( parent_amoeba : Amoeba):
    # take in an Amoeba, and create two new of the class
    # and drop the parent, 
    # to represent the division 
    parent_x = parent_amoeba.pos_x 
    parent_y = parent_amoeba.pos_y 
    
    amoeba1 = Amoeba ( parent_x + 1, parent_y)
    amoeba2 = Amoeba( parent_x + 1, ( parent_y + 1 ) % 4)
    
    return amoeba1, amoeba2

def test_amoeba_class (starting_x = 0, starting_y = 0):
    parent_amoeba = Amoeba( starting_x, starting_y )
    print( " paraent coords: ( %d, %d )" %(parent_amoeba.pos_x, parent_amoeba.pos_y) )
    amoeba1 , amoeba2 = divide_amoeba( parent_amoeba)
    print( " children: ( %d , %d ) , ( %d, %d )" 
        % (amoeba1.pos_x, amoeba1.pos_y, amoeba2.pos_x, amoeba2.pos_y) )
    
def loop_test_amoeba_class ():
    for x in range ( 10):
        for y in range( 23):
            test_amoeba_class( x, y)
            
loop_test_amoeba_class()