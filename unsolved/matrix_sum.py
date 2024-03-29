# Daylan Stoica
# @DaylanDStoica

# 27 December 2022

'''
Matrix Sum
Problem 345

We define the Matrix Sum of a matrix as the maximum possible sum of matrix elements 
such that none of the selected elements share the same row or column.

For example, the Matrix Sum of the matrix below equals 3315 ( = 863 + 383 + 343 + 959 + 767):
[
  7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303
]

Find the Matrix Sum of:

[
  7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805
]
'''


def print_matrix ( in_matrix):
  for row in in_matrix:
    print(row)
    
    
def find_the_highest_sum( matrix):
    '''given a 2D amtrix of intgers, find the highest sum of elements
    with unique columns and rows'''
    sum = 0
    
    
    return sum 
  
base_matrix = """[
  7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303 
]""" # should equal 3315

# with the matrix data given as a string, convert into a 2D matrix, with each row separated by a new line
string_matrix = """[7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805]"""

# split the matrix string into a 2d matrix
# final_matrix = string_matrix


def convert_string_to_matrix ( in_matrix):
  '''given a string of values, return a 2d matrix of the values'''
  """ 
  x = str(input())
arr  = x.split(";")
finalArr = []
for items in arr:
    arr2 = []
    arr2.append(items)
    finalArr.append(arr2)
print(finalArr)
"""
  x = in_matrix 
  array = x.split('\n')
  finalArr = []
  for row in array:
    arr2 = []
    arr2.append(row)
    finalArr.append(arr2)
  return finalArr


string_matrix.replace ( '[', '')
string_matrix.replace( ']', '')
# final_matrix = [ r.split(' ') for r in string_matrix.split('\n') ]
final_matrix = convert_string_to_matrix(string_matrix)

#test: print the type and values before the conversion, and after conversion into matrix
print(type( string_matrix))
print( string_matrix)


# final_matrix.drop('[', ']')
print(type(final_matrix))
# print(final_matrix)
print_matrix( final_matrix)


'''
go through the matrix, finding the coordinates of the next largest number
'''

