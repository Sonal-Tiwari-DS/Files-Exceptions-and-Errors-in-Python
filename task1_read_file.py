# Task 1: Read a File and Handle Errors

def read_file(filename):
    """Reads and prints content of a file line by line."""
    try:
        with open(filename, 'r') as file:
            print("File content:\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run 
read_file("sample.txt")
