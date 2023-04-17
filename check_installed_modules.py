import subprocess
import sys
import time

executecommand = "pip list"
command = executecommand
output = subprocess.run(command, capture_output=True).stdout
output2length = output.decode("utf-8")
with open("new_workspace_installed_modules.txt", "w") as read_module:
            read_file1 = read_module.write(output2length)
with open("installed_modules.txt") as read_module:
            read_file2_raw = read_module.read()
            read_file2 = len(read_file2_raw)
            time.sleep(1)
            length_1 = int(read_file1)
            length_2 = int(read_file2)
            print("new_workspace_installed_modules: ", length_1, "installed_modules: ", length_2)
            if length_1 >= ((length_2)-10) and length_1 <= ((length_2)+10):
                    print("Complete Core Modules")
            elif not read_file1 == read_file2:
                    print("Modules Incomplete or Exceeded")