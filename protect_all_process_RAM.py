import cmd
from pkgutil import get_data
from re import sub
import sys
import time
from webbrowser import get
import psutil
import os
import subprocess
import program_list

init_program_list = program_list.program_list

program_list_save = ['blender.exe', 'msedge.exe', 'explorer.exe', 'RobloxStudioBeta.exe', 'XboxGameBarSpotify.exe', 'Python.exe', 'RuntimeBroker.exe', 'RobloxPlayerBeta.exe']

print('Initializing...')
print('If RAM usage exceeded: Terminate \'blender.exe', 'msedge.exe', 'explorer.exe', 'RobloxStudioBeta.exe', 'XboxGameBarSpotify.exe', 'RuntimeBroker.exe', 'RobloxPlayerBeta.exe', 'browser.exe', 'AvastBrowser.exe', 'firefox.exe', 'chrome.exe', 'CocCocUpdate.exe', 'CocCocCrashHandler.exe', 'CocCocCrashHandler64.exe', 'MicrosoftEdgeUpdate.exe', 'GoogleUpdate.exe', 'GoogleCrashHandler.exe', 'fdm.exe', 'PhoneExperienceHost.exe', 'AdobeIPCBroker.exe', 'CCXProcess.exe', 'OneDrive.exe', 'node.exe')
protect_process = True
interation = 0
print_limiter = 5
while protect_process == True:
    get_ram_usage = psutil.virtual_memory()
    get_ram_usage_percent = get_ram_usage.percent.conjugate()
    ram_usage_var1 = 98 #Set lower than Var2.
    ram_usage_var2 = 100 #Set higher than Var1.
    if get_ram_usage_percent >= ram_usage_var1 and get_ram_usage_percent <= ram_usage_var2:
        print('Executing Command')
        for items in init_program_list:
            data = items
            parameter_1 = 'taskkill /F /im '
            join_data = parameter_1 + data
            command = join_data
            process = subprocess.run(command, capture_output=True).stderr
            output_process = process.decode("utf-8")
            time.sleep(1)
        with open('protect_all_process_RAM_usage_out.txt', 'w') as write_file:
            write_file.write(output_process)
        with open('protect_all_process_RAM_usage_out.txt') as read_file:
            read_file_init = read_file.readline()
            length_output_process = (len(output_process))
            length_read_file_init = (len(read_file_init))
            val_a_0 = 0
            val_b_0 = 0
            if length_output_process == val_a_0 and length_output_process == val_b_0:
                print('All Process Terminated')
                sys.exit()
            elif length_output_process >= ((length_read_file_init)):
                print(output_process)
                add_interation = interation + 1
                interation = add_interation
                print(interation)
                if interation == 5:
                    print(output_process)
                    print('All Process Terminated')
                    print('Initializing sys.exit()...')
                    sys.exit()
            

    elif get_ram_usage_percent < ram_usage_var1:
        time.sleep(5)
        if print_limiter > 0:
            print_limiter_sub = print_limiter -1
            print_limiter = print_limiter_sub
            print_limiter_to_str = str(print_limiter)
            print('RAM usage normal. Checks Left: '+print_limiter_to_str+' protect_all_process_RAM.py will still run after checks is not printing.')