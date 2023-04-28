def integer_count_log_write():
    integer_count_input = (input("Input iteration limit: "))
    val_1 = int(integer_count_input)
    with open('integer_count_value.py', 'w') as write_file:
            val_1_to_str = str(val_1)
            init_write = write_file.write('val_1 = '+val_1_to_str)