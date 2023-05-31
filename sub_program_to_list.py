import program_list
import os
get_current_file_name = os.path.basename(__file__)
try:
    def init_sub_program_to_list():
        init_ = program_list.program_list

        pause = (input("Must have '.exe' at the end. \nPress any key to continue"))
        input_1 = (input("Input program name to remove from the list: "))
        init_.remove(input_1)

        result = init_
        result_to_str = str(result)
        with open('program_list.py', 'w') as write_file:
            write_file.write("program_list = "+result_to_str)
    init_sub_program_to_list()
except Exception as error_output:
        print(get_current_file_name+' Loc>sec_a0001:', error_output)
        import sub_program_to_list
        in_sub_program_to_list = sub_program_to_list
        in_sub_program_to_list.init_sub_program_to_list()