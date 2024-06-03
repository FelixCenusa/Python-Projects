"""Module Docstring. Happy???"""

def pick(the_backpack,pick_up,the_index = -100):
    """picks a item"""
    lets_see = 1
    if the_index == -100:
        the_index = len(the_backpack)
        lets_see = 0
    
    
    if int(the_index) > int(len(the_backpack)):
        printthis = str(the_backpack) + " " + str(the_index) + " Error"
        print(printthis)
        return the_backpack
    if lets_see == 0:
        the_index = int(the_index)
        the_backpack.insert(the_index,pick_up)
        printthis = the_backpack , " inserted at place ", str(the_index)
        printthis = the_backpack
        print(printthis)
        return printthis
    the_index = int(the_index)
    the_backpack.insert(the_index,pick_up)
    message = str(pick_up) + " has been added to index " + str(the_index)
    print(message)
    return the_backpack

def inventory(the_backpack):
    """Prints out the backpack items"""
    message = "The backpack has " + str(len(the_backpack)) + " items and they are: " + str(the_backpack)
    print(message)
    
def drop(the_backpack,throw_away):
    """Throw away something from the backpack, return updated backpack."""
    try:
        the_backpack.remove(throw_away)
        message = str(throw_away) + " has been removed"
        print(message)
        return the_backpack
    except Exception:
        if throw_away not in the_backpack:
            print("Error " + throw_away + " does not exist!")
            return the_backpack
    return the_backpack
        

def swap(the_backpack,first_swap,second_swap):
    """Swap a items"""
    try:
        where1 = the_backpack.index(first_swap)
        where2 = the_backpack.index(second_swap)
        the_backpack.remove(first_swap)
        the_backpack.remove(second_swap)
        if int(where1) <= int(where2):
            the_backpack.insert(where1,second_swap)
            the_backpack.insert(where2,first_swap)
        else:
            the_backpack.insert(where2,first_swap)
            the_backpack.insert(where1,second_swap)
        print(the_backpack)
        return the_backpack
    except Exception:
        if first_swap not in the_backpack:
            message = first_swap + " does not exist! - Error"
            print(message)
            if second_swap not in the_backpack:
                message += " and neither does " + second_swap
                print(message)
            return the_backpack
    return the_backpack
