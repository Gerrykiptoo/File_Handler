# File_Handler
📁 Overview
This Python program demonstrates comprehensive file handling operations including reading, writing, and processing text files with robust error handling. It provides an interactive menu for users to perform various file operations safely.

# ✨Features#

file_handler/
├── file_handling.py    # Main program file
├── original.txt        # Example input file
├── output.txt          # Generated output
├── uppercase.txt       # Uppercase version
├── reverse.txt         # Reversed line version (optional)
└── wordcount.txt       # Version with word count (optional)


# 📂 Files in the Project

1.file_handling.py - Main program with all the functions

2.original.txt - Sample input file (created automatically)

3.Generated output files:

4.output.txt

5.uppercase.txt

6.reverse.txt (if reverse option used)

7.wordcount.txt (if word count option used)

# 🛠️ How to Use
First run setup (in terminal):

echo "Sample file content line 1" > original.txt
echo "Line 2 with more text" >> original.txt
echo "Final line of content" >> original.txt

# Run the program:
#### python file_handling.py


# Menu Options:
1. Read a file
2. Create uppercase version of a file
3. Reverse lines in a file
4. Add word count to a file
5. Exit
    
# 🔧 Functions Included
read_file() - Basic file reading

read_file_safely() - File reading with error handling

write_to_file() - Safe file writing

process_file() - Process files with transformation functions

Transformation functions:

uppercase_text()

reverse_lines()

word_count()

# 🚨 Error Handling
The program handles:

File not found errors

Permission errors

General I/O errors

Unexpected exceptions

