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
	searchResult = re.findall("/\w+.*wav", read_data)
	SetAndString = str((set(searchResult)))
	Replace20 = SetAndString.replace("%20", "/")
	FinalList = Replace20.replace(",", "\n")
	print(FinalList)

if os.path.exists(filename3):
  os.remove(filename3)
else:
  print("The file does not exist and cannot be deleted.")



