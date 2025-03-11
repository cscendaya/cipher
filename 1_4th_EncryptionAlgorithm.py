import secrets
from tkinter import font
import pyfiglet 

#------CONSTANT VALUES---------------------------------------

ENCRYPTION_MULTIPLIER = 15 
DECRYPTION_INVERSE = 7

TRANSPORT_MULTIPLIER = 5
TRANSPORT_OFFSET = 7
TRANSPORT_INVERSE = 21
    
#------ENCRYPTION--------------------------------------------

""" A function that returns an ENCRYPTED integer value by applying Affine formula """

""" Formula: (Ciphertext) C = (aP + b) mod 26 (a = co-prime, p = plaintext, b = constant/additive key) """

def encrypt (a, p, b):
    return (a * p + b) % 26
    
#------DECRYPTION--------------------------------------------

""" A function that returns an DECRYPTED integer value by applying Affine formula """

""" Formula: (Plaintext) P = i x (C - B) mod 26 (i = modular inverse, C = ciphertext, B = constant/additive key) """
    
def decrypt (i, c, b):
    return(i * (c - b)) % 26

""" A function that continuously adds 100 to the key when it is a negative value. """
    
def fix_key (key):
    while key < 0:
        key += 26 #take note this might cause issue, change to 100 if ever.
    return key
    
#------OTHER FUNCTIONS---------------------------------------

""" A function that takes the list of input characters and converts them into corresponding numerical values (0-25). Uses ord() to return ASCII value of each letter"""

""" Subtracting each letter's ASCII to 'a' which has an ASCII value of 97, this process serves as 0 based index for acquiring values 0 - 25 """

def char_to_num(char_list):
    return [ord(letter) - ord('a') for letter in char_list] 

""" A function that takes the list of numerical values and perform the indicated operations. Returning the index integer value for locating master key. """
 
def generate_key_index(numeric_values, initial_key):    
    return (( sum(numeric_values) + initial_key ) % 26 ) 

""" A function that uses the key_index as index to iterate, pick, and return an offset/additive key value in the list that has randomized order of values. (0 - 2048) """

""" Utilizes secrets.SystemRandom().shuffle to securely randomize values that are not based on any patterns. """

def locate_offset_value(key_index):
    offset_values = list(range(0,2049))
    randomizer = secrets.SystemRandom() 
    randomizer.shuffle(offset_values)
    shift_value = key_index % len(offset_values)
    return offset_values[shift_value]
    
""" A function that gets each numeric value in the list and add it with the ASCII value of 'a' which is 97, this reverses the char_to_num function. """

""" After converting numeric values to char, it merges all characters into a single string by utilizing ''.join() """

def convert_to_char(list):
    return ''.join(chr(value + ord('a')) for value in list)
    
#------ENCRYPTION MAIN ALGORITHM-----------------------------

""" A function that handles the main flow of encryption process.  """

def encrypt_opt():
    
    try:
        
        user_input = input("\nEnter plaintext to encrypt: ").lower()
    
        if not user_input.isalpha():
            raise ValueError("\nInput must contain letters only.\n")
    
        initial_key_input = input("Enter your preferred initial key: ")
        if not initial_key_input.isdigit():
            raise ValueError("\nInitial key must be a positive integer.\n")

        initial_key = int(initial_key_input)
        
        if initial_key <= 0: 
            raise ValueError("\nInitial key must be a positive integer.\n")
        
        """ Utilizes the char_to_num function that returns a list populated with converted numeric values of the user input. """
        
        numeric_values = char_to_num(list(user_input)) 
        
        """ Utilizes the locate_offset_value function that returns the picked offset value based on the index of key_index. """
        
        """ The generate_key_index function in the parameter immediately returns the key_index after generating. Eliminating the need to be assigned into a variable. """
        
        """ The returned offset_value of the function will then be assigned as the master key that will be used in encrypting the plaintext characters.  """
        
        master_key = locate_offset_value(generate_key_index(numeric_values, initial_key))
        
        """ Utilizing the encrypt function, it takes three parameter for the Affine formula. Returns a list of encrypted numeric values. """
        encrypted_values = [encrypt(ENCRYPTION_MULTIPLIER, num, master_key) for num in numeric_values] 
        
        """ This section covers the convertion of encrypted numeric values to its corresponding char value. """
        encrypted_text = convert_to_char(encrypted_values)
        
        """ This part encrypts the master key, converting it to transport key. """
        transport_key = encrypt(TRANSPORT_MULTIPLIER, master_key ,TRANSPORT_OFFSET)
    
        print(f"\nEncrypted Text: {encrypted_text}\nTransport Key: {transport_key}\n\nWarning: Exposing the transport key weakens encryption security, allowing attackers to decrypt the ciphertext. \nKeep it strictly confidential.\n")
        
    except ValueError as e: print(e)

#------DECRYPTION MAIN ALGORITHM------------------------------

""" A function that handles the main flow of decryption process.  """    

def decrypt_opt():
    
    try:
    
        user_input = input("\nEnter ciphertext to decrypt: ").lower()
        
        if not user_input.isalpha():
            raise ValueError("\nCiphertext must contain letters only.\n")
        
        transport_key_input = input("Enter transport key: ")
        if not transport_key_input.isdigit():
            raise ValueError("\nTransport key must be a positive integer.\n")

        transport_key = int(transport_key_input)
        
        if transport_key < 0: 
            raise ValueError("\nNegative values are not allowed.\n")
        
        """ Utilizing the fix_key function with the function decrypt as argument to its paramater, this line decrypts and validate the transport key. """
        
        master_key = fix_key(decrypt(TRANSPORT_INVERSE, transport_key, TRANSPORT_OFFSET))
        
        """ Convertion of each char in user input into its corresponding numeric value. """
        numeric_values = char_to_num(list(user_input))
        
        """ Decryption process, uses the master key as an argument in completing the decryption process. """
        decrypted_values = [decrypt(DECRYPTION_INVERSE, num, master_key) for num in numeric_values]
        
        """ Convertion of decrypted numeric values to its corresponding char values. Decyphering the plaintext. """
        decrypted_text = convert_to_char(decrypted_values)
        print(f"\nDecrypted Text: {decrypted_text}\n")
        
    except ValueError as e: print(e)
    
#------MAIN MENU----------------------------------------------
    
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
            
def main():
    
    banner = pyfiglet.figlet_format("CONVOY Encryption", font="cybermedium")
    print(banner)
    
    print("""Version 1.0.0\n\nOrigin:

    The CONVOY Algorithm was developed by Endaya, Go, and Salandanan, with a focus on securing encryption keys. 
    Inspired by armored trucks transporting valuable assets, the algorithm prioritizes key security
    by encrypting it separately. Built on Affine encryption, CONVOY ensures strong yet lightweight encryption,
    balancing security and efficiency.\n""")
    
    while True:
         choice = get_menu_choice()
         
         if choice == 1:
             encrypt_opt()
         elif choice == 2:
             decrypt_opt()
         elif choice == 3:
             print("Returning to the Main Menu...")
             break 

if _name_ == "_main_":
    main()