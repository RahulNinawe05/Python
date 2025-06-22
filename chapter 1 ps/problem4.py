import os

# Specify the directorye path
directory_path = '/'

try:
    # Walk through the directory
    for dirpath, dirnames, filenames in os.walk(directory_path):
        print(f'Found directory: {dirpath}')
        for filename in filenames:
            print(f'\t{filename}')
except FileNotFoundError:
    print(f"The directory {directory_path} does not exist.")
except PermissionError:
    print(f"Permission denied to access {directory_path}.")
