#!/usr/bin/python3

import os
import re
import sys

def main():
    for line in sys.stdin:
        # Modify the regex to check for lines starting with #
        match = re.match(r'^\s*#', line)
        
        fields = line.strip().split(':')  # strip any whitespace and split into an array
        
        # Check if the line starts with # or does not have exactly 5 fields
        # This skips commented lines or lines with incorrect format
        if match or len(fields) != 5:
            continue
        
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,,," % (fields[3], fields[2])  # Full name for user info
        groups = fields[4].split(',')  # Split groups into a list
        
        print(f"==> Creating account for {username}...")
        
        # Create user with disabled password and specified full name
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        os.system(cmd)
        
        print(f"==> Setting the password for {username}...")
        
        # Set the password for the new user
        cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
        os.system(cmd)
        
        # Add user to specified groups
        for group in groups:
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"
                os.system(cmd)

if __name__ == '__main__':
    main()
