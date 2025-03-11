#main.py

import caesar, vigenere, xor, convoy
import pyfiglet

def get_main_menu_choice():

    banner = pyfiglet.figlet_format("IT129 Encryption Algorithms", font="standard")
    print(banner)

    print("""Version 1.0.0\n\nAbout:

    Developed by Endaya, Go, and Salandanan for their IT129 Project.
          
Select an option below to proceed:\n""")
    
    while True:       
        try:
            choice = input("MENU\n\n"
                           "1 - Caesar\n"
                           "2 - Vigenere\n"
                           "3 - XOR\n"
                           "4 - Convoy\n"
                           "5 - Exit\n"
                           "\nEnter choice ( 1 - 5 ): ")

            if not choice.isdigit():
                print("\nInvalid input. Please select 1, 2, 3, 4, or 5.\n")
                continue

            choice = int(choice)

            if choice in (1,2,3,4,5):
                return choice
            else:
                print("\nInvalid choice, Please select from 1, 2, 3, 4, or 5.\n")
            
        except ValueError:
            print("\nInvalid input, Please enter a number.\n")

def main():
  
    while True:
        choice = get_main_menu_choice()
         
        if choice == 1:   caesar.run()
        elif choice == 2: vigenere.run()
        elif choice == 3: xor.run_xor()
        elif choice == 4: convoy.run_convoy()
        elif choice == 5:
            print("Exiting...")
            break 

if __name__ == "__main__":
    main()