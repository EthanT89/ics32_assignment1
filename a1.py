# Ethan Thornberg
# ethornbe@uci.edu
# 43744127

import shlex
from pathlib import Path

def parse_input(user_input: str):
    """Split user input into a list of tokens using shlex."""

    user_input = user_input.strip()
    if not user_input:
        return []
    return shlex.split(user_input)

def create_file(parsed_input):
    """
    Creates a file given a File Path and File Name
    If successful, prints the path to the newly created file.
    Otherwise, prints 'ERROR'.
    """
    if len(parsed_input) != 4:
        print("ERROR")
        return
    
    dir_path_str = parsed_input[1]
    option = parsed_input[2]
    file_name = parsed_input[3]
    
    if option != '-n':
        print("ERROR")
        return

    dir_path = Path(dir_path_str)
    if not dir_path.is_dir():
        print("ERROR")
        return

    new_file_path = dir_path / f"{file_name}.dsu"

    if new_file_path.exists():
        print("ERROR")
        return
    
    try:
        new_file_path.touch()
        print(str(new_file_path))
    except Exception:
        print("ERROR")

def delete_file(parsed_input):
    """
    Handle the 'D' command.
    Expects: D path_to_file
    If successful, prints '<file_path> DELETED'.
    Otherwise, prints 'ERROR'.
    """
    if len(parsed_input) != 2:
        print("ERROR")
        return
    
    # parsed_input[0] = 'D'
    file_path_str = parsed_input[1]
    file_path = Path(file_path_str)

    # Must be a .dsu file and must exist
    if file_path.suffix != '.dsu' or not file_path.exists():
        print("ERROR")
        return

    try:
        file_path.unlink()
        print(f"{file_path} DELETED")
    except Exception:
        print("ERROR")

def read_file(parsed_input):
    """
    Handle the 'R' command.
    Expects: R path_to_file
    If file is empty, prints 'EMPTY'.
    Otherwise, prints the file contents.
    Prints 'ERROR' if it's not a valid .dsu file or doesn't exist.
    """
    if len(parsed_input) != 2:
        print("ERROR")
        return
    
    # parsed_input[0] = 'R'
    file_path_str = parsed_input[1]
    file_path = Path(file_path_str)

    # Check suffix and existence
    if file_path.suffix != '.dsu' or not file_path.exists():
        print("ERROR")
        return

    try:
        contents = file_path.read_text()
        if len(contents.strip()) == 0:
            print("EMPTY")
        else:
            # Print file contents directly
            print(contents, end='')
    except Exception:
        print("ERROR")

def main():
    while True:
        user_input = input()
        parsed_input = parse_input(user_input)
        
        if not parsed_input:
            # If empty input, ignore or print ERROR. Let's ignore here.
            continue
        
        command = parsed_input[0].upper()
        
        if command == 'Q':  # Quit
            break
        elif command == 'C':
            create_file(parsed_input)
        elif command == 'D':
            delete_file(parsed_input)
        elif command == 'R':
            read_file(parsed_input)
        else:
            print("ERROR")

if __name__ == "__main__":
    main()
