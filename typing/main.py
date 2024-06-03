"""This is the main file, where the functions are called from a input."""
import os
import functions as f


image_press_ice = """

██████╗ ██████╗ ███████╗███████╗███████╗      ██╗ ██████╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝      ██║██╔════╝██╔════╝
██████╔╝██████╔╝█████╗  ███████╗███████╗█████╗██║██║     █████╗  
██╔═══╝ ██╔══██╗██╔══╝  ╚════██║╚════██║╚════╝██║██║     ██╔══╝  
██║     ██║  ██║███████╗███████║███████║      ██║╚██████╗███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝      ╚═╝ ╚═════╝╚══════╝
"""

def main():
    """This is the main function for the entire file."""
    stop = False
    while not stop:
        os.system("clear")
        print(image_press_ice)
        print("Welcome to Press-Ice, where we measure your typing accuracy!!! ")
        print("1. Train easy ")
        print("2. Train medium ")
        print("3. Train hard ")
        print("4. See high score ")
        print("5. Train one letter at the time ")
        print("q. Quit ")


        choice = input("--> ")
        if choice == "q":
            print("Goodbye for now! ")
            stop = True

        elif choice == "1":
            f.train_easy()

        elif choice == "2":
            f.train_medium()
            

        elif choice == "3":
            f.train_hard()

        elif choice == "4":
            f.see_high_score()

        elif choice == "5":
            f.practice()

        if not stop:
            input("\nPress enter to continue: ")

    
if __name__ == "__main__":
    main()
