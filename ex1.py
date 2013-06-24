from os import mkdir, listdir, chdir
from sys import argv
from os.path import exists
from shutil import move

script, move_from_path = argv


for letter in range(97,123):
	if not exists(chr(letter)):
		mkdir(chr(letter))

files = listdir(move_from_path)

for f in files:
	first_letter = f[0].lower()
	#print first_letter
	move((move_from_path + "/" + f), 
		 (first_letter))





