import os
import re
import gzip
import pathlib
import json

def extract_files_and_vsts(filepath):
    """Extracts files and VSTs, processing the file line by line."""
    samples = set()
    vsts = set()

    try:
        with gzip.open(filepath, 'rt', encoding='utf-8', errors='ignore') as f_in:
            for line in f_in:  # Process line by line
                # More robust and efficient regex (using finditer)
                for ext in ['wav', 'mp3', 'aiff']:
                    for match in re.finditer(rf'(?<=[\s<"])((?:(?!\.{ext})[\S])+)\.{ext}(?:\?[^"\s]*)?(?=["\s>])', line, re.IGNORECASE):
                        samples.add(match.group(1).replace("%20", " ") + "." + ext)

                for match in re.finditer(r'(?<=[\s<"])((?:(?!\.vst)[\S])+)\.vst(?=["\s>])', line, re.IGNORECASE):
                    vsts.add(match.group(1) + ".vst")

    except (OSError, EOFError, gzip.BadGzipFile) as e:
      print(f"Error reading {filepath}: {e}")
      return None, None #return None

    return list(samples), list(vsts)

def process_ableton_file(filepath):
    """Processes a single Ableton file."""
    print(f'Processing {filepath}')
    samples, vsts = extract_files_and_vsts(filepath)
    if samples is None or vsts is None: #Check the error
        return None
    project_name = filepath.stem
    return {
        "project": project_name,
        "samples": samples,
        "vsts": vsts
    }

def main():
    """Main function."""
    my_path = pathlib.Path().resolve()
    output_filepath = my_path / 'allSamples.json'

    print('Searching for .als files...')
    als_files = list(my_path.glob('**/*.als'))

    if not als_files:
        print('No .als files found.')
        return

    print('Going through the projects...')
    results = []
    for als_file in als_files:
        project_data = process_ableton_file(als_file)
        if project_data:
            results.append(project_data)

    try:
        with open(output_filepath, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4)
    except OSError as e:
        print(f"Error writing to output file: {e}")

    print(f'Results written to {output_filepath}')

if __name__ == '__main__':
    main()