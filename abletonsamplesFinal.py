import os
import re
import sys
import gzip

from shutil import copyfile

from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename2 = askopenfilename()
base = os.path.splitext(filename2)[0]
filename3 = copyfile(filename2, base + '.zip')


with gzip.open(filename3, 'rb') as f:
	read_data = f.read().decode('utf-8')

	searchResultWAV = re.findall("/\w+.*wav", read_data)
	SetAndStringWAV = str((set(searchResultWAV)))
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



if os.path.exists(filename3):
  os.remove(filename3)
else:
  print("The file does not exist and cannot be deleted.")
