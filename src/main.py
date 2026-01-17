import os    #to work with files,folders and directories

def scan_files(directory):  #directory is the folder to scan
    print(f"Scanning directory: {directory}\n")

    for folder, subfolders, files in os.walk(directory):  #recursively goes through every folder and sub-folder
        for file in files:
            file_path = os.path.join(folder, file)  #create and joins the folder path
            print(file_path)

# paths relative to this file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   #points to the project root
SAMPLES_DIR = os.path.join(BASE_DIR, "samples")   #appends to the base project directory
#this works regardless from where the script is run

print("Resolved samples path:", SAMPLES_DIR)  #confirms the exact directory it will scan

scan_files(SAMPLES_DIR)  #calls the function
