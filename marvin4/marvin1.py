#!/usr/bin/python3
"""Docstring here"""
def greet():#1
    """Docstring here, just say their name"""
    name = input("What is your name? ")
    print("\nFake GPT says:\n")
    print(f"Hello {name} - your awesomeness!")
    print("What can I do you for?!")


def celcius_to_fahrenheit():#2
    """Docstring here, self explanatory"""
    celcius = float(input("Enter temperature in Celcius: "))
    farenheit = celcius * 1.8 + 32
    print("the temperature in Farenheit is: ",  round(farenheit, 2))


def points_to_grade():#3
    """Docstring here, max points and what they got calculate percentage and return grade"""
    max_points = float(input("What is the max points you can get?: "))
    points_got = float(input("How many points did you get?: "))
    if points_got >= max_points * 0.9:
        #print("Your grade is A. AMAZING!!!")
        print("score: A")
    elif points_got >= max_points * 0.8:
        #print("Your grade is B. Pretty good!")
        print("score: B")
    elif points_got >= max_points * 0.7:
        #print("Your grade is C. Not bad!")
        print("score: C")
    elif points_got >= max_points * 0.6:
        #print("Your grade is D. You passed!")
        print("score: D")
    elif points_got < max_points * 0.6:
        #print("Your grade is F. You failed :(")
        print("score: F")


def sum_and_average():#4
    """Docstring here, sum and avg of inputs until they say done"""
    number1 = input("Give me a number: ")
    count = 1
    while number1 != "done":
        number2 = input("Give me another number or type \"done\" to calculate: ")
        if number2 != "done":
            number1 = float(number1)
            number1 += float(number2)
            count += 1
        else:
            average = number1 / count
            print("The sum of your number(s) is ", round(number1,2), " and the average is ", round(average,2), ".")
            number1 = "done"


def hyphen_string():#5
    """Docstring here, exxttteeeennnnndddddeeeeeerrrrrrrr with dashes"""
    extender = input("Give me a word and I will extend it for the lulz: ")
    string = ""
    counter = 0
    for letter in extender:
        counter += 1
        mult = letter * counter
        string += mult + "-"
        #Fix no - at the end.
    string = string.rstrip(string[-1])
    print(string)


def compare_numbers():#6
    """Docstring here, compare two numbers"""
    input1 = str(input("Enter something: "))
    temporary = input1
    while input1 != "done":
        input1 = str(input("Enter something again: "))
        if input1.isdigit():
            if input1.isdigit():
                if int(temporary) < int(input1):
                    print("larger!")
                    temporary = input1
                elif int(temporary) > int(input1):
                    print("smaller!")
                    temporary = input1
                elif int(temporary) == int(input1):
                    print("same!")
                    temporary = input1
                else:
                    print("How did you get here?")
        else:
            print("not a number!")


def validate_ssn():#7
    """Docstring here, uses some algorythm to calculate sum of numbers and see if modulus 10 is 0"""
    personal_number = str(input("Give me a SSN and I will check if its valid "))
    personal_number = str(personal_number)
    personal_number = personal_number.replace("-", "")
    pn_strip = personal_number.replace(" ", "")
    calc = 0 
    if len(str(pn_strip)) == 10:
        if pn_strip.isdigit():
            calc = 0
            temp = 0
            multiplier = 2
            for single in pn_strip:
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
        divide = calc % 10
        if divide == 0:
            print( "Valid")
        else:
            print( "Not valid") 
    


def robber_language():#8
    """Docstring here, baby language"""
    to_translate = str(input("Give me some words to translate: "))
    translated = ""
    consonants = "bcdfghjklmnpqrstvwxz"
    for letter23 in to_translate:
        if letter23 in consonants:
            translated += letter23 + "o" + letter23
        else:
            translated += letter23
    print(translated)


def a1_extra():#a1
    """Docstring here, extra, checks if string inide string"""
    entire = str(input("Give me a word: "))
    is_it_inside = str(input("Give me another word: "))
    
    valid = False
    for howmanyi in is_it_inside:
        if howmanyi in entire:
            entire = entire.replace(howmanyi, "", 1)
            valid = True
        else:
            valid = False
            break
    
    if valid is True:
        print("Match!")
    else:
        print("No match!")


def a2_extra():#a2
    """Docstring here, double it until contains all 0-9 digits with max tries as second input"""
    starting_number = str(input("Give me a starting number to double until it contains all numbers 0-9: "))
    total_tries = int(input("How many times max should i try to double it? ")) 
    counter = -1
    string = ""
    x_amount = 1
    y_amount = 0
    while x_amount <= total_tries:
        for whyuniquei in starting_number:
            if whyuniquei not in string:
                string += whyuniquei
        if len(str(string)) == 10:
            x_amount = total_tries + 1
            y_amount = 1
        starting_number = int(starting_number)
        starting_number *= 2
        starting_number = str(starting_number)
        string = starting_number
        x_amount += 1
        counter += 1
        string = ""
    if y_amount == 1:
        printthis = "" + str(counter)
        printthis = printthis.replace(" ", "")
        print("Answer:",printthis, "times")
    else:
        print("Answer: -1 times") 


def a3_extra():#a3
    """Docstring here, combine 2 names in a weird way cuz if it starts with a vowel it sound weird."""
    name1 = str(input("Give me the first name: "))
    name2 = str(input("Give me the second name: ")) 
    vowels = "aeiouy"
    counter = 0
    counter2 = 0

    for fortheloveofgod in name1.lower():
        counter += 1
        if fortheloveofgod in vowels:
            break
    name1 = name1[0:counter-1]
    #print(name1)
    
    for fortheloveofgod in name2.lower():
        counter2 += 1
        if fortheloveofgod in vowels:
            break
    name2 = name2[counter2-1:]
    combined_names = name1 + name2
    print(combined_names)

def a4_extra():#a4
    """Docstring here, only input single digit score per player but it works as intended"""
    input1 = str(input("Give me players and their scores in this format \
(capital is subtract, lowercase is add points) A1b2g5G1a4: "))
    def calculate_scores(input_str):
        """This function calculates stuff..."""
        player_dictionary = {}
        for i in range(0, len(input_str),2):   
            current_player = input_str[i]
            current_score = input_str[i+1]
            if current_player.islower():
                player_dictionary[current_player] = \
                    int(player_dictionary.get(current_player, 0)) + int(current_score)
            elif current_player.isupper():
                current_player = current_player.lower()
                player_dictionary[current_player] = \
                    int(player_dictionary.get(current_player, 0)) - int(current_score)
        formatted_scores = [f'{current_player} {current_score}' \
                            for current_player, current_score in player_dictionary.items()]
        return ', '.join(formatted_scores)

    output = calculate_scores(input1)
    print(output)
