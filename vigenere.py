import helper 

def vigenere_cipher(txt_list, key_list, encrypt=True):
    vkey =  helper.get_repeating_key(txt_list, key_list) if len(txt_list) != len(key_list) else key_list
    vigenere = []
    if encrypt:
        for i in range(len(txt_list)): vigenere.append((txt_list[i] + vkey[i]) % 26)
    else: 
        for i in range(len(txt_list)): vigenere.append((txt_list[i] - vkey[i]) % 26)
    return vigenere

def vigenere_encrypt():
    pass

def vigenere_decrypt():
    pass

"""
getvkey="abc"
vencrypted_text= convert_to_char(vigenere_cipher(char_to_num(userInput), (char_to_num(getvkey)), True))
print(vencrypted_text)
vdecrypted_text= convert_to_char(vigenere_cipher(char_to_num(vencrypted_text), (char_to_num(getvkey)), False))
print(vdecrypted_text) """

def run():
    print("""Version 1.0.0\n\nOrigin:

    The VIGENERE ALGORITHM\n""")
    
    while True:
        choice = helper.get_menu_choice()
        
        if choice == 1:
            vigenere_encrypt()
        elif choice == 2:
            vigenere_decrypt()
        elif choice == 3: 
            print("Returning to the Main Menu...")
            break   

