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

def create_file ():
    # Creates a new file in the specified directory
    # C 'path' -n 'name' 
    # All files are '.sdu' formats

    # Check for existing directory, otherwise print ERROR

    # Check for possible existing files with given name, otherwise print ERROR

    # Create new file

    # Confirm file was created by printing the new path

    pass

def delete_file ():
    # Deletes an existing DSU file in the given directory
    # D 'path'

    # Check if file exists and is a DSU file, otherwise print ERROR

    # Delete file

    # Output 'path' DELETED

    pass

def read_file ():
    # Print the contents of a DSU file given the directory
    # R 'path'
    
    # Check if file exists and is DSU file, print EMPTY and prompt input again

    # Check contents, if empty print EMPTY and wait for corrected input

    # Print contents if not empty

    pass

def main ():

    # Prompt for user input until 'q' is entered

    # Parse input contents with .split() and .strip() 

    # using conditional branching execute command

    pass



if __name__ == '__main__':

    input('Welcome to PyFiles! Press Enter to Start... ')