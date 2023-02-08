import sys
import os
from settings import *

def check_input():
	if len(sys.argv) != 2:
		sys.exit("Wrong argument number")
	if not sys.argv[1].endswith(".template"):
		sys.exit("Wrong file extension")
	if not os.path.isfile(sys.argv[1]):
		sys.exit("File doesn't exist")
	return sys.argv[1]

def main():
	input = check_input()
	output_file = input.replace(".template", ".html")
	dict = globals()
	with open(input) as file:
		data = file.read()
	for key, value in dict.items():
		data = data.replace("{" + key + "}", str(value))
	with open(output_file, "w") as file:
		file.write(data)

if __name__ == '__main__':
	main()
