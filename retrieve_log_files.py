import log_files_list
import os
init_ = log_files_list.log_files_list_get
get_current_file_name = os.path.basename(__file__)
val_1 = '?'

try:
    def get_log_files_for_loop():
        for log_files in init_:
            try:
                global val_1
                val_1 = log_files
                print("Log file name: "+log_files+"\n")
                with open(log_files, 'r') as f:
                    print(f.read())
                print("\n")
            except Exception as error_output:
                print(get_current_file_name+' Loc>sec_a0001:', 'Log file named "',val_1,'" ',error_output)
except Exception as error_output:
        print(get_current_file_name+' Loc>sec_a0002:', 'Log file named "',val_1,'" ',error_output)