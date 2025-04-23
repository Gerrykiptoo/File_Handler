# File reading function
def read_file(filename):
    """Basic file reading function"""
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

# Safe file reading with error handling
def read_file_safely(filename):
    """Read file with error handling"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile content:")
            print(content)
            return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' doesn't exist.")
    except PermissionError:
        print(f"Error: No permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# File writing function
def write_to_file(filename, content):
    """Write content to a file"""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Successfully wrote to {filename}")
    except PermissionError:
        print(f"Error: No permission to write to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while writing: {str(e)}")

# File processing function
def process_file(input_file, output_file, processing_func):
    """Process a file through a function and save to new file"""
    try:
        # Read
        with open(input_file, 'r') as f:
            content = f.read()
        
        # Process
        processed = processing_func(content)
        
        # Write
        with open(output_file, 'w') as f:
            f.write(processed)
            
        print(f"Processed file saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Processing error: {str(e)}")

# Processing functions
def uppercase_text(text):
    """Convert text to uppercase"""
    return text.upper()

def reverse_lines(text):
    """Reverse each line of text"""
    lines = text.split('\n')
    return '\n'.join(line[::-1] for line in lines)

def word_count(text):
    """Add word count at the end"""
    words = text.split()
    return f"{text}\n\nWord count: {len(words)}"

# Main menu
def main_menu():
    """Main interactive menu"""
    print("\nFile Operations Menu:")
    print("1. Read a file")
    print("2. Create uppercase version of a file")
    print("3. Reverse lines in a file")
    print("4. Add word count to a file")
    print("5. Exit")
    
    while True:
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            filename = input("Enter filename to read: ")
            read_file_safely(filename)
        elif choice == '2':
            input_file = input("Enter input filename: ")
            output_file = input("Enter output filename: ")
            process_file(input_file, output_file, uppercase_text)
        elif choice == '3':
            input_file = input("Enter input filename: ")
            output_file = input("Enter output filename: ")
            process_file(input_file, output_file, reverse_lines)
        elif choice == '4':
            input_file = input("Enter input filename: ")
            output_file = input("Enter output filename: ")
            process_file(input_file, output_file, word_count)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

# Program entry point
if __name__ == "__main__":
    print("Welcome to the File Handling Program!")
    main_menu()