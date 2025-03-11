import secrets
from tkinter import font
import pyfiglet 
import helper 

def xor_cipher(txt_list, key_list): 
    xkey =  helper.get_repeating_key(txt_list, key_list) if len(txt_list) != len(key_list) else key_list   
    xor = []
    for i in range(len(txt_list)):
        xor.append(txt_list[i] ^ xkey[i])
    return bytes(xor) #list of integers turned to bytes

def xor_encrypt(): #not final

    try: 
        xuser_input = input("\nXOR Plaintext: ") #insert helper function? na may try except shizzles
        xkey_input = input("XOR key: ")   #insert helper function?
        xencrypted_text = xor_cipher(list(xuser_input.encode()), xkey_input.encode()) #list of bytes
        print(f"""
=============================================================================
                           ENCRYPTION SUCCESSFUL 
=============================================================================
              
RESULTS:                            
              
Ciphertext(hex):     {xencrypted_text.hex()}

=============================================================================

IMPORTANT NOTICE:

- Sample 1
- Sample 2
- Sample 3

=============================================================================
""") #.hex() = normalize into a copy-able string
        
    except ValueError as error: print(error)

def xor_decrypt(): #kinda final
    while True: 
        try: 
            xuser_input = input("\nXOR Ciphertext(hex): ")
            if xuser_input == 'q': break            #if user wants to quit during input loop
            xhex_input = bytes.fromhex(xuser_input) #bytes.fromhex() = from hex to byte 
            break    

        except ValueError:
            print("Invalid hexadecimal input. Please enter valid hex values.") 

    xkey_input = input("XOR Key: ").encode()  #insert helper function?
    xdecrypted_text = xor_cipher(xhex_input, xkey_input) 
    print(f"""
=============================================================================
                            DECRYPTION SUCCESSFUL 
=============================================================================
              
RESULTS:              
              
Decrypted Text:     {xdecrypted_text.decode()}

=============================================================================

SECURITY NOTE:

- Ensure the decrypted message is handled securely.
- XOR Encryption provides security, but responsibility lies with the user.

=============================================================================

""")

def run():

    banner = pyfiglet.figlet_format("XOR Encryption", font="cybermedium")
    print(f"""\n=============================================================================

{banner}""")
    
    print("""Version 1.0.0\n\nOrigin:

    Sample Text of Origin...
          
Select an option below to proceed:\n""")

    while True:
        
        choice = helper.get_menu_choice()
        
        if choice == 1:
            xor_encrypt()  
            helper.get_menu_choice() 
        elif choice == 2:
            xor_decrypt() 
            helper.get_menu_choice()      
        elif choice == 3: 
            print("Returning to the Main Menu...")
            break