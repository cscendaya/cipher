#main.py

import caesar, vigenere, xor, convoy

def get_main_menu_choice():
    
    while True:       
        try:
            choice = int(input("MENU\n\n1 - Caesar\n2 - Vigenere\n3 - XOR\n4 - Convoy\n5 - Exit\n\nEnter choice: "))
            
            if choice in (1,2,3,4,5):
                return choice
            else:
                print("\nInvalid choice, Please select from 1, 2, 3, 4, or 5.\n")
            
        except ValueError:
            print("\nInvalid input, Please enter a number.\n")

def main():
    while True:
        choice = get_main_menu_choice()
         
        if choice == 1:
            caesar.run()
        elif choice == 2:
            vigenere.run()
        elif choice == 3:
            xor.run()
        elif choice == 4:
            convoy.run()
        elif choice == 5:
            print("Exiting...")
            break 

if __name__ == "__main__":
    main()
            