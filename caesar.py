import helper 

def caesar_cipher(txt_list, shift, encrypt=True):
    caesar = []
    shift = shift if encrypt else -shift  
    for value in txt_list: caesar.append((value + shift) % 26)
    return caesar

def caesar_encrypt():
    pass

def caesar_decrypt():
    pass

""" userInput = "banana"
key = 5
cencrypted_text= convert_to_char((caesar_cipher(char_to_num(userInput), key)))
print(cencrypted_text)
cdecrypted_text= convert_to_char((caesar_cipher(char_to_num(cencrypted_text), key, False)))
print(cdecrypted_text)"""


def run():
    print("""Version 1.0.0\n\nOrigin:

    The CAESAR ALGORITHM\n""")
    
    while True:
        choice = helper.get_menu_choice()
        
        if choice == 1:
            caesar_encrypt()
        elif choice == 2:
            caesar_decrypt()
        elif choice == 3: 
            print("Returning to the Main Menu...")
            break   
