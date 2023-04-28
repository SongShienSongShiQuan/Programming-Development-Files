from multiprocessing import process
import os
import sys
import subprocess
import time
import integer_count_log
import integer_count_value



pause = (input("Press 'Enter to continue'..."))

input_1 = (input("Input iteration limit: "))
val_1 = int(input_1)
if type(val_1) == int:
    with open('integer_count_value.py', 'w') as write_file:
        val_1_to_str = str(val_1)
        init_write = write_file.write('val_1 = '+val_1_to_str)
val_1 = int(input_1)


Exception_Loc_Index = []
init = True
none_int_part = 'sec_a'
integer_count = 0
string_int_part = '0000'

while init == True:
    string_int_part_to_real_int = int(string_int_part)
    int_part_add = string_int_part_to_real_int + 1
    add_leading_zeros = ("%04d" % (int_part_add,))
    to_str = str(add_leading_zeros)
    string_int_part = to_str
    result = (none_int_part+to_str)
    print(result)
    Exception_Loc_Index.append(result)
    time.sleep(0.1)
    add_integer_count = integer_count + 1
    integer_count = add_integer_count
    print(add_integer_count)
    if add_integer_count == val_1:
        try:
            print('Printing '+val_1_to_str+' interations: ',Exception_Loc_Index)
            Exception_Loc_Index_to_str = str(Exception_Loc_Index)
            with open('Exception_Duplication_Log.py', 'w') as write_file:
                write_file.write('Exception_Loc_Index = '+Exception_Loc_Index_to_str+'\nread_list = Exception_Loc_Index[0]')
        except Exception as error_output:
            print('Error Increment Loc>sec_a0001:', error_output)
        path1 = 'Exception Duplication Function.py'
        pause = (input("Press 'Enter to continue'..."))
        process = subprocess.run(['python.exe', path1])
        sys.exit()
    print('Running...')