calibrate = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day1/CalibrationValuez", "r")
temp_store = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day1/temporary_store.txt","w")

while True:
    line = "temp"
    while line != "":
        line = calibrate.readline()
        for i in line:
            if i in "123456789":
                temp_store.write(i)
        temp_store.write("\n")          
    break
temp_store.close()
calibrate.close()


file_here = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day1/temporary_store.txt", "r")
total = 0
line = "niceass"
while line != "":
    line = file_here.readline()
    line = line.rstrip("\n")    
    try:
        first = line[0]
        last = line[-1]
    except:
        break
    together = first + last
    together = int(together)
    total += together
print(total)