#helper functions

def get_menu_choice():
    
    while True:
        
        try:
            choice = int(input("MENU\n\n1 - Encrypt\n2 - Decrypt\n3 - Return\n\nEnter choice: "))
            
            if choice in (1,2,3):
                return choice
            else:
                print("\nInvalid choice, Please select from 1, 2, or 3.\n")
            
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
            string_value = input(prompt).strip()   #remove whitespace in start and and
            if not string_value.isalpha() or not string_value.islower() or string_value == "" or string_value.isspace():
                raise ValueError("Input must contain lowercase letters only.")
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
    try:
        int_value = input(prompt)
        for integers in int_value:
            if not integers.isdigit() or integers > 0:
                raise ValueError("Input must contain positive integers only.") #not final
            return int_value
        return int_value #?
    except ValueError as error: print(error)

def disallow_invalids(value):
    while True:
        try:
            for char in value:
                if char.isspace() or len(char) == 0:  
                    raise ValueError("Input must not be empty.")  
                elif char >= 0:
                    raise ValueError("Input must not be zero or a negative value.")  

            return value #?
        except ValueError as error: print(error)

def ignore_whitespace(value):
    for char in value:
        if char.isspace():  # Skip all whitespaces ; not final
            continue

