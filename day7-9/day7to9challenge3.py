from data import us_state_abbrev, states_list
import os

def main():
    #Challenge 1: Print the 10th item in each data structure
    #us_state_abbrev, which is a dictionary. So get the keys list and sort them
    keys = sorted(us_state_abbrev.keys())

    #To print 10th item, print k,v based on the key at index 9 on keys list
    print("({}, {})".format(keys[9], us_state_abbrev[keys[9]]))

    #states_list, which is a list. So print the one at index 9
    print(states_list[9])

    # Challenge 2: Print the 45th key in the dictionary. Just print the value at index 44 on keys list
    print(keys[44])

    # Challenge 3: Print the 27th value in the dictionary. Just print the key, where key is the value at index 26 on keys list
    print(us_state_abbrev[keys[26]])


if __name__ == '__main__':
    main()
