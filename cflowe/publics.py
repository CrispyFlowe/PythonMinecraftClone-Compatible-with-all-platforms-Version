# CFLOWE PUBLICS
import sys
import os

# sys.path.insert(1, '/path/to/application/app/folder')
sys.path.append('/path/to/application/app/folder')


true = 1
false = 0


def printf(text, *formats):
    sys.stdout.writelines(text %(formats) + "\n")


