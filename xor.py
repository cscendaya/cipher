import helper 

def xor_cipher(txt_list, key_list): 
    xkey =  helper.get_repeating_key(txt_list, key_list) if len(txt_list) != len(key_list) else key_list   
    xor = []
    for i in range(len(txt_list)):
        xor.append(txt_list[i] ^ xkey[i])
    return bytes(xor) #list of integers turned to bytes

def xor_encrypt(): #not final

    try: 
        xuser_input = input("XOR plaintext: ") #insert helper function? na may try except shizzles
        xkey_input = input("XOR key: ")   #insert helper function?
        xencrypted_text = xor_cipher(list(xuser_input.encode()), xkey_input.encode()) #list of bytes
        print("Ciphertext(hex):", xencrypted_text.hex())                              #.hex() = normalize into a copy-able string
    except ValueError as error: print(error)

def xor_decrypt(): #kinda final
    while True: 
        try: 
            xuser_input = input("XOR Ciphertext(hex): ")
            if xuser_input == 'q': break            #if user wants to quit during input loop
            xhex_input = bytes.fromhex(xuser_input) #bytes.fromhex() = from hex to byte 
            break                     
        except ValueError:
            print("Invalid hexadecimal input. Please enter valid hex values.") 

    xkey_input = input("XOR Key: ").encode()  #insert helper function?
    xdecrypted_text = xor_cipher(xhex_input, xkey_input) 
    print("Decrypted text:", xdecrypted_text.decode())  

def run():

    while True:
        print("""Version 1.0.0\n\nOrigin:

        The XOR ALGORITHM\n""")
        
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
                                

