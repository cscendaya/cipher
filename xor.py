import helper 
import pyfiglet

def xor_cipher(txt_list, key_list): 
    xkey =  helper.get_repeating_key(txt_list, key_list) if len(txt_list) != len(key_list) else key_list   
    xor = []
    for i in range(len(txt_list)):
        xor.append(txt_list[i] ^ xkey[i])
    return bytes(xor)                                                                 #list of integers turned to bytes

def xor_encrypt(): 
    try: 
        xuser_input = helper.xor_str_validation("XOR Plaintext: ")#.strip() #if valid, strip for end and start whitespace -- ilagay nlng to sa vigenere and caesar, whitespace is ok here masisira kasi message
    except ValueError as error: print(error)

    try: 
        xkey_input = helper.xor_str_validation("XOR key: ")   
        xencrypted_text = xor_cipher(list(xuser_input.encode()), xkey_input.encode()) #return list of bytes (insert list() for consistency with xkeyinput repeating key??)
        print(f"""
                =============================================================================
                                        ENCRYPTION SUCCESSFUL 
                =============================================================================
                            
                RESULTS:                            
                            
                Ciphertext(hex):     {xencrypted_text.hex()}                                    

                =============================================================================

                IMPORTANT NOTICE:

                Encrypted XOR output is raw binary data (random bytes).
                Copy-paste the encrypted plaintext (as hex values) for accurate decryption later.
                Ensure the key is handled securely.

                =============================================================================
                """)  #.hex() = normalize into a copy-able string
    except ValueError or IndexError as error: print(error)

def xor_decrypt(): 
    
    while True:
        try: 
            xduser_input = helper.xor_str_validation("XOR Ciphertext: ")                                         
            xhex_input = bytes.fromhex(xduser_input)                       #bytes.fromhex() = return from hex to original byte perfectly 
            break                                                          #exit loop if successful                   
        except ValueError as error:
            print("Invalid hexadecimal input. Please enter valid hex values.", error)

    while True:
        try:
            xkey_input = helper.xor_str_validation("XOR Key: ").encode()  
            xdecrypted_text = xor_cipher(xhex_input, xkey_input) 
            print(f"""
                    =============================================================================
                                                DECRYPTION SUCCESSFUL 
                    =============================================================================
                                
                    RESULTS:              
                                
                    Decrypted Text:     {xdecrypted_text.decode(errors="replace")}

                    =============================================================================

                    SECURITY NOTE:

                    Ensure the decrypted message is handled securely.
                    XOR Encryption provides security, but responsibility lies with the user.
                    Non UTF-8 characters will be printed as "?"

                    =============================================================================

                    """) #.decode(errors="replace") = non-utf 8 characters may be printed, hence replacing it with ? , assuming that the ciphertext is not from a text string only
        except ValueError as error: print(error) 

def run_xor():

    banner = pyfiglet.figlet_format("XOR Encryption", font="cybermedium")
    print(f"""\n=============================================================================

            {banner}""")
    
    print("""Version 1.0.0\n\nOrigin:

                Sample Text of Origin...
                Limitations: Limited to utf-8 characters, if not, it will be replaced as ? 
                    
                Select an option below to proceed:\n""")
    

    while True:         
        choice = helper.get_menu_choice()
        if choice == 1:
            xor_encrypt()  
        elif choice == 2:
            xor_decrypt() 
        elif choice == 3: 
            print("Returning to the Main Menu...")
            break  
                                    

if __name__ == "__main__":
    run_xor()