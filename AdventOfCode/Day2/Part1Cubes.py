# MAX 12 red cubes, 13 green cubes, and 14 blue cubes

open_input = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day2/PuzzleInput.txt", "r")

def limit(colour):
    if colour == "r":
        return 12
    if colour == "g":
        return 13
    if colour == "b":
        return 14

total_total = 0
while True:
    line = open_input.readline()
    while line != "":
        we_break = 0
        indexx = 0
        counter = 0
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
            if int(firstnr[:-2]) > limit(firstnr[-1]):
                we_break = 1
                break
        if we_break == 0:
            total_total += int(row_number)
        if indexx == -1:
            print("line done")
            counter += 1
        break
    if int(row_number) == 100:
        break
print(total_total)