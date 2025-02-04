# inet_4031_adduser_script

### Description
This repository contains a Python script for automating user creation on Linux systems. The script provides a systematic approach to generating user accounts and group memberships by parsing a structured input file. It demonstrates a programmatic method for system administration tasks, allowing efficient and scalable user management across Linux environments.

### Operation
1. Prerequisites:
   - Ensure Python 3 is installed
   - Verify sudo/root access permissions

2. Script Execution:
   ```bash
   # Make script executable
   chmod +x create-users.py

   # Run with input file
   sudo ./create-users.py < create-users.input
   ```

3. Input File Configuration:
   - Use colon-delimited format
   - Specify username, password, last name, first name, and group memberships
   - Support for multiple groups and comment lines
