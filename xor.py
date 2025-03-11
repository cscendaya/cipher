import helper 

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
        print("Ciphertext(hex):", xencrypted_text.hex())                              #.hex() = normalize into a copy-able string
    except ValueError as error: print(error)
    return


def xor_decrypt(): 
    
    try: 
        xduser_input = helper.xor_str_validation("XOR Ciphertext: ")                                         
        xhex_input = bytes.fromhex(xduser_input)                                       #bytes.fromhex() = from hex to byte                     
    except ValueError:
        print("Invalid hexadecimal input. Please enter valid hex values.")

    try:
        xkey_input = helper.xor_str_validation("XOR Key: ").encode()  
        xdecrypted_text = xor_cipher(xhex_input, xkey_input) 
        print("Decrypted text:", xdecrypted_text.decode()) 
    except ValueError as error: print(error) 
    return

def run_xor():

    while True:
        print("""Version 1.0.0\n\nOrigin:

        The XOR ALGORITHM\n""")
        choice = helper.get_menu_choice()
        
        if choice == 1:
            xor_encrypt()  
        elif choice == 2:
            xor_decrypt() 
        elif choice == 3: 
            print("Returning to the Main Menu...")
            break  
                                    

