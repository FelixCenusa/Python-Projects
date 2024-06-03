opened_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day3/Text.txt","r")

line1 = "ok"
symbols = ""
while line1 != "":
    line1 = opened_file.readline()
    for i in line1:
        if i not in "01234567890.":
            if i not in symbols:
                symbols += i
print(symbols)