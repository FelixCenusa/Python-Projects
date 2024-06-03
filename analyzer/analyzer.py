"""HELLO IM HERE"""

#make:
#Lines
#Words
#Letters analyzer from both lorum and phil,
# but phil should be selected when start        
def lines(x_case):#legit
    """here is my module dosctring, title is descriptive."""
    current_selected = x_case
    with open(current_selected) as current_file:
        rows = -1
        line = "temp"
        while line != "":
            line = current_file.readline()
            rows += 1
    return rows

def words(y_case):#legit
    """here is my module dosctring, title is descriptive."""
    current_selected = y_case
    with open(current_selected) as current_file:
        words_a = 0
        line = "temp"
        while line != "":
            line = current_file.readline()
            for i in line:
                if i == " ":
                    words_a += 1
        words_a += int(lines(y_case))
    return words_a

def letters(z_case):#legit
    """here is my module dosctring, title is descriptive."""
    letters_here = int(characters(z_case)) - int(words(z_case))
    letters_here -= (int(lines(z_case))*2)
    letters_here -= (int(special(z_case)))

    return letters_here

def characters(w_case):#personal
    """here is my module dosctring, title is descriptive."""
    current_selected = w_case
    with open(current_selected) as current_file:
        characters_oops = 0
        line = "temp"
        while line != "":
            line = current_file.readline()
            for _ in line:
                characters_oops += 1
        return characters_oops

def special(w1case):#personal
    """here is my module dosctring, title is descriptive."""
    current_selected = w1case
    with open(current_selected) as current_file:
        specials = 0
        line = "temp"
        while line != "":
            line = current_file.readline()
            for i in line:
                if i == "-":
                    specials += 1
    return specials


def just_words(w3case):#personal
    """here is my module dosctring, title is descriptive."""
    current_selected = w3case
    with open(current_selected) as current_file:
        string_words = ""
        line = "temp"
        while line != "":
            line = current_file.readline()
            string_words += line
        string_words = string_words.replace("\n"," ")
        string_words = string_words.replace(".","")
        string_words = string_words.replace(",","")
        string_words = string_words.lower()
    return string_words

def word_list(w4case):#personal
    """here is my module dosctring, title is descriptive."""
    words_here = just_words(w4case)
    words_here = words_here.split(" ")
    return words_here
    
def word_frequency_not_format(w5case):#personal
    """here is my module dosctring, title is descriptive."""
    stored_list = word_list(w5case)
    sorted_list = sorted(stored_list)
    x_case = "aaaaaaa aaaaa"
    dict_here = {}
    counter = 1
    careful = False
    for i in sorted_list:
        if x_case == i:
            counter += 1
            dict_here[x_case] = counter
            careful = True
        if x_case != i:
            if careful is False:
                dict_here[x_case] = 1
                counter = 1
            if careful is True:
                counter = 1
                careful = False
        x_case = i
    if careful is False:
        dict_here[x_case] = 1
    dict_here = sorted(dict_here.items(), key=lambda x_case:x_case[0], reverse = True)
    dict_here = dict(dict_here)
    sorted_dict = sorted(dict_here.items(), key=lambda x_case:x_case[1], reverse = True)
    return sorted_dict

def letter_list(w6case):#personal
    """here is my module dosctring, title is descriptive."""
    words_here = just_words(w6case)
    words_here = words_here.replace(" ","")
    words_here = words_here.replace("-","")
    just_letters = words_here.lower()
    return just_letters

def letter_frequency_not_format(w7case):#personal
    """here is my module dosctring, title is descriptive."""
    stored_letters = letter_list(w7case)
    sorted_list = sorted(stored_letters)
    x_cases = "aaaaaaa aaaaa"
    dict_here = {}
    counter = 1
    careful = False
    for i in sorted_list:
        if x_cases == i:
            counter += 1
            dict_here[x_cases] = counter
            careful = True
        if x_cases != i:
            if careful is False:
                dict_here[x_cases] = 1
                counter = 1
            if careful is True:
                counter = 1
                careful = False
        x_cases = i
    if careful is False:
        dict_here[x_cases] = 1

    dict_here = sorted(dict_here.items(), key=lambda x_cases:x_cases[0], reverse = True)
    dict_here = dict(dict_here)
    sorted_dict = sorted(dict_here.items(), key=lambda x_cases:x_cases[1], reverse = True)
    return sorted_dict

def percent_word(w8case):#personal
    """here is my module dosctring, title is descriptive."""
    words_here = words(w8case)
    word_frequency_here = dict(word_frequency_not_format(w8case))
    list_values = word_frequency_here.values()
    percent = []
    for i in list_values:
        percent.append(str(round((1 / (int(words_here) / int(i))*100),1)))
    return percent

def percent_letter(w9case):#personal
    """here is my module dosctring, title is descriptive."""
    letters_here = letters(w9case)
    letter_frequency_here = dict(letter_frequency_not_format(w9case))
    list_values = letter_frequency_here.values()
    percent = []
    for i in list_values:
        percent.append(str(round((1 / (int(letters_here) / int(i))*100),1)))
    return percent

def word_frequency(w10case):#legit
    """here is my module dosctring, title is descriptive."""
    stored = word_frequency_not_format(w10case)
    percent = percent_word(w10case)
    stored_words = dict(stored).keys()
    stored_words = list(stored_words)
    stored_amounts = dict(stored).values()
    stored_amounts = list(stored_amounts)
    formatted =f"{stored_words[0]}: {stored_amounts[0]} | {percent[0]}%\n\
{stored_words[1]}: {stored_amounts[1]} | {percent[1]}%\n\
{stored_words[2]}: {stored_amounts[2]} | {percent[2]}%\n\
{stored_words[3]}: {stored_amounts[3]} | {percent[3]}%\n\
{stored_words[4]}: {stored_amounts[4]} | {percent[4]}%\n\
{stored_words[5]}: {stored_amounts[5]} | {percent[5]}%\n\
{stored_words[6]}: {stored_amounts[6]} | {percent[6]}%"
    return formatted


def letter_frequency(w11case):#legit
    """here is my module dosctring, title is descriptive."""
    stored = letter_frequency_not_format(w11case)
    percent = percent_letter(w11case)
    stored_letters = dict(stored).keys()
    stored_letters = list(stored_letters)
    stored_amounts = dict(stored).values()
    stored_amounts = list(stored_amounts)
    formatted =f"{stored_letters[0]}: {stored_amounts[0]} | {percent[0]}%\n\
{stored_letters[1]}: {stored_amounts[1]} | {percent[1]}%\n\
{stored_letters[2]}: {stored_amounts[2]} | {percent[2]}%\n\
{stored_letters[3]}: {stored_amounts[3]} | {percent[3]}%\n\
{stored_letters[4]}: {stored_amounts[4]} | {percent[4]}%\n\
{stored_letters[5]}: {stored_amounts[5]} | {percent[5]}%\n\
{stored_letters[6]}: {stored_amounts[6]} | {percent[6]}%"
    return formatted

def all_att_once(wlastcase):#legit
    """here is my module dosctring, title is descriptive."""
    formatted = f"{lines(wlastcase)}\n\
{words(wlastcase)}\n{letters(wlastcase)}\n\
{word_frequency(wlastcase)}\n\
{letter_frequency(wlastcase)}"
    return formatted
