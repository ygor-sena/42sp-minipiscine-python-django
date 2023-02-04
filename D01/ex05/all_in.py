import sys

def get_states():
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    return states

def get_cities():
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    return capital_cities

def get_cities_from_states(states, cities, arg):
    if arg not in states:
        return None
    return(cities[states[arg]])

def get_states_from_cities(states, cities, arg):
    result = None
    for key, value in cities.items():
        if value == arg:
            result = key
    for key, value in states.items():
        if value == result:
            result = key
            return (result)
    return None
    
def main():
    if len(sys.argv) == 2:
        states = get_states()
        cities = get_cities()
        lst = sys.argv[1].split(',')
        for ele in lst:
            ele = ele.strip()
            if ele != "":
                out_cities = get_cities_from_states(states, cities, ele.title())
                out_states = get_states_from_cities(states, cities, ele.title())
                if out_cities is not None:
                    print("{} is the capital of {}".format(out_cities, ele.title()))
                elif out_states is not None:
                    print("{} is the capital of {}".format(ele.title(), out_states))
                else:
                    print("{} is neither a capital city nor a state".format(ele))

if __name__ == '__main__':
    main()
