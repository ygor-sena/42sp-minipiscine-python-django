def get_dict():
    d = {
        'Hendrix' : '1942',
        'Allman' : '1946',
        'King' : '1925',
        'Clapton' : '1945',
        'Johnson' : '1911',
        'Berry' : '1926',
        'Vaughan' : '1954',
        'Cooder' : '1947',
        'Page' : '1944',
        'Richards' : '1943',
        'Hammett' : '1962',
        'Cobain' : '1967',
        'Garcia' : '1942',
        'Beck' : '1944',
        'Santana' : '1947',
        'Ramone' : '1948',
        'White' : '1975',
        'Frusciante': '1970',
        'Thompson' : '1949',
        'Burton' : '1939',
    }
    return d

def print_dict(dict):
    for key, value in dict.items():
        print(key)

def main():
    lst = list(get_dict().items())
    mark = sorted(lst, key=lambda x:x[::-1])
    result = dict(mark)
    print_dict(result)

if __name__ == '__main__':
    main()
