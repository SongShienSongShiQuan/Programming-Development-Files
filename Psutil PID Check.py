import psutil

def is_process_running(pid):
    """Returns True if a process with the given PID is running"""
    return pid in [p.pid for p in psutil.process_iter()]

# Example usage
if is_process_running(16224):
    print('cmd.exe process with PID 16224 is running')
else:
    print('cmd.exe process with PID 16224 is not running')