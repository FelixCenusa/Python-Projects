#Left is Winning numbers, Right is numbers we have.
open_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day4/Data.txt","r")
line = open_file.readline()
where_line = line.find("|")
where_semicolon = line.find(":")
print(where_line,where_semicolon)
total_total = 0
card_nr = 0
dict_here = {}
just_string = 0
ctr = 1
while ctr <= 201:
    dict_here.update({ctr:1})
    ctr += 1

def add_to_dict(key,value):
    test = dict_here.get(key)
    if type(test) == type(just_string):
        dict_here.pop(key)
        dict_here.update({key:value+test})
    else:
        dict_here.update({key:value})

while True:
    correct_counter = 0
    card_nr +=1
    first = line[where_semicolon+2:where_line].rstrip("\n").split(" ")
    last = line[where_line+2:].rstrip("\n").split(" ")
    for i in first:
        if i != "":
            for j in last:
                if i == j:
                    correct_counter +=1

    if correct_counter >= 1:
        repeat = 0
        times = dict_here.get(card_nr)
        while repeat < times:
            repeat += 1
            counter = 0
            while counter < correct_counter: #adds the next cards if correct
                counter += 1
                add_to_dict(card_nr+counter,1)


    line = open_file.readline()
    if line == "":
        break
values = dict_here.values()
for i in values:
    total_total+= i
print(total_total)



#First correct is +1 points, any other are *2 points.
