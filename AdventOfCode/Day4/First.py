#Left is Winning numbers, Right is numbers we have.
open_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day4/Data.txt","r")
line = open_file.readline()
where_line = line.find("|")
where_semicolon = line.find(":")
print(where_line,where_semicolon)
total_total = 0
while True:
    correct_counter = 0
    first = line[where_semicolon+2:where_line].rstrip("\n").split(" ")
    last = line[where_line+2:].rstrip("\n").split(" ")
    for i in first:
        if i != "":
            for j in last:
                if i == j:
                    correct_counter +=1
    if correct_counter > 1:
        times = correct_counter -1
        result = 2**times
        total_total += result
    if correct_counter == 1:
        total_total += correct_counter

    line = open_file.readline()
    if line == "":
        break
print(total_total)


#First correct is +1 points, any other are *2 points.
