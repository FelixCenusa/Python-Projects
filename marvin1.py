#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fake GPT with a simple menu to start up with.
Fake GPT doesnt do anything, just presents a menu with some choices.
You should add functinoality to Fake GPT.
This program was made by Felix Cenusa, BTH student Software Engineering 2023-2026, this program is the beginning of a series of "marvin" programs.
"""

FakeGPT_image = r"""
  █████▒▄▄▄       ██ ▄█▀▓█████      ▄████  ██▓███  ▄▄▄█████▓
▓██   ▒▒████▄     ██▄█▒ ▓█   ▀     ██▒ ▀█▒▓██░  ██▒▓  ██▒ ▓▒
▒████ ░▒██  ▀█▄  ▓███▄░ ▒███      ▒██░▄▄▄░▓██░ ██▓▒▒ ▓██░ ▒░
░▓█▒  ░░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄    ░▓█  ██▓▒██▄█▓▒ ▒░ ▓██▓ ░ 
░▒█░    ▓█   ▓██▒▒██▒ █▄░▒████▒   ░▒▓███▀▒▒██▒ ░  ░  ▒██▒ ░ 
 ▒ ░    ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░    ░▒   ▒ ▒▓▒░ ░  ░  ▒ ░░   
 ░       ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░     ░   ░ ░▒ ░         ░    
 ░ ░     ░   ▒   ░ ░░ ░    ░      ░ ░   ░ ░░         ░      
             ░  ░░  ░      ░  ░         ░                   
                                                            
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
stop = False
while not stop:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(FakeGPT_image)
    print("Hi, I'm Fake GPT. I know it all. What can I do you for?")
    print("1) Present yourself to Fake GPT.")
    print("2) Change temperature units from Celcius to Farenheit.")
    print("3) Points on a grade.")
    print("4) Sum and Average of numbers.")
    print("5) Exxttteeeennnnnddddddeeeeeeerrrrrrrr!!!!!!!!!.")
    print("6) Number comparator.")
    print("7) Personal number validator.")
    print("8) Translate to the Robber's language")
    print("a1) Imput inside match.")
    print("a2) Double it and give it to the next person?")
    print("a3) Name combiner.")
    print("a4) Player points calculator.")
    print("q) Quit.")
    

    choice = input("--> ")

    if choice == "q":
        print("Bye, bye - and welcome back anytime!")
        stop = True

    elif choice == "1":
        name = input("What is your name? ")
        print("\nFake GPT says:\n")
        print(f"Hello {name} - your awesomeness!")
        print("What can I do you for?!")
    
    elif choice == "2":
        celcius = float(input("Enter temperature in Celcius: "))
        farenheit = celcius * 1.8 + 32
        print("the temperature in Farenheit is: ",  round(farenheit, 2))

    elif choice == "3":
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

    elif choice == "4":
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
    
#rundll32.exe user32.dll,LockWorkStation 
#Still need to add exeption handling in case they say done or q in the middle of a program.

    elif choice == "5":
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
        
    elif choice == "6":
        input1 = str(input("Enter something: "))
        x = input1

        while input1 != "done":
            input1 = str(input("Enter something again: "))
            if input1.isdigit():
                if input1.isdigit():
                    if int(x) < int(input1):
                        print("larger!")
                        x = input1
                    elif int(x) > int(input1):
                        print("smaller!")
                        x = input1
                    elif int(x) == int(input1):
                        print("same!")
                        x = input1
                    else:
                        print("How did you get here?")
            else:
                print("not a number!")

    elif choice == "7":
        pn = str(input("Write your personal number and I will see if its valid: "))
        pn = pn.replace("-", "")
        pn_strip = pn.replace(" ", "")
        valid = False
        if len(str(pn_strip)) == 10:
            valid = False
            if pn_strip.isdigit():
                calc = 0
                temp = 0
                multiplier = 2
                for single in pn_strip:
                    temp = int(single) * int(multiplier)
                    #print(temp)
                    #print("prunted temp above")
                    added = 0
                    if len(str(temp)) == 2:
                        temp = str(temp)
                        added = int(temp[0]) + int(temp[1])
                        #print(added)
                        #print("added print above")
                        calc += int(added)
                        multiplier = (multiplier % 2) + 1
                    else:
                        calc += int(temp)
                        multiplier = (multiplier % 2) + 1
                        #print(calc)
                        divide = 0
                        divide = calc % 10
                        if divide == 0:
                            valid = True      
        if valid is True:
            print("Valid")
        else:
            print("Not valid")

    elif choice == "8":
        to_translate = str(input("Give me some words to translate: "))
        translated = ""
        consonants = "bcdfghjklmnpqrstvwxz"
        for letter23 in to_translate:
            if letter23 in consonants:
                translated += letter23 + "o" + letter23
            else:
                translated += letter23
        print(translated)

    elif choice == "a1":
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

            #Remove all the print statements

    elif choice == "a2":
        starting_number = str(input("Give me a starting number to double until it contains all numbers 0-9: "))
        total_tries = int(input("How many times max should i try to double it? ")) 
        counter = -1
        string = ""
        tracker = ""
        x = 1
        y = 0
        while x <= total_tries:
            for whyuniquei in starting_number:
                if whyuniquei not in string:
                    string += whyuniquei
            if len(str(string)) == 10:
                x = total_tries + 1
                y = 1
            starting_number = int(starting_number)
            starting_number *= 2
            starting_number = str(starting_number)
            string = starting_number
            x += 1
            counter += 1
            string = ""
        if y == 1:
            printthis = "" + str(counter)
            printthis = printthis.replace(" ", "")
            print("Answer:",printthis, "times")
        else:
            print("Answer: -1 times") 

    elif choice == "a3":
        name1 = str(input("Give me the first name: "))
        name2 = str(input("Give me the second name: ")) 
        vowels = "aeiouy"
        counter = 0
        counter2 = 0

        for fortheloveofgod in name1.lower():
            counter += 1
            if fortheloveofgod in vowels:
                first_vowel = fortheloveofgod
                #print(first_vowel)
                break
        name1 = name1[0:counter-1]
        #print(name1)
        
        for fortheloveofgod in name2.lower():
            counter2 += 1
            if fortheloveofgod in vowels:
                first_vowel = fortheloveofgod
                #print(first_vowel)
                break
        name2 = name2[counter2-1:]
        combined_names = name1 + name2
        print(combined_names)



    elif choice == "a4":
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

    
    


                
        

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    if not stop:
        input("\nPress enter to continue...")

"""
DONE!!!!!!!!!!! WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
"""