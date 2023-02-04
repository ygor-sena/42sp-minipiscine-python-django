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

def main():
    states = get_states()
    cities = get_cities()
    error_key = "Unknown state"

    if len(sys.argv) == 2:
        s_value = states.get(sys.argv[1], error_key)
        result = cities.get(s_value, error_key)
        print(result)

if __name__ == '__main__':
    main()
