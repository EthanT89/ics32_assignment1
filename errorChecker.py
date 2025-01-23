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
        print('ERRORa')
        return

    if cmd == '-n':
        filename = file_name + '.dsu'
    else:
        print('ERRORb')
        return

    new_file = directory / filename
    
    if new_file.exists():
        print('ERRORc')
        return

    # Create new file
    new_file.touch()  # physically creates an empty file

    # Confirm file was created by printing the new path
    print(new_file)

def delete_file (file_to_delete):
    # Deletes an existing DSU file in the given directory
    # D 'path'

    # Check if file exists and is a DSU file, otherwise print ERROR

    if (not file_to_delete.exists()) or (file_to_delete.suffix != ".dsu"):
        print("ERRORd")
        return

    # Delete file
    file_to_delete.unlink()

    # Output 'path' DELETED
    print(f"{file_to_delete} DELETED")

def read_file (file_to_read):
    # Print the contents of a DSU file given the directory
    # R 'path'
    
    # Check if file exists and is DSU file, print EMPTY and prompt input again
    if not file_to_read.exists() or file_to_read.suffix != ".dsu":
        print("ERRORe")
        return
    # Check contents, if empty print EMPTY and wait for corrected input
    contents = file_to_read.read_text()
    if not contents:
        print("EMPTY")
    else:
        # Print contents if not empty
        print(contents)

def main ():

    user_input = ''

    while user_input != 'q':

        user_input = input()
    
        # Parse input contents with shlex.split() 
        parts = shlex.split(user_input, posix=False)

        if len(parts) == 0:
            # No command given
            continue

        cmd = parts[0].upper()

        if cmd == 'Q':
            break

        if cmd not in ['C', 'D', 'R', 'Q']:
            print("ERRORf")
            continue

        if len(parts) < 2:
            print("ERRORg")
            continue

        raw_path = parts[1]
        if raw_path.startswith('"') and raw_path.endswith('"'):
            raw_path = raw_path[1:-1]

        directory = Path(raw_path)

        # execute command using conditional branching
        if cmd == 'C':
            if len(parts) < 4:
                print("ERRORh")
                continue
            if parts[2] != "-n":
                print("ERRORi")
                continue
            create_file (directory, parts[3], parts[2])

        elif cmd == 'D':
            delete_file (directory)

        elif cmd == 'R':
            read_file(directory)

if __name__ == '__main__':

    currentDir = Path.cwd()

    main ()
