def my_var():
    digit = 42
    nbr_str = '42'
    sentence = 'quarante-deux'
    f_digit = 42.0
    choose = True
    nbr_list = [42]
    nbr_dict = {42: 42}
    nbr_tupl = (42,)
    new_set = set()

    print(digit, "has a type", type(digit))
    print(nbr_str, "has a type", type(nbr_str))
    print(sentence, "has a type", type(sentence))
    print(f_digit, "has a type", type(f_digit))
    print(choose, "has a type", type(choose))
    print(nbr_list, "has a type", type(nbr_list))
    print(nbr_dict, "has a type", type(nbr_dict))
    print(nbr_tupl, "has a type", type(nbr_tupl))
    print(new_set, "has a type", type(new_set))

if __name__ == '__main__':
    my_var()
