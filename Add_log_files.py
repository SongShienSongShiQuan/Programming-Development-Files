import log_files_list
import os
get_current_file_name = os.path.basename(__file__)
try:
    def init_add_log_files():
        init_ = log_files_list.log_files_list_get

        input_1 = (input("Input log file name to add: "))
        init_.append(input_1)

        result = init_
        result_to_str = str(result)
        with open('log_files_list.py', 'w') as write_file:
            write_file.write("log_files_list_get = "+result_to_str)
    init_add_log_files()
except Exception as error_output:
        print(get_current_file_name+' Loc>sec_a0001:', error_output)
        import Add_log_files
        in_add_log_files = Add_log_files
        in_add_log_files.init_add_log_files()