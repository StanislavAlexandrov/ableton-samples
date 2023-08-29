import os
import re
import gzip
import pathlib
import glob
from shutil import copyfile

def search_and_print_results(read_data, extension):
    search_result = re.findall(f"/\w+.*{extension}", read_data)
    if search_result:
        search_set = set(search_result)
        search_str = str(search_set)
        replace_space = search_str.replace("%20", " ")
        final_list = replace_space.replace(",", "\n")
        print(final_list)
    else:
        print(f"No {extension.upper()} files found.")

def getAllAbletonFiles(filename):
    print(filename)
    base = os.path.splitext(filename)[0]
    temp_zip_file = copyfile(filename, base + '.zip')

    try:
        with gzip.open(temp_zip_file, 'rb') as f:
            read_data = f.read().decode('utf-8')
            search_and_print_results(read_data, 'wav')
            search_and_print_results(read_data, 'mp3')
            search_and_print_results(read_data, 'aiff')

            search_result_vst = re.findall("\w.*vst", read_data)
            if search_result_vst:
                for element in search_result_vst:
                    print(element)
            else:
                print("No VST plugins found.")
    finally:
        os.remove(temp_zip_file)

def main():
    my_path = pathlib.Path().resolve()
    result = []

    for x in os.walk(my_path):
        for y in glob.glob(os.path.join(x[0], '*.als')):
            result.append(y)

    for onefile in result:
        getAllAbletonFiles(onefile)

if __name__ == '__main__':
    main()
