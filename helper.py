#helper functions

def get_menu_choice():
    
    while True:
        
        try:
            choice = int(input("MENU\n\n1 - Encrypt\n2 - Decrypt\n3 - About\n4 - Return\n\nEnter choice: "))
            
            if choice in (1,2,3,4):
                return choice
            else:
                print("\nInvalid choice, Please select from 1, 2, 3, or 4.\n")
            
        except ValueError:
            print("\nInvalid input, Please enter a number.\n")

#---------CONVERSION------------

def char_to_num_lower(letter_list):
    return [ord(letter) - ord('a') for letter in letter_list] 

def convert_to_char_lower(value_list):
    return ''.join(chr(value + ord('a')) for value in value_list)

#-----------OTHERS-------------

def get_repeating_key(text_list, key): #works if kulang or sobra ung key
    repeat_key = []
    for i in range(len(text_list)):
        repeat_key.append(key[i % len(key)])  
    return repeat_key

#-------INPUT VALIDATIONS------- #lagyan pa ba limit ung user inputs? if so, how many? 

def str_validation(prompt):
    while True: 
        try:
            string_value = input(prompt)
            if not string_value.isalpha() or not string_value.islower() or string_value == "" or string_value.isspace():
                raise ValueError("Input must contain lowercase letters only.")
            return string_value
        except ValueError as error:
            print(error)  

def xor_str_validation(prompt):
    while True: 
        try:
            string_value = input(prompt)
            if string_value == "" or string_value.isspace():
                raise ValueError("Invalid input.")
            return string_value
        except ValueError as error:
            print(error)  

def int_validation(prompt): 
    while True:
        try:
            int_value = input(prompt)  # Get input as string
            if not int_value.isdigit():
                raise ValueError("Input must be a positive integer.")
            return int(int_value)  # Convert to integer after validation
        except ValueError as error:
            print(error)