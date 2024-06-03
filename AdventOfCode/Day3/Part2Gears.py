opened_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day3/Text.txt","r")

#Now we make a simultaneous 3 line reader

line1 = opened_file.readline()
line2 = line1
limit = len(line1)
total_total = 0
linenr = 0
store_pairs = {}
just_string = ""
while True:
    counter = 0
    line3 = opened_file.readline()
    if line3 == "":
        break
    linenr += 1
    #compare some stuff, line 2 is middle. 257656
    while counter < limit:
        number = ""
        cancel_counter = False
        line2char = line2[counter]
        star_coord = ""
        while line2char in "0123456789":
            number +=line2char
            if line1[counter] in "*": #up 
                star_coord = f"{linenr-1},{counter}"
            if line3[counter] in "*": #down
                star_coord = f"{linenr+1},{counter}"
            if line2[counter-1] in "*": #left
                star_coord = f"{linenr},{counter-1}"
            if line2[counter+1] in "*": #right
                star_coord = f"{linenr},{counter+1}"
            if line1[counter-1] in "*": #TOP LEFT
                star_coord = f"{linenr-1},{counter-1}"
            if line1[counter+1] in "*": #TOP RIGHT
                star_coord = f"{linenr-1},{counter+1}"
            if line3[counter-1] in "*": #BOTTOM LEFT
                star_coord = f"{linenr+1},{counter-1}"
            if line3[counter+1] in "*": #BOTTOM RIGHT
                star_coord = f"{linenr+1},{counter+1}"
            counter += 1
            cancel_counter = True
            line2char = line2[counter]
        if star_coord != "":
            test = store_pairs.get(star_coord)
            if type(test) == type(just_string):
                total_total += int(test) * int(number)
                store_pairs.pop(star_coord)
            else:
                store_pairs.update({star_coord:number})

        if cancel_counter == False:
            counter += 1

    #swap the lines:
    line1 = line2
    line2 = line3
print(total_total)