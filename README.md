# ableton-samples

2025: updated script, more robust regex etc, now exports to .json. Issue: Large .als files with collected samples take a while to process.

TODO: Perfomance tweaks (multithreading)

2022 edit: I have redone this as a website here: <https://ableton-samples-list.vercel.app/>

A Python 3 script that displays all .WAV, .MP3 and .AIFF samples and VSTs (beta) used in an Ableton Live project.

Let's say you have a lot of old sample folders on your hard drive that you do not plan on using anymore and would like to delete to save up space. What if some of the files were in an older track that you did not do 'save and collect' for? Firing up Ableton takes too long, so this script may be helpful to quickly check if that's the case.

Select one or multiple .ALS files (Ableton Live project file) and all samples and VSTs (beta) used in the project will be displayed.

## Usage

on a Mac first run:
"brew install python-tk"

then inside the folder that has the script:
"python3 abletonsamplesFinal.py"

If you have a lot of projects for further readability you can import the data into Sublime Text and do 'permute lines - unique'.

## EDIT

New command line version will list all the samples from a folder of projects. On the Mac:

1. Copy the abletonSamplesFinal_ALL_COMMANDLINE.py file into the root of the directory with your projects.
2. Open the terminal and navigate to the same project directory using the cd command (e.g., cd PATH_TO_YOUR_DIRECTORY). You can also drag the folder into the terminal instead of typing.
3. In the terminal, enter the following command (without quotes): python3 abletonSamplesFinal_ALL_COMMANDLINE.py
4. The script will now run, printing progress messages to the terminal. Once it is complete, all the sample names with respective directories will be saved to a file called allSamples.json in the same directory.

Note that you no longer need to redirect the output to allSamples.txt using >, as the script now handles this for you.
