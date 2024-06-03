"""This file contains all the functions that will be called by main.py"""
import os
import time
import random

def current_directory_func():
    """Change the current directory to your current directory.(where this file is located)"""
    current_directory = "typing/"
    return current_directory

def rows_total(file_name):
    """calculates how many rows total a file has."""
    with open(file_name) as file_here:
        line = "temp"
        rows = -1
        while line != "":
            line = file_here.readline()
            rows += 1
    return rows

def train_input(file_name):
    """gets the imput from the user and gives the text that the user should imput. also timer."""
    with open(file_name) as easy_txt:
        line = "temp"
        from_user_total = ""
        start_time = time.time() #START TIMER
        while True:
            line = easy_txt.readline()
            if line == "":
                break
            added = line
            if "\n" not in line:
                added += "\n"
            os.system("clear")
            #START TIMER
            from_user = input(added)
            from_user_total += from_user
            from_user_total += "\n"
        stop_time = time.time() #START TIMER
        timed = stop_time - start_time
    from_user_total = from_user_total.rstrip(from_user_total[-1])
    file_here = open(f"{current_directory_func()}train.txt", "w")
    file_here.write(from_user_total)
    file_here.close()
    os.system("clear")
    input("Congrats! You finished the training.\nPress enter to see statistics... ")
    os.system("clear")
    return timed

def train_results(file_name):
    """this is the heart of the program, where all the functions mingle with eachother. """
    timed = train_input(file_name)
    name_file = name_getter(file_name)
    line_train,line_here,minus_points_words,minus_points_letters,\
minus_letters_please,lines_train_clean = equalizer(file_name)
    both_correct_plus_wrong = correct_counter(line_train,line_here)
    word_precision,letter_precision,letters_wrong_dict,summed_w_a = the_calculator(\
file_name,both_correct_plus_wrong,\
minus_points_words,minus_points_letters,minus_letters_please)
    file_here = open(f"{current_directory_func()}too_many_arguments.txt", "w")
    file_here.write(str(summed_w_a))
    file_here.write("\n")
    file_here.write(str(lines_train_clean))
    file_here.write("\n")
    file_here.close()
    user_name = format_data(word_precision,letter_precision,letters_wrong_dict,\
timed,line_here)
    with open(f"{current_directory_func()}data.txt", "w") as data_file:
        data_file.write(f"{user_name}\n{word_precision}\n{name_file}")
    add_to_high_score()
    
def equalizer(file_name):
    """this makes sure that the user input has the same length\
 as the wanted imput so no errors appear"""
    rows_here = rows_total(file_name)
    just_file = open(file_name, "r")
    train_file = open(f"{current_directory_func()}train.txt", "r")
    counter = 0
    lines_train = ""
    lines_train_clean = []
    lines_here = ""
    minus_points_words = 0
    minus_points_letters = 0
    minus_letters_please = ""
    while counter < rows_here:
        line_here  = just_file.readline()
        line_train = train_file.readline()
        lines_here += line_here
        line_here = line_here.rstrip("\n")
        line_here = line_here.split(" ")
        line_train = line_train.rstrip("\n")
        line_train = line_train.split(" ")
        lines_train_clean += line_train
        counter_again = 0
        words_line_train = ""
        while True:
            while len(line_train) < len(line_here):
                line_train.append("")
                if len(line_train) == len(line_here):
                    break
            while len(line_train) > len(line_here):
                minus_letters_please += str(line_train[-1])
                line_train.pop(-1)
                minus_points_words += -1
                if len(line_train) == len(line_here):
                    break
            if len(line_train) == len(line_here):
                break
        while counter_again < len(line_here):
            word_train = line_train[counter_again]
            word_og = line_here[counter_again]
            while len(word_train) != len(word_og):
                if len(word_train) > len(word_og):
                    word_train = word_train[0:-1]
                    minus_points_letters += -1
                    if len(word_train) == len(word_og):
                        word_train += "0"#False positive fixer
                        break
                elif len(word_train) < len(word_og):
                    word_train += choose_add(word_train,word_og)# fix in case a 0 does come up
            words_line_train += word_train
            words_line_train += " "
            counter_again += 1
        words_line_train = words_line_train.rstrip(words_line_train[-1])
        lines_train += words_line_train
        lines_train += "\n"
        counter += 1
    lines_train = lines_train.rstrip(lines_train[-1])
    return (lines_train,lines_here,minus_points_words,minus_points_letters,minus_letters_please,lines_train_clean)

def choose_add(word_train,word_og):
    """this gets rid of a false positive in case that the letter missing is actually 0"""
    len_word_train = len(word_train)
    len_word_og = len(word_og)
    if len_word_train < len_word_og:
        index = len_word_train
        if word_og[index] == "0":
            word_train = "1"
        else:
            word_train = "0"
    return word_train


def correct_counter(whole_train,whole_og):
    """this counts how many correct words and letters there are."""
    whole_train = whole_train.split("\n")
    whole_og = whole_og.split("\n")
    correct_letter_counter = ""
    wrong_letter_counter = ""
    correct_word_counter = ""
    counter_fourth = 0
    while counter_fourth < len(whole_og):
        sentance_og = str(whole_og[counter_fourth])
        sentance_train = str(whole_train[counter_fourth])
        counter_again = 0
        while counter_again < len(sentance_og.split(" ")):
            words_og = str(sentance_og.split(" ")[counter_again])
            words_train = str(sentance_train.split(" ")[counter_again])
            if words_train == words_og:
                correct_word_counter += "1"
                correct_letter_counter += words_train
            counter_third = 0
            if words_train != words_og:
                correct_word_counter += "0"
                while counter_third < len(words_og):
                    letters_og = words_og[counter_third]
                    letters_train = words_train[counter_third]
                    if letters_og == letters_train:
                        correct_letter_counter += letters_train
                    else:
                        wrong_letter_counter += letters_og
                    counter_third += 1
            counter_again += 1
        counter_fourth += 1
        both_correct_plus_wrong = []
        both_correct_plus_wrong.append(correct_word_counter)
        both_correct_plus_wrong.append(correct_letter_counter)
        both_correct_plus_wrong.append(wrong_letter_counter)
    return (both_correct_plus_wrong)
            

def total_counter(file_name):
    """this counts the total lettesr and total words in the original file so we \
can calculate a percenage of correct words and letters later down the line"""
    just_file = open(file_name, "r")
    lines_here = ""
    for i in range(0,rows_total(file_name)):
        line_here  = just_file.readline()
        line_here = line_here.rstrip("\n")
        lines_here += line_here
        lines_here += " "
    total_words_amount = len(lines_here.split(" ")) - 1
    total_letters = ""
    for i in range (0, total_words_amount):
        words = lines_here.split(" ")[i]
        new_stored = words.rstrip(" ")
        total_letters += new_stored
    total_letters_amount = len(total_letters)
    just_file.close()
    return (total_letters_amount,total_words_amount)



def the_calculator(file_name,both_correct_plus_wrong\
,minus_points_words,minus_points_letters,minus_letters_please):
    """this calculates word and letter precision, also makes \
a dictionary with the wrong letters to be used later, and sends the \
word accuracy to another function for another use"""
    words_correct = both_correct_plus_wrong[0] 
    letters_correct = both_correct_plus_wrong[1]
    letters_wrong = both_correct_plus_wrong[2]
    total_letters_amount,total_words_amount = total_counter(file_name)
    added_w_c = 0
    for i in words_correct:
        added_w_c += int(i)
    summed_w_a = added_w_c + minus_points_words
    summed_l_a = len(letters_correct) + minus_points_letters - len(minus_letters_please)

    word_precision = str(round((( summed_w_a / total_words_amount)*100),2))+"%"
    letter_precision = str(round(((summed_l_a / total_letters_amount)*100),2))+"%"
    letters_wrong_dict = {}
    worked = 0
    for i in letters_wrong:
        value_try = letters_wrong_dict.get(i)
        try:
            ok_case = int(value_try) + 1
            worked = ok_case - ok_case + 1
        except TypeError:
            worked = 0
        if worked == 1:
            amount = value_try + 1
            letters_wrong_dict.update({i : amount})
        if worked != 1:
            letters_wrong_dict.update({i : 1})
    letters_wrong_dict = sorted(letters_wrong_dict.items(), key=lambda x_case:x_case[0], reverse = False)
    letters_wrong_dict = dict(letters_wrong_dict)
    letters_wrong_dict = sorted(letters_wrong_dict.items(), key=lambda x_case:x_case[1], reverse = True)
    return (word_precision,letter_precision,letters_wrong_dict,summed_w_a)

def format_data(word_precision,letter_precision,letters_wrong_dict,timed,line_here):
    """this just prints the data in the way that was required. makes it nice."""
    file_here = open(f"{current_directory_func()}too_many_arguments.txt", "r")
    summed_w_a = file_here.readline()
    summed_w_a = int(summed_w_a[0:-1])
    lines_train_clean = file_here.readline()
    lines_train_clean = lines_train_clean[0:-1]
    lines_train_clean = lines_train_clean[1:-1]
    lines_train_clean = lines_train_clean.split(",")
    lines_train_cleaned = []
    for i in lines_train_clean:
        if i[0] == " ":
            i = i[1:]
        lines_train_cleaned.append(i[1:-1])
    lines_train_clean = lines_train_cleaned
    file_here.close()
    
    print(f"-----Here are your results!!!-----\nWord precission:{word_precision}\
\nLetter precision: {letter_precision}\nMisspelled letters: ")
    for i in letters_wrong_dict:
        string_i = str(i)
        letter_i = string_i[2]
        amount_i = string_i[6:]
        amount_i = amount_i[:-1]
        print(f"{letter_i}: {amount_i}")
    print("")
    minutes = int(timed // 60)
    seconds = round((timed % 60),1)
    plural_or = "minutes"
    if minutes == 1:
        plural_or = "minute"
    print(f"It took you {minutes} {plural_or} and {seconds} seconds to type all that text.")
    all_lines = []
    for i in line_here.split("\n"):
        single_line = i.split(" ")
        all_lines += single_line
    total_words = len(all_lines)
    typed_words = len(lines_train_clean)

    if seconds > 30:
        seconds = 0
        minutes += 1
    if seconds < 30:
        seconds = 0
    if minutes == 0:
        minutes = 1
    new_seconds = (minutes * 60) + seconds
    gross_wpm = (typed_words / new_seconds) * 60
    net_wpm = gross_wpm - (((total_words-summed_w_a) / new_seconds) * 60)
    animal = "Sengångare"
    if 10 <= net_wpm < 20:
        animal = "Snigel"
    if 20 <= net_wpm < 30:
        animal = "Sjöko"
    if 30 <= net_wpm < 40:
        animal = "Människa"
    if 40 <= net_wpm < 50:
        animal = "Gasell"
    if 50 <= net_wpm < 60:
        animal = "Struts"
    if 60 <= net_wpm < 70:
        animal = "Gepard"
    if 70 <= net_wpm < 80:
        animal = "Svärdfisk"
    if 80 <= net_wpm < 90:
        animal = "Sporrgås"
    if 90 <= net_wpm < 100:
        animal = "Taggstjärtseglare"
    if 100 <= net_wpm < 120:
        animal = "Kungsörn"
    if net_wpm >= 120:
        animal = "Pilgrimsfalk"

    print(f"Growss WPM: {round(gross_wpm,1)}")
    print(f"Net WPM: {round(net_wpm,1)}")
    print(f"You type as fast as a {animal}")

    user_name = input("Enter a username to add to the High Score!: ")
    return user_name

def name_getter(file_name):
    """this gets the name of a file, useful also if there is \
longer directories then just eg: easy.txt"""
    name = file_name
    if "easy" in name:
        name = "easy"
    elif "medium" in name:
        name = "medium"
    elif "hard" in name:
        name = "hard"
    else:
        name = ""
    return name
    

def train_easy():
    """train_results does the work, but it needs to know with what file to work."""
    train_results(f"{current_directory_func()}easy.txt")

def train_medium():
    """train_results does the work, but it needs to know with what file to work."""
    train_results(f"{current_directory_func()}medium.txt")

def train_hard():
    """train_results does the work, but it needs to know with what file to work."""
    train_results(f"{current_directory_func()}hard.txt")


def add_to_high_score():
    """this adds to and sorts the high-score file to be printed later on if wanted."""
    with open(f"{current_directory_func()}data.txt", "r") as data_file:
        user_name = str(data_file.readline())[0:-1]
        word_precision = str(data_file.readline())[0:-1]
        name_file = str(data_file.readline())
    file_here = open(f"{current_directory_func()}score.txt", "a")
    if len(user_name) > 7:
        user_name = user_name[0:6]
    while len(user_name) < 7:
        user_name += " "
    if len(word_precision) > 8:
        word_precision = word_precision[0:7]
    while len(word_precision) < 8:
        word_precision += " "
    file_here.write(f"{user_name} {word_precision}{name_file}\n")
    file_here.close()
    file_here = open(f"{current_directory_func()}score.txt", "r")
    whole_high_score = file_here.read()
    file_here.close()
    whole_high_score = whole_high_score.split("\n")
    whole_high_score.pop(-1)
    low_score = 0
    sorted_score = []
    stored_scores = []
    store_score = ""
    while True:
        for i in whole_high_score:
            if float(str(i)[8:12].rstrip().rstrip("%")) >= low_score:
                if i not in stored_scores:
                    low_score = float(str(i)[8:12].rstrip().rstrip("%"))
                    store_score = str(i)
        sorted_score.append(low_score)
        stored_scores.append(store_score)
        low_score = 0
        if len(sorted_score) == len(whole_high_score):
            break
    newly_sorted = ""
    for i in stored_scores:
        if i[-1] in "d":
            newly_sorted += i
            newly_sorted += "\n"
    for i in stored_scores:
        if i[-1] in "m":
            newly_sorted += i
            newly_sorted += "\n"
    for i in stored_scores:
        if i[-1] in "y":
            newly_sorted += i
            newly_sorted += "\n"
    file_here = open(f"{current_directory_func()}score.txt", "w")
    file_here.write(newly_sorted)
    file_here.close()
    

    #Sort them by most importantly, difficulty, then the percentage words correct.

def see_high_score():
    """this prints the high-score that was stored inthe hiiiigh_score.txt file. already sorted."""
    excepted = 0
    try:
        file_here = open(f"{current_directory_func()}score.txt", "r")
        file_here.close()
    except FileNotFoundError:
        print("No high-scores exist yet! Practice some!")
        excepted = 1
    if excepted == 0:
        file_here = open(f"{current_directory_func()}score.txt", "r")
        print("")
        print(file_here.read())


def practice():
    """This is the extra practice task that I thought gave no extra points so here it is:) fully functional."""
    amount_of_seconds = input("how long should the test last?")
    start_here = time.time()
    correct_counter_here = 0
    dict_of_wrong = {}
    worked = 0
    total_counter_here = 0
    while (time.time()-start_here) < int(amount_of_seconds):
        total_counter_here += 1
        os.system("clear")
        string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!\"£$%^&*()_+¨€[]'#@~/?,.<>"
        random_thing = random.choice(string)
        random_plus = random_thing + "\n"
        from_user = str(input(random_plus))
        if random_thing == from_user:
            correct_counter_here += 1
        if random_thing != from_user: 
            take_it = dict_of_wrong.get(random_thing)
            worked = 1
            if take_it is None:
                dict_of_wrong.update({random_thing:1})
                worked = 0
            if worked == 1:
                dict_of_wrong.update({random_thing:(int(take_it)+1)})
                worked = 0
    percent = correct_counter_here / total_counter_here * 100
    wrong_percent = 100 - percent
    dict_of_wrong = sorted(dict_of_wrong.items(), key=lambda x_case:x_case[0], reverse = False)
    dict_of_wrong = dict(dict_of_wrong)
    dict_of_wrong = sorted(dict_of_wrong.items(), key=lambda x_case:x_case[1], reverse = True)
    os.system("clear")
    print(f"Incorrect percentage: {round(wrong_percent,2)}%")
    cpm = total_counter_here / int(amount_of_seconds) * 60
    print(f"Typed characters per minute: {cpm}")
    print("Wrongly spelled letters: ")
    for i in dict_of_wrong:
        string_i = str(i)
        letter_i = string_i[2]
        amount_i = string_i[6:]
        amount_i = amount_i[:-1]
        print(f"{letter_i}: {amount_i}")
