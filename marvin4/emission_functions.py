"""file with functions for emmisions and such"""
import emission_data as ed

def search_country(search_word): #13
    """Docstring, searches country"""
    another_storage = []
    for keys in ed.country_data:
        if search_word.lower() in keys.lower():
            another_storage.append(keys)
    if not another_storage:
        raise ValueError("Doesnt exist!")
    return another_storage

def get_country_year_data_megaton(country, year): #14.1
    """megaton"""
    year = str(year)
    data = ed.country_data.get(country)
    the_id = data.get("id")
    if "1990" in year:
        butterfly = ed.emission_1990.get(the_id)
        multiply = butterfly*1_000_000
        return multiply
    if "2005" in year:
        butterfly = ed.emission_2005.get(the_id)
        multiply = butterfly*1_000_000
        return multiply
    if "2017" in year:
        butterfly = ed.emission_2017.get(the_id)
        multiply = butterfly*1_000_000
        return multiply
    raise ValueError("Wrong year!") #fabricating errors because we need them..




def get_country_change_for_years(country, year1, year2): #14.2
    """change between years"""
    try:
        first = get_country_year_data_megaton(country, year1)
        second = get_country_year_data_megaton(country, year2)
        calculate = round((((second) / first)*100) - 100,2)
        return calculate
    except TypeError:
        return ValueError









def get_country_data(country_name): #15.1
    """Recieve string as argument here"""
    stored = ed.country_data.get(country_name)
    population = stored.get("population")
    x_snakecase = 0
    for i in "0123456789":
        if i in str(population):
            x_snakecase = 1
            population_1990 = population[0]
            population_2005 = population[1]
            population_2017 = population[2]
            break
    if x_snakecase == 0:
        stored.update({"population":None})
        population_1990,population_2005,population_2017 = None,None,None
    country = country_name
    emission_1990 = get_country_year_data_megaton(country, "1990")
    emission_2005 = get_country_year_data_megaton(country, "2005")
    emission_2017 = get_country_year_data_megaton(country, "2017")
    from1990to2005 = get_country_change_for_years(country, 1990, 2005)
    from2005to2017 = get_country_change_for_years(country, 2005, 2017)
    weird = {"name":country,1990:{"emission":emission_1990,"population":population_1990},\
2005:{"emission":emission_2005,"population":population_2005},\
2017:{"emission":emission_2017,"population":population_2017},\
"emission_change":(from1990to2005,from2005to2017)} 
    return weird


def print_country_data(data): #15.2
    """Documsdbgais print it differently because"""
    country = data.get("name")
    emission_1990 = data[1990]["emission"]
    emission_2005 = data[2005]["emission"]
    emission_2017 = data[2017]["emission"]
    from1990to2005 = data["emission_change"][0]
    from2005to2017 = data["emission_change"][1]
    population_1990 = data[1990]["population"]
    population_2005 = data[2005]["population"]
    population_2017 = data[2017]["population"]

    print_here = f"{country},\n1990: "+ f"{emission_1990}" + "\n"\
+ "2005: " +f"{emission_2005}" + "\n"\
"2017: " +f"{emission_2017}" + "\n"\
f"1990-2005: {from1990to2005}%     2005-2017: {from2005to2017}%)"
    if population_1990 is not None:
        print_here +="\n"\
f"Population: 1990: {population_1990}\
    2005: {population_2005}     2017: {population_2017}"
    else:
        print_here +="\n" "Missing population data!"
    print(print_here)
    
    return print_here
