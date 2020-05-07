import os
import re
import sys
import gzip

from shutil import copyfile

from tkinter import Tk
from tkinter.filedialog import askopenfilenames

#Ask user to select a project file. 
Tk().withdraw()
filename2 = askopenfilenames()
print(filename2)

for file in filename2:

	print(str(file))

	#Replace the .als extension with .zip and make a copy of the file. 
	base = os.path.splitext(file)[0]
	filename3 = copyfile(file, base + '.zip')

	#Unzip the resulting file. Only gzip worked. 
	with gzip.open(filename3, 'rb') as f:
		read_data = f.read().decode('utf-8')

		#Search for lines with the appropriate extension, turn the result into a set to exclude duplicates. 
		searchResultWAV = re.findall("/\w+.*wav", read_data)
		SetAndStringWAV = str((set(searchResultWAV)))
		#Do a few replacements for readability.
		Replace20WAV = SetAndStringWAV.replace("%20", "/")
		FinalListWAV = Replace20WAV.replace(",", "\n")


		searchResultMP3 = re.findall("/\w+.*mp3", read_data)
		SetAndStringMP3 = str((set(searchResultMP3)))
		Replace20MP3 = SetAndStringMP3.replace("%20", "/")
		FinalListMP3 = Replace20MP3.replace(",", "\n")


		searchResultAIFF = re.findall("/\w+.*aiff", read_data)
		SetAndStringAIFF = str((set(searchResultAIFF)))
		Replace20AIFF = SetAndStringAIFF.replace("%20", "/")
		FinalListAIFF = Replace20AIFF.replace(",", "\n")

		searchResultVST = re.findall("\w.*vst*", read_data)
		#SetAndStringVST = str((set(searchResultAIFF)))
		#Replace20VST = SetAndStringAIFF.replace("%20", "/")
		#FinalListVST = Replace20AIFF.replace(",", "\n")

		#Print the results if they exist. 
		if len(searchResultWAV) > 0:
			print(FinalListWAV)
		else:
			print("No WAV files found.")

		if len(searchResultMP3) > 0:
			print(FinalListMP3)
		else:
			print("No MP3 files found.")

		if len(searchResultAIFF) > 0:
			print(FinalListAIFF)
		else:
			print("No AIFF files found.")

		if len(searchResultVST) > 0:
			print(searchResultVST)
		else:
			print("No VST plugins found.")


#Remove the copied file if it exists. 
		if os.path.exists(filename3):
		  os.remove(filename3)
		else:
		  print("The file does not exist and cannot be deleted.")
