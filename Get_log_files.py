import os
import retrieve_log_files
init_ = retrieve_log_files
dir_path = os.path.dirname(os.path.realpath(__file__))
path = dir_path
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

def initialize_retrieve_log_files_py():
    init_.get_log_files_for_loop()
initialize_retrieve_log_files_py()

for file in os.listdir():
    if file.endswith(".txt"):
        print("Log file name: "+file+"\n")
        read_text_file(file)
        print("\n")