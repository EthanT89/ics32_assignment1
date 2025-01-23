# Ethan Thornberg
# ethornbe@uci.edu
# 43744127

""" Imports """

from pathlib import Path
import shlex

""" Base Functions """

# Input should appear as follows:
# [COMMAND] [INPUT] [[-]OPTION] [INPUT]
# Should handle Absolute and relative paths in commands

def create_file (directory, file_name, cmd):
    # Creates a new file in the specified directory
    # C 'path' -n 'name' 
    # All files are '.dsu' formats
    if not directory.exists():
        print('ERROR: directory does not exist.\n')
        return

    if cmd == '-n':
        filename = file_name + '.dsu'
    else:
        print('ERROR\n')
        return

    new_file = directory / filename
    
    if new_file.exists():
        print('ERROR: file already exists.\n')
        return

    # Create new file
    new_file.touch()  # physically creates an empty file

    # Confirm file was created by printing the new path
    print(new_file)
    print()

def delete_file (file_to_delete):
    # Deletes an existing DSU file in the given directory
    # D 'path'
    print('Attempting to delete file -', file_to_delete)

    # Check if file exists and is a DSU file, otherwise print ERROR

    if (not file_to_delete.exists()) or (file_to_delete.suffix != ".dsu"):
        print("ERROR: File DNE")
        return

    # Delete file
    file_to_delete.unlink()

    # Output 'path' DELETED
    print(f"{file_to_delete} DELETED\n")

def read_file (file_to_read):
    # Print the contents of a DSU file given the directory
    # R 'path'
    
    # Check if file exists and is DSU file, print EMPTY and prompt input again
    if not file_to_read.exists() or file_to_read.suffix != ".dsu":
        print("ERROR: DNE or not .dsu")
        return
    # Check contents, if empty print EMPTY and wait for corrected input
    contents = file_to_read.read_text()
    if not contents:
        print("EMPTY\n")
    else:
        # Print contents if not empty
        print('Here are the contents of the file: ')
        print(contents)
        print()

def print_options ():
    # Print the menu options for the user to choose from

    print('Commands:')
    print('Enter \'C\' to Create a File')
    print('Enter \'D\' to Delete a File')
    print('Enter \'R\' to Read a File')
    print('Format: [COMMAND] [INPUT] [[-]OPTION] [INPUT]\n')

def main ():

    user_input = ''

    while user_input != 'q':

        print_options()
        user_input = input('Please Enter a Command in the Correct Format (\'q\' to quit): \n')
        print()
    
        # Parse input contents with shlex.split() 
        parts = shlex.split(user_input)
        
        if len(parts) == 0:
            # No command given
            continue

        cmd = parts[0].upper()

        if cmd not in ['C', 'D', 'R', 'Q']:
            print("ERROR")
            continue

        directory = Path(parts[1])       

        # execute command using conditional branching
        if cmd == 'C':
            create_file (directory, parts[3], parts[2])

        elif cmd == 'D':
            delete_file (directory)

        elif cmd == 'R':
            read_file(directory)

if __name__ == '__main__':

    currentDir = Path.cwd()

    input('Welcome to PyFiles! Press Enter to Start... \n')

    main ()
