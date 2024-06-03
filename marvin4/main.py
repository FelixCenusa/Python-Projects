#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ofcourse im missing dosctring. This is to run marvin.."""

import marvin1 as m1
import marvin2 as m2
import inventory as inv
import emission_functions as ef

"""Ofcourse im missing dosctring. This is to run marvin.."""
def main():
    """
    Fake GPT with a simple menu to start up with.
    Fake GPT doesnt do anything, just presents a menu with some choices.
    You should add functinoality to Fake GPT.
    This program has been made by Felix Beniamin Cenusa BTH student Software Engineering 2023-2026 and is the final version of the "Marvin" program that I call Fake-GPT.
    """
    backpack = []

    fakegpt_image = r"""
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
        print(fakegpt_image)
        print("Hi, I'm Fake GPT. I know it all. What can I do you for?")
        print("1) Present yourself to Fake GPT.")
        print("2) Change temperature units from Celcius to Farenheit.")
        print("3) Points on a grade.")
        print("4) Sum and Average of numbers.")
        print("5) Exxttteeeennnnnddddddeeeeeeerrrrrrrr!!!!!!!!!.")
        print("6) Number comparator.")
        print("7) Personal number validator.")
        print("8) Translate to the Robber's language.")
        print("9) Create valid SSN.")
        print("10) Acronym maker.")
        print("11) Randomize string.")
        print("12) Find all indexes.")
        print("a1) Imput inside match.")
        print("a2) Double it and give it to the next person?")
        print("a3) Name combiner.")
        print("a4) Player points calculator.")
        print("inv) Access backpack!")
        print("inv pick .. ..) Pick X from floor and place it in Y ")
        print("inv drop) Drop from backpack.")
        print("inv swap) Swap two items in the backpack")
        print("13) Find countries in the data.(case sensitive)")
        print("14) Show change in emmision of a country")
        print("15) Print country data")


        print("q) Quit.")
        

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            stop = True

        elif choice == "1":
            m1.greet()
        
        elif choice == "2":
            m1.celcius_to_fahrenheit()

        elif choice == "3":
            m1.points_to_grade()

        elif choice == "4":
            m1.sum_and_average()
        
    #rundll32.exe user32.dll,LockWorkStation 
    #Still need to add exeption handling in case they say done or q in the middle of a program.

        elif choice == "5":
            m1.hyphen_string()
            
        elif choice == "6":
            m1.compare_numbers()

        elif choice == "7":
            m1.validate_ssn()

        elif choice == "8":
            m1.robber_language()

        elif choice == "9":
            print(m2.create_ssn(str(input("Give me YYMMDD and I will make you a valid SSN: "))))

        elif choice == "10":
            print(m2.get_acronym(input("Give me some words with capital letters and I will make an acronym: ")))
        
        elif choice == "11":
            print(m2.randomize_string(input("Give me some words and I will rnadomize them: ")))
        
        elif choice == "12":
            print(m2.find_all_indexes(input("Give me a long string of letters: "),\
input("Give me a letter that is inside the other string and I will check its index: ")))

        elif choice == "a1":
            m1.a1_extra()

        elif choice == "a2":
            m1.a2_extra()

        elif choice == "a3":
            m1.a3_extra()

        elif choice == "a4":
            m1.a4_extra()

        
        elif "inv pick" in choice.lower():
            splitted = choice.split(" ")
            if len(splitted) == 4:
                index = splitted[3]
            elif len(splitted) == 3:
                index = int(len(backpack))
            element = str(splitted[2])
            inv.pick(backpack, element, index)

        elif "inv drop" in choice.lower():
            splitted_again = choice.split(" ")
            if len(splitted_again) == 3:
                inv.drop(backpack, splitted_again[2])

        elif "inv swap" in choice.lower():
            splitted_third = choice.split(" ")
            if len(splitted_third) == 4:
                inv.swap(backpack, splitted_third[2],splitted_third[3])

        
        elif choice.lower() == "inv":
            inv.inventory(backpack)
    
        elif choice.lower() == "inv drop":
            inv.drop(backpack, input("What do you want to drop from the backpack?: "))

        elif choice == "13":
            try:
                stored2 = ef.search_country(input("Give me a input: "))
                print("Following countries were found:",stored2)
            except ValueError:
                print("Country does not exist!")
                
            
        elif choice == "14":
            all_here = input("Give me a country and year(s)")
            all_split = all_here.split(",")
            if len(all_split) == 2: #14.1
                country = all_split[0]
                year = str(all_split[1])
                try:
                    print(ef.get_country_year_data_megaton(country, year))
                except ValueError:
                    print("Invalid year")
            elif len(all_split) == 3: #14.2
                country = all_split[0]
                from_year = str(all_split[1])
                to_year = str(all_split[2])
                try:
                    result = ef.get_country_change_for_years(country,from_year, to_year)
                    if "Value" in str(result):
                        print("Wrong year!")
                    else:
                        format_here = country + ":" + str(result) + "%"
                        print(format_here)
                except ValueError as error:
                    print(error)
                    print("Wrong year!")
                except Exception:
                    print("Wrong year! everything!")
                    


        elif choice == "15":
            here = ef.print_country_data(ef.get_country_data(input("Give me a country: ")))
            print(here)


                    
            

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        if not stop:
            input("\nPress enter to continue...")

    """
    DONE!!!!!!!!!!! WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    """

if __name__ == "__main__":
    main()
