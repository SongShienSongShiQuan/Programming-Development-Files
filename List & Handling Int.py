import os
import sys
import subprocess


Exception_Loc_Index = ['sec_a0000', 'sec_a5501']

a0 = Exception_Loc_Index[0] #Prints the 0 part of list: 'sec_a0000'.
a1 = Exception_Loc_Index[1] #Prints the 0 part of list: 'sec_a5501'.
print(a0, a1)

none_int_part = 'sec_a'
int_part = 0000
int_part_add = int_part + 1
add_leading_zeros = ("%04d" % (int_part_add,))
to_str = str(add_leading_zeros)
join_str = (none_int_part+to_str)
print(join_str)