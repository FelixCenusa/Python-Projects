def get_nth_key(dictionary, n=0):
    try:
        if n < 0:
            n += len(dictionary)
        for i, value in enumerate(dictionary.values()):
            if i == n:
                return value
    except IndexError:
        print("dictionary index out of range") 

def alot(number,nr):
        this_x = line.find(number)
        start_at = this_x
        while this_x != -1:
            dict_here.update({this_x:nr})
            this_x = line.find(number,(start_at+1))
            start_at = this_x

file_name = "/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day1/CalibrationValuez"
#file_here = open(file_name, "r")

file_here = open(file_name, "r")
line = "temp"
file_here_temp = open("temporary_store.txt", "w")
total_total = 0
line_at = -1
while line != "":
    line_at += 1
    dict_here = {}
    indexxx = -1
    line = file_here.readline()
    line = line.rstrip("\n")   

    alot("one",1)
    alot("two",2)
    alot("three",3)
    alot("four",4)
    alot("five",5)
    alot("six",6)
    alot("seven",7)
    alot("eight",8)
    alot("nine",9)
    
    for i in line:
        indexxx += 1
        if i in "1234567890":
            dict_here.update({indexxx:i})
    dict_here = sorted(dict_here.items(), key=lambda x_case:x_case[0], reverse = False)
    dict_here = dict(dict_here)
    first = get_nth_key(dict_here,0)
    length = len(dict_here) - 1
    last = get_nth_key(dict_here,length)

    try:
        togethr = str(first) + str(last)
        total_total += int(togethr)
    except:
        print("Done!!")
    
print(total_total)
