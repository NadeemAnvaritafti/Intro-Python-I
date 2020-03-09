"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print('This is the name of the script:', sys.argv[0])
print('Number of arguments:', len(sys.argv))
for item in sys.argv:
    print('Argument:', item)

# Print out the OS platform you're using:
platform = sys.platform
print(platform)
if platform == 'win32':
    print('Platform is Windows')

# Print out the version of Python you're using:
print('Python version:', sys.version)


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print('Process ID:', os.getpid())

# Print the current working directory (cwd):
print('CWD:', os.getcwd())

# Print out your machine's login name
print('Login name:', os.getlogin())
