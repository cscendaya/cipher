#main.py

import caesar, vigenere, xor, convoy
import pyfiglet

def print_info():
    print("""\n=============================================================================
          \nVersion 1.0.0\n\nAbout:

    This software is a console-based cryptographic program designed for secure and efficient encryption and decryption.
    It features multiple encryption methods, including Caesar, Vigenère, XOR, and CONVOY, a custom-developed algorithm.
    With a command-line interface, decent error handling, and detailed insights into each cryptographic process,
    our program ensures reliability, security, and ease of use, Our software offers a practical approach to understanding 
    and applying encryption techniques.

Developed By:

(IT129 - CIS342)

- Endaya, Carlie Shaye C.
- Go, Charles Kristoffer A.
- Salandanan, Christian Kerby T.

=============================================================================\n""")

def get_main_menu_choice():
    
    while True:       
        try:
            choice = input("MAIN MENU\n\n"
                           "1 - Caesar\n"
                           "2 - Vigenere\n"
                           "3 - XOR\n"
                           "4 - Convoy\n"
                           "5 - About\n"
                           "6 - Exit\n"
                           "\nEnter choice ( 1 - 6 ): ").replace(" ", "")

            if not choice.isdigit():
                print("\nInvalid input. Please select 1, 2, 3, 4, 5, or 6.\n")
                continue

            choice = int(choice)

            if choice in (1,2,3,4,5,6):
                return choice
            else:
                print("\nInvalid choice, Please select from 1, 2, 3, 4, 5, or 6.\n")
            
        except ValueError:
            print("\nInvalid input, Please enter a number.\n")

def main():

    banner = pyfiglet.figlet_format("IT129 Cryptographic Algorithms", font="standard")
    print(f"""{banner}\nSelect an Algorithm below to proceed:\n""")
    
    while True:
        choice = get_main_menu_choice()
         
        if choice == 1:
            caesar.run()
        elif choice == 2:
            vigenere.run()
        elif choice == 3:
            xor.run_xor()
        elif choice == 4:
            convoy.run_convoy()
        elif choice == 5:
            print_info()
        elif choice == 6:
            print("Exiting...")
            break 

if __name__ == "__main__":
    main()
