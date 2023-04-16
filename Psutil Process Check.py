import psutil as psu

def is_process_running(process_name):
    """Returns True if a process with the given name is running"""
    for proc in psu.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

# Example usage
if is_process_running('OpenHardwareMonitor.exe'):
    print('OpenHardwareMonitor.exe process is running')
else:
    print('OpenHardwareMonitor.exe process is not running')