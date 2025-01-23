# a1.py

# Ethan Thornberg
# ethornbe@uci.edu
# 43744127

""" Imports """

from pathlib import Path


""" Base Functions """

# Input should appear as follows:
# [COMMAND] [INPUT] [[-]OPTION] [INPUT]
# Should handle Absolute and relative paths in commands

def create_file (file_path, file_name):
    # Creates a new file in the specified directory
    # C 'path' -n 'name' 
    # All files are '.sdu' formats

    # Check for existing directory, otherwise print ERROR
    if not file_path.exists():
        print('ERROR')
        return

    # Check for possible existing files with given name, otherwise print ERROR

    # Create new file

    # Confirm file was created by printing the new path

    pass

def delete_file (file_path):
    # Deletes an existing DSU file in the given directory
    # D 'path'

    # Check if file exists and is a DSU file, otherwise print ERROR

    # Delete file
    file_path.unlink()
    # Output 'path' DELETED

    pass

def read_file (file_path):
    # Print the contents of a DSU file given the directory
    # R 'path'
    
    # Check if file exists and is DSU file, print EMPTY and prompt input again
    if not file_path.exists() or '.dsu' in str(file_path):
        print('EMPTY')
        return
    # Check contents, if empty print EMPTY and wait for corrected input

    # Print contents if not empty
    
    print(file_path)
    fileContent = file_path.read_text()
    print(fileContent)
    print()

    pass

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
        user_input = user_input.lower().strip().split()
        user_input[1] = Path(user_input[1])

        print(user_input[0], 'is your command\n')

        if user_input[0] == 'c':
            create_file (user_input[1], user_input[3])

        elif user_input[0] == 'd':
            delete_file (user_input[1])

        elif user_input[0] == 'r':
            read_file(user_input[1])




    # Parse input contents with .split() and .strip() 

    # using conditional branching execute command

    pass



if __name__ == '__main__':

    currentDir = Path.cwd()

    input('Welcome to PyFiles! Press Enter to Start... \n')

    main ()
