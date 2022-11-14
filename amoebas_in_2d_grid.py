# Daylan Stoica

# @DaylanDStoica

# 24 October 2022

'''
Amoebas in a 2D grid
Problem 762

Consider a two dimensional grid of squares. The grid has 4 rows but infinitely many columns.
coordinates that repressent the fill
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
C(2) = 2,   C(10) = 1301,  C(20) = 5895236TODO: rework t to work with a list of ,
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


"""
from multiprocessing.spawn import old_main_modules


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
    
    amoeba1 = Amoeba( parent_x + 1, parent_y)
    amoeba2 = Amoeba( parent_x + 1, ( parent_y + 1 ) % 4)
    
    return amoeba1, amoeba2

def divide_amoeba_outer ( parent_amoeba : Amoeba):
    # to handle the outer transition from one to two amoebas
    parent_amoeba, amoeba2 = divide_amoeba( parent_amoeba)
        #replace the parent amoeba with one of the children's values
    return parent_amoeba, amoeba2

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
            
# loop_test_amoeba_class()

def handle_tracking_filled ( grid ,parent_amoeba : Amoeba):
    # take in a parent_amoeba, and the grid that tracks where is occupied 
    parent_x = parent_amoeba.pos_x 
    parent_y = parent_amoeba.pos_y 
    amoeba1, amoeba2 = divide_amoeba( parent_amoeba)
    grid[parent_x][parent_y] = '_'  # parent's coord is now empty 
    grid[amoeba1.pos_x][amoeba1.pos_y] = '*' #now filled
    grid[amoeba2.pos_y][amoeba2.pos_y] = '*' #now filled
    
    
def build_grid():
    grid = [ [] ]
    return grid

def trigger_all_divisions( grid, amoeba_list):
    ''' go through the list of amoebas and trigger their division, and update the grid appropriately'''
    print("Starting grid: ")
    old_grid = grid 
    print(old_grid)
    old_amoeba_list = amoeba_list # a temp variable, used for keeping for-loop stable
        # not going through constantly shifting contents
        # also true for the grid - old_grid
    for curr_amoeba in old_amoeba_list:
        handle_tracking_filled(grid, curr_amoeba)
        print("     new grid:")
        print(grid)
    print("final grid: ")
    print(grid)
    
def test_mass_division ():
    starting_amoeba = Amoeba()
    grid = build_grid() 
    amoeba_list = [starting_amoeba]
    for i in range(10):
        trigger_all_divisions(grid, amoeba_list)
        
test_mass_division()
"""

"""

# rework the functions, to work with a list of coords (x,y)
# drop the idea of an Amoeba class 

# using a list of 2D coords (x,y) to record where is filled and 
# divided to
def base_amoeba_grid():
    # build the base of the grid, with the starting amoeba's coordinates
    # return [(0,0)]
    return [ [0,0] ]

def divide_amoeba( amoeba_pos):
    '''
    An amoeba in square-cell (x,y) can divide itself into two amoebas 
    to occupy the squares (x+1, y) and (x+1, (y+1) mod 4), 
    '''
    # amoeba_pos will contain the two parts of coords 
    amoeba_x = amoeba_pos[0] + 1 #the new amoebas share the new pos_x
    amoeba_y1 = amoeba_pos[1] 
    amoeba_y2 = ( amoeba_pos[1] + 1) % 4   

    # return [( amoeba_x, amoeba_y1), ( amoeba_x, amoeba_y2)]
    # return as a list of lists, to be split outside
    return [ [amoeba_x, amoeba_y1], [amoeba_x, amoeba_y2]]

def print_grid_test():
    grid = base_amoeba_grid()
    print("starting grid", grid)
    temp_grid = grid
    #use temporary grid for not using dynamic list within the loop
    
    for amoeba in temp_grid:
        # print("amoeba type: ",type(amoeba))
        # print("grid type:", type(grid))
        print("current amoeba: ", amoeba)
        temp_amoeba = amoeba 
        # grid.pop(amoeba)
        new_amoebas = divide_amoeba(temp_amoeba)
        grid.remove(amoeba) # remove the parent amoeba, now divided

        grid.append(new_amoebas[0])
        grid.append( new_amoebas[1])
        #add the new coords to the grid
    print("final grid", grid)


print_grid_test()

"""

'''attempt number 3: one single 1-D list, not a 2-D array of coords, 
but a single row of coordinates
each element will include two elements, representing the two coordinates
that will be used to calculate the locations of the new amoebas after division
amoeba[0] will be the x-coordinate, amoeba[1] will be the y-coordinate'''

def build_grid():
    '''build a 'grid', represented by nested list'''
    grid = [ [0,0] ]
    return grid 

def divide_amoeba (grid, parent_amoeba):
    '''given the coordinates of a parent_amoeba, get the coordinates of its children
    and add them to the grid, while removing the parent from the list'''
    par_x = parent_amoeba[0]
    par_y = parent_amoeba[1]
    
    amoeba1 = [par_x + 1, par_y]
    amoeba2 = [ par_x  + 1, ( par_y + 1) % 4]
    
    grid.append(amoeba1)
    grid.append( amoeba2)
    grid.remove(parent_amoeba)
    
    
import copy 
def split_all_amoebas( grid):
    '''create a copy of the grid, to loop through and perform the divisions separately, then at end, convert 
    original grid to divided_grid'''
    modded_grid = grid.copy() 
    print(" beginning to split all amoeabas in the list")
    print("         original grid: ")
    print(grid)
    for parent_amoeba in grid:
        print("splitting amoeba: ", parent_amoeba)
        divide_amoeba(modded_grid, parent_amoeba)
        # intention: to update the grid within the function, 
    grid = modded_grid
    print("         new grid: ")
    print(grid)
    return grid 
    
    
def main():
    grid = build_grid()
    for x in range(4):
        print("split division ", x)
        grid = split_all_amoebas(grid)
        
        
    print("     final grid")
    print(grid)
    
main()
