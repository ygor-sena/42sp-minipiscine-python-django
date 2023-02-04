def print_dict(dict):
    for key, value in dict.items():
        print(key, ':', value)

def get_list():
    d = [
    ('Hendrix' , '1942'),
    ('Allman' , '1946'),
    ('King' , '1925'),
    ('Clapton' , '1945'),
    ('Johnson' , '1911'),
    ('Berry' , '1926'),
    ('Vaughan' , '1954'),
    ('Cooder' , '1947'),
    ('Page' , '1944'),
    ('Richards' , '1943'),
    ('Hammett' , '1962'),
    ('Cobain' , '1967'),
    ('Garcia' , '1942'),
    ('Beck' , '1944'),
    ('Santana' , '1947'),
    ('Ramone' , '1948'),
    ('White' , '1975'),
    ('Frusciante', '1970'),
    ('Thompson' , '1949'),
    ('Burton' , '1939')
    ]
    dict = {}
    for key, value in d:
        if value in dict:
            dict[value] =  dict[value] + " " + key
        else:
            dict[value] = key
    print_dict(dict)

def main():
    list = get_list()

if __name__ == '__main__':
    main()
