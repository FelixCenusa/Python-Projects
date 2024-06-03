"""Module dosctring: random is random.."""
import random

def create_ssn(yymmdd):#9.0
    """This makes a ssn ok?"""
    personal_number = yymmdd
    if personal_number == "7":
        again = input("Again: ")
        return again
    personal_number = str(personal_number)
    personal_number = personal_number.replace("-", "")
    pn_strip = personal_number.replace(" ", "")
    random_num = random.randint(100,999)
    pn_add = pn_strip + str(random_num)
    calc = str(calculate_luhna_sum(pn_add))
    divide = 0
    divide = int(calc) % 10
    if divide != 0:
        last_digit = 10 - int(divide)
    else:
        last_digit = 0
    result = pn_strip + "-" + str(random_num) + str(last_digit)
    return result

def calculate_luhna_sum(pn_add):#9.1
    """This is the algorythm"""
    if str(len(str(pn_add))) in "69":
        if pn_add.isdigit():
            calc = 0
            temp = 0
            multiplier = 2
            for single in pn_add:
                temp = int(single) * int(multiplier)
                added = 0
                if len(str(temp)) == 2:
                    temp = str(temp)
                    added = int(temp[0]) + int(temp[1])
                    calc += int(added)
                    multiplier = (multiplier % 2) + 1
                else:
                    calc += int(temp)
                    multiplier = (multiplier % 2) + 1
            return calc
    return None


def get_acronym(input_acronym):#10
    """This gets capitals and concatinates them"""
    input_acronym = str(input_acronym)
    uppers = ""
    for letter in input_acronym:
        if letter.isupper():
            uppers += letter
    return uppers


def randomize_string(input_randomize):#11
    """this randomizes a string"""
    store = ""
    input_randomize = str(input_randomize)
    if input_randomize[-1].isdigit():
        for letter in input_randomize:
            if letter.isdigit():
                input_randomize = input_randomize.replace(letter, "", 1)
                store += letter
        shuffled = "".join(random.sample(input_randomize,len(input_randomize)))
        total = shuffled + store
        return total

    shuffled = "".join(random.sample(input_randomize,len(input_randomize)))
    print_this = input_randomize + " --> " + shuffled
    return print_this


def find_all_indexes(string1,string2):#12
    """this finds the indexes"""
    string1 = str(string1)
    string1 = string1.lower()
    string2 = str(string2)
    start_from = 0
    stored_indexes = ""
    did_once = False
    x_valriable = 1
    while x_valriable == 1:
        try:
            index_at = string1.index(string2,start_from)
            start_from = int(index_at) + 1
            stored_indexes += str(index_at) + ","
            did_once = True

        except ValueError:
            x_valriable = 0
    if did_once is True:
        fixed_indexes = stored_indexes.rstrip(stored_indexes[-1])
        return fixed_indexes
    return ""

#end of file
