import sys
import os
import random

path = sys.argv[1]

def randomize_file():
	return random.choice(os.listdir(path))

def print_random_filename(random_file):
	random_filename = random_file.split(".jpg")[0]
	print random_filename

random_file = random.choice(os.listdir(path))

if random_file.startswith('.'):
	new_random_file = randomize_file()
	print_random_filename(new_random_file)
else:
	print_random_filename(random_file)
