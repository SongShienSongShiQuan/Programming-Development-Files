import cmd
from pkgutil import get_data
from re import sub
import sys
import time
from webbrowser import get
import psutil
import os
import subprocess

print('Initializing...')
print('If RAM usage exceeded: Terminate \'blender.exe\' to protect_process.')
protect_process = True
while protect_process == True:
    get_ram_usage = psutil.virtual_memory()
    get_ram_usage_percent = get_ram_usage.percent.conjugate()
    ram_usage_var1 = 96.5 #Set lower than Var2.
    ram_usage_var2 = 100 #Set higher than Var1.
    if get_ram_usage_percent >= ram_usage_var1 and get_ram_usage_percent <= ram_usage_var2:
        print('Executing Command')
        command = 'taskkill /im blender.exe'
        process = subprocess.run(command, capture_output=True).stderr
        output_process = process.decode("utf-8")
        time.sleep(1)
        with open('protect_process_terminate_blender_out.txt', 'w') as write_file:
            write_file.write(output_process)
        with open('protect_process_terminate_blender_out.txt') as read_file:
            read_file_init = read_file.readline()
            length_output_process = (len(output_process))
            length_read_file_init = (len(read_file_init))
            if length_output_process >= ((length_read_file_init)-5) and length_output_process <= ((length_read_file_init)+5):
                print('Process Terminated', output_process)
                print('Initializing: Sys.ext()')
                sys.exit()
            print('Re-init...')
            

    elif get_ram_usage_percent < ram_usage_var1:
        time.sleep(5)
        print('RAM usage normal.')