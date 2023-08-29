import os
import re
import gzip
import pathlib
import glob
from shutil import copyfile

def search_and_print_results(read_data, extension, f):
    search_result = re.findall(f"/\w+.*{extension}", read_data)
    if search_result:
        search_set = set(search_result)
        search_str = str(search_set)
        replace_space = search_str.replace("%20", " ")
        final_list = replace_space.replace(",", "\n")
        f.write(final_list)
    else:
        f.write(f"No {extension.upper()} files found.\n")

def getAllAbletonFiles(filename, f):
    print(f'Processing {filename}')
    base = os.path.splitext(filename)[0]
    temp_zip_file = copyfile(filename, base + '.zip')

    try:
        with gzip.open(temp_zip_file, 'rb') as f_in:
            read_data = f_in.read().decode('utf-8')
            search_and_print_results(read_data, 'wav', f)
            search_and_print_results(read_data, 'mp3', f)
            search_and_print_results(read_data, 'aiff', f)

            search_result_vst = re.findall("\w.*vst", read_data)
            if search_result_vst:
                for element in search_result_vst:
                    f.write(element + '\n')
            else:
                f.write("No VST plugins found.\n")
    finally:
        os.remove(temp_zip_file)

def main():
    my_path = pathlib.Path().resolve()
    result = []
    output_file = 'allSamples.txt'

    print('Searching for .als files...')
    for x in os.walk(my_path):
        for y in glob.glob(os.path.join(x[0], '*.als')):
            result.append(y)

    if not result:
        print('No .als files found.')
        return

    print('Going through the projects...')
    with open(output_file, 'w') as f:
        for onefile in result:
            getAllAbletonFiles(onefile, f)

    print(f'Results written to {output_file}')

if __name__ == '__main__':
    main()

