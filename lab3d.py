#!/usr/bin/env python3

# Author ID: rchoudhary15

import subprocess

def free_space():
    # Run the Linux command and capture the output
    p = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    
    # Communicate with the process and get the output
    output = p.communicate()
    
    # Extract stdout, decode to string and strip newline
    stdout = output[0].decode('utf-8').strip()
    
    return stdout

# If run directly, print the free space
if __name__ == '__main__':
    print(free_space())
