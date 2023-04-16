import os
import subprocess

# Define the PowerShell command to type "help()" in the Python terminal
ps_command = "python 'C:/Users/Chowfer/Desktop/CODE SPACE/File Management Main Admin.py' | python"

# Use subprocess to execute the PowerShell command and print the output
output = subprocess.run(["powershell", "-Command", ps_command])
print(output)