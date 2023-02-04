def read_file():
    with open("numbers.txt", "r") as file:
        read_data = file.read()
    output = read_data.replace(',', "\n")
    print(output)

if __name__ == '__main__':
    read_file()