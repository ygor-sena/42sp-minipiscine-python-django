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

def return_city_key(cities, value):
    k_cities = list(cities.keys())
    v_cities = list(cities.values())
    for i in range(len(cities)):
        if v_cities[i] == value:
            return k_cities[i]
    return ("Unknown capital city")

def return_state_key(states, value):
    k_states = list(states.keys())
    v_states = list(states.values())
    for i in range(len(states)):
        if v_states[i] == value:
            return k_states[i]
    return ("Unknown capital city")

def main():
    states = get_states()
    cities = get_cities()

    if len(sys.argv) == 2:
        city_key = return_city_key(cities, sys.argv[1])
        result = return_state_key(states, city_key)
        print(result)

if __name__ == '__main__':
    main()
        