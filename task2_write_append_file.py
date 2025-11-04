# Task 2: Write and Append Data to a File

def write_and_append_file(filename):
    """Writes user input to a file, appends extra data, and displays the result."""
    try:
        # Write user input to the file
        user_input = input("Enter some data to write to the file: ")
        with open(filename, 'w') as file:
            file.write(user_input + '\n')

        # Append more data
        extra_data = input("Enter additional data to append: ")
        with open(filename, 'a') as file:
            file.write(extra_data + '\n')

        # Read and display final content
        print("\nFinal file content:")
        with open(filename, 'r') as file:
            print(file.read())

    except Exception as e:
        print(f"An error occurred: {e}")


write_and_append_file("output.txt")
