"""This script contains a function `read_and_modify_file` that performs the following tasks:
    1. Prompts the user to enter the name of a file to read.
    2. Reads the content of the specified file.
    3. Modifies the content by converting it to uppercase.
    4. Writes the modified content to a new file with a name prefixed by "modified_".
    5. Handles potential errors such as:
        - FileNotFoundError: If the specified file does not exist.
        - PermissionError: If there is no permission to read the file.
        - Any other unexpected exceptions.
    The function provides user-friendly error messages for better usability.
Open a file in read mode and handle exceptions"""
def read_and_modify_file():
        try:
            # Ask user for the input file name
            input_filename = input("Enter the name of the file to read: ")
            
            # Check if the file exists and is readable
            print(f"Trying to open file: {input_filename}")
            # Try to open and read the file
            with open(example.txt, 'r') as example:
                content = example.read()
            
            # Modify the content (for example, convert to uppercase)
            modified_content = content.upper()
    
            # Create a new file name for the modified content
            output_filename = f"modified_{input_filename}"
    
            # Write the modified content to the new file
            with open(output_filename, 'w') as outfile:
                outfile.write(modified_content)
    
            print(f"Modified content has been written to '{output_filename}'.")
    
        except FileNotFoundError:
            print("❌ Error: The file does not exist.")
        except PermissionError:
            print("❌ Error: Permission denied to read the file.")
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            
# Run the program
read_and_modify_file()
# Ensure the script doesn't close immediately after execution
input("Press Enter to exit...")