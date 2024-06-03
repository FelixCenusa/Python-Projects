opened_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day3/Text.txt","r")

#Now we make a simultaneous 3 line reader

line1 = opened_file.readline()
line2 = line1
limit = len(line1)
total_total = 0
while True:
    counter = 0
    line3 = opened_file.readline()
    if line3 == "":
        break
    #compare some stuff, line 2 is middle. 257656
    while counter < limit:
        number = ""
        valid = False
        cancel_counter = False
        line2char = line2[counter]
        while line2char in "0123456789":
            number +=line2char
            if line1[counter] in "*/@&$=#-+%": #up 
                valid = True
            if line3[counter] in "*/@&$=#-+%": #down
                valid = True
            if line2[counter-1] in "*/@&$=#-+%": #left
                valid = True
            if line2[counter+1] in "*/@&$=#-+%": #right
                valid = True
            if line1[counter-1] in "*/@&$=#-+%": #TOP LEFT
                valid = True
            if line1[counter+1] in "*/@&$=#-+%": #TOP RIGHT
                valid = True
            if line3[counter-1] in "*/@&$=#-+%": #BOTTOM LEFT
                valid = True
            if line3[counter+1] in "*/@&$=#-+%": #BOTTOM RIGHT
                valid = True

            counter += 1
            cancel_counter = True
            line2char = line2[counter]
        if cancel_counter == False:
            counter += 1
        if valid == True:
            total_total += int(number)

    #swap the lines:
    line1 = line2
    line2 = line3
print(total_total)