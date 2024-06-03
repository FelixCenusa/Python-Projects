#Names of the maps are confusing as they are not accurate with the data.
#So I will be naming them the same as the data comes in.
puzzle_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/puzzle_file.txt", "r")

seeds_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/seeds_file.txt","w")
seeds_file.write(puzzle_file.readline()[7:])
seeds_file.close()
#soil_to_seed_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/soil_to_seed_file.txt","w")
#fertilizer_to_soil_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/fertilizer_to_soil_file.txt","w")
#water_to_fertilizer_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/water_to_fertilizer_file.txt","w")
#light_to_water_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/light_to_water_file.txt","w")
#temperature_to_light_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/temperature_to_light_file.txt","w")
#humidity_to_temperature_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/humidity_to_temperature_file.txt","w")
#location_to_humidity_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/location_to_humidity_file.txt","w")

temp = puzzle_file.readline()

def a_lot(file_name,compare_to):#Makes the files with relevant data.
    file_here = open(file_name,"w")
    temp = puzzle_file.readline()
    if compare_to in temp:
        while temp != "\n":
            temp = puzzle_file.readline()
            file_here.write(temp)
    file_here.close()

def special_a_lot(file_name,compare_to):#Makes the files with relevant data.
    file_here = open(file_name,"w")
    temp = puzzle_file.readline()
    if compare_to in temp:
        while temp != "":
            temp = puzzle_file.readline()
            file_here.write(temp)
    file_here.close()


a_lot("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/soil_to_seed_file.txt","seed-to-soil map:")
a_lot("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/fertilizer_to_soil_file.txt","soil-to-fertilizer map:")
a_lot("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/water_to_fertilizer_file.txt","fertilizer-to-water map:")
a_lot("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/light_to_water_file.txt","water-to-light map:")
a_lot("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/temperature_to_light_file.txt","light-to-temperature map:")
a_lot("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/humidity_to_temperature_file.txt","temperature-to-humidity map:")
special_a_lot("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/location_to_humidity_file.txt","humidity-to-location")


print("Stored all the values in respective documents.")


seeds_file = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/seeds_file.txt","r")
clean_seeds = seeds_file.readline().rstrip("\n").split(" ")
def redo_for_files(file_name):
    begin = False
    for index, seed in enumerate(clean_seeds):#first iteration
        if index % 2 == 0:
            seed_start = seed
            begin = False
        if index % 2 == 1:
            current_seed_range = f"{seed_start}:{int(seed_start)+int(seed)-1}" #Inclusive from and to.
            print(current_seed_range)
            begin = True

        if begin == True:
            print("Currently working on seed range: ", current_seed_range)
            said_file = open(file_name,"r")
            line = "temp"
            while line != "":
                line = said_file.readline()
                if line == "\n":
                    break
                clean_line = line.rstrip("\n").split(" ")
                clean_line_range = [f"{clean_line[1]}:{int(clean_line[1])+int(clean_line[2])-1}"]#from and to inclusive.
                print("Working on line range: ",clean_line_range)
                transform_add = int(clean_line[0]) - int(clean_line[1])
                print("If Transform, do it by: ",transform_add)
                seed_range_start = current_seed_range[0:(int(current_seed_range.find(":")))]
                print(seed_range_start)
                seed_range_end = current_seed_range[(int(current_seed_range.find(":"))+1):]
                print(seed_range_end)
                

                if int(seed_send) - int(clean_line[1]) >= 0:
                    if int(clean_line[1])+int(clean_line[2])-1-int(seed_send) >= 0:
                        new_seed = int(seed_send) - int(clean_line[1]) + int(clean_line[0])
                        clean_seeds[index] = str(new_seed)
                        break
            said_file.close()
    print(clean_seeds)

redo_for_files("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/soil_to_seed_file.txt")
redo_for_files("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/fertilizer_to_soil_file.txt")
redo_for_files("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/water_to_fertilizer_file.txt")
redo_for_files("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/light_to_water_file.txt")
redo_for_files("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/temperature_to_light_file.txt")
redo_for_files("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/humidity_to_temperature_file.txt")
redo_for_files("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day5/location_to_humidity_file.txt")







x = 99999999999999999999999999999999999999999999
for i in clean_seeds:
    if int(i) < x:
        x = int(i)
print(x)
print("Result")
print(clean_seeds)
