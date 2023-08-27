import os
import re
import gzip
from shutil import copyfile
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

def search_and_print(extension, read_data):
    # Search for lines with the appropriate extension, turn the result into a set to exclude duplicates.
    search_result = re.findall(f"/\w+.*{extension}", read_data)
    set_and_string = str(set(search_result))
    # Do a few replacements for readability.
    replace_20 = set_and_string.replace("%20", "/")
    final_list = replace_20.replace(",", "\n")
    
    # Print the results if they exist.
    if search_result:
        print(final_list)
    else:
        print(f"No {extension.upper()} files found.")
    

def process_files(filename2):
    for file in filename2:
        print(str(file))

        # Replace the .als extension with .zip and make a copy of the file.
        base = os.path.splitext(file)[0]
        filename3 = copyfile(file, base + '.zip')

        try:
            # Unzip the resulting file. Only gzip worked.
            with gzip.open(filename3, 'rb') as f:
                read_data = f.read().decode('utf-8')

                search_and_print("wav", read_data)
                search_and_print("mp3", read_data)
                search_and_print("aiff", read_data)
                
                search_result_vst = re.findall("\w.*vst*", read_data)
                if search_result_vst:
                    print(search_result_vst)
                else:
                    print("No VST plugins found.")
        except gzip.BadGzipFile:
            print("The file is not a gzip file.")
        except FileNotFoundError:
            print("The file does not exist.")
        finally:
            # Remove the copied file if it exists.
            if os.path.exists(filename3):
                os.remove(filename3)
            else:
                print("The file does not exist and cannot be deleted.")


def main():
    Tk().withdraw()
    filename2 = askopenfilenames()
    print(filename2)
    
    process_files(filename2)


if __name__ == "__main__":
    main()
