# pipi.py

# Import the OS module to work with the file path
import os

# Get the current working directory
current_dir = os.getcwd()

# Create a path to the 'uploads' directory
uploads_dir = os.path.join(current_dir, 'uploads')

# Check if the 'uploads' directory exists
if not os.path.exists(uploads_dir):
    print("The 'uploads' directory does not exist. Exiting.")
    exit(1)

# Create and write to the 'preview.txt' file
with open(os.path.join(uploads_dir, 'preview.txt'), 'w') as file:
    file.write("Hello, this is a preview file created by pipi.py!\n")
    file.write("You can use this file to store some preview data.\n")
    file.write("Feel free to modify or extend it as needed.\n")

print("Preview file 'preview.txt' created successfully in 'uploads' directory.")
