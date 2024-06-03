# MAX 12 red cubes, 13 green cubes, and 14 blue cubes

open_input = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day2/PuzzleInput.txt", "r")

total_total = 0
while True:
    line = open_input.readline()
    while line != "":
        we_break = 0
        indexx = 0
        counter = 0
        current_max_r = 1
        current_max_g = 1
        current_max_b = 1
        row_number = line.find(" ")
        row_number = line[row_number+1:row_number+4]
        row_number = row_number.rstrip(" ")
        row_number = row_number.rstrip(":")
        print("Row Number: ", row_number)
        first_semicolon_index = line.find(":") 
        line = line[first_semicolon_index:]     
        while indexx != -1:
            indexx = line.find(" ")
            if indexx == -1:
                break
            line = line[indexx+1:]
            indexx = line.find(" ")
            firstnr = line[:indexx+2]
            line = line[indexx+2:]
            colour = firstnr[-1]
            amount = int(firstnr[:-2])
            if colour == "r":
                if amount > current_max_r:
                    current_max_r = amount
            if colour == "g":
                if amount > current_max_g:
                    current_max_g = amount
            if colour == "b":
                if amount > current_max_b:
                    current_max_b = amount
        total_total += (current_max_r*current_max_g*current_max_b)
        counter += 1
        break
    if int(row_number) == 100:
        break
print(total_total)