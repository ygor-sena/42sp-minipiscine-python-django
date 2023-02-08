from local_lib.path import Path

def main():
	folder = "test_folder"
	file_name = folder + "/test_file"
	try:
		Path.makedirs(folder)
		f = Path(file_name)
		f.open("a")
		f.write_text("My very first pip installation!")
		print(Path(f).read_text())
	except FileExistsError as e:
		print(e)

if __name__ == '__main__':
	main()
