"""tee-hee docstring this is the main file."""
import analyzer as a

def main():
    """here is my module dosctring, title is descriptive."""
    current_file = "analyzer\phil.txt"
    stop = False
    while not stop:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print("lines, words or letters?: ")
        print("press \"q\" to Quit.")

        choice = input("--> ")
        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            stop = True

        elif choice == "lines":
            print(a.lines(current_file))

        elif choice == "words":
            print(a.words(current_file))
            
        elif choice == "letters":
            print(a.letters(current_file))

        elif choice == "all":
            print(a.all_att_once(current_file))

        elif choice in ["word_frequency","wf"]:
            print(a.word_frequency(current_file))
        
        elif choice in ["lf","letter_frequency"]: #placeholder
            print(a.letter_frequency(current_file))

        elif choice == "change":
            temp = input("Which file should we use? lorum.txt or phil.txt? ")
            if "phil.txt" == temp:
                one_passed = True
            if "lorum.txt" == temp:
                one_passed = True
            if not one_passed:
                print("File name dosent exist!")
            if one_passed:
                current_file = temp



        if not stop:
            input("\nPlease press enter: ")




    
if __name__ == "__main__":
    main()
    