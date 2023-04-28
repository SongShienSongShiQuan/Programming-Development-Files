import imp
import os
import sys
import subprocess
import time
import Exception_Duplication_Log
import integer_count_value

init = True
counter = 0
ref1 = integer_count_value.val_1
val_1 = ref1
while init == True:
    try:
        access_log = Exception_Duplication_Log.Exception_Loc_Index[counter]
        result = access_log
        add_counter = counter + 1
        counter = add_counter
        result_to_str = str(result)
        with open('Mako_Software.py') as read_file:
            init_read_file = read_file.read()
            get_string1 = init_read_file.count(result_to_str)
            var_get_string1 = get_string1
            if var_get_string1 == 1:
                print(result_to_str+'| Result: -0.')
            elif var_get_string1 > 1:
                print(result_to_str+'| Result: Error Duplicate '+result_to_str+' Found.')
            elif var_get_string1 < 1:
                print(result_to_str+'| Result: Error 0 '+result_to_str+' Found.')
    except Exception as error_output:
        print('Error Increment Loc>sec_a0001:', error_output)
        time.sleep(1)
        sys.exit()
    time.sleep(0.1)