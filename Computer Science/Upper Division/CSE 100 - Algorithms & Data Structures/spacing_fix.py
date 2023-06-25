import sys
import os

# check args
if len(sys.argv) < 2:
    print("Please provide a file name as a command-line argument.")
    sys.exit(1)

# get the directory name from the command line
directory = sys.argv[1]

# Iterate over all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    if os.path.isfile(file_path):  # Check if the item is a file
        with open(file_path, 'r+') as file:
            if '.DS_Store' in file_path:
                continue
            
            file_contents = file.read()
            
            # Perform manipulations on file_contents
            new_file = file_contents.replace("-   ", "- ")
            new_file = new_file.replace(".  ", ". ")
            
            file.seek(0)
            file.write(new_file)
            file.truncate()