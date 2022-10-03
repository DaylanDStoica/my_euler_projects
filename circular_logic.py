#Daylan Stoica
# @DaylanDStoica

# October 1 , 2022

'''
Circular Logic
Problem 209

A k-input binary truth table is a map from k input bits 
(binary digits, 0 [false] or 1 [true]) to 1 output bit. 
For example, the 2-input binary truth tables for the 
logical AND and XOR functions are:

x 	y 	x AND y
0	0	   0
0	1	   0
1	0	   0
1	1	   1
x 	y 	x XOR y
0	0	   0
0	1	   1
1	0	   1
1	1	   0

How many 6-input binary truth tables, τ, satisfy the formula
τ(a, b, c, d, e, f) AND 
τ(b, c, d, e, f, a XOR (b AND c)) 
    = 0

for all 6-bit inputs (a, b, c, d, e, f)?
'''

'''
PLAN:
compile the two tables separately, then run through the different possible states for each
and join them at the greater table level 
    T1 AND T2
        T1 = (a,b,c,d,e,f)
        T2 = (b,c,d,e,f,  a XOR ( b AND C)  )
'''
class Truth_Table:
    def __init__(self, table_length=6):
        # self.table_array = [0,1]*table_length
        # self.table_array = [[0,1]]*table_length
        self.table_array = [[False, True]] * table_length
    
    def build_the_table(self):
        '''with the given string of boolean statements for the instance
        create a table of different True/False conditions'''
        pass
    
    
def test():
    # table1 = [[0,1]]*6
    table1 = Truth_Table(6)

    print(table1.table_array)
    # print(table1)
    
test()
