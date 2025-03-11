import helper 
import pyfiglet

def vigenere_cipher(txt_list, key_list, encrypt=True):
    vkey =  helper.get_repeating_key(txt_list, key_list) if len(txt_list) != len(key_list) else key_list
    vigenere = []
    if encrypt:
        for i in range(len(txt_list)): vigenere.append((txt_list[i] + vkey[i]) % 26)
    else: 
        for i in range(len(txt_list)): vigenere.append((txt_list[i] - vkey[i]) % 26)
    return vigenere

def vigenere_encrypt():
    user_text = helper.str_validation("\nEnter text to encrypt: ")
    key = helper.str_validation("Enter encryption key (lowercase only): ")
    encrypted_text = helper.convert_to_char_lower(
        vigenere_cipher(helper.char_to_num_lower(user_text), helper.char_to_num_lower(key), True)
    )
    print(f"""
=============================================================================
                           ENCRYPTION SUCCESSFUL 
=============================================================================
              
RESULTS:                            
              
Encrypted Text:     {encrypted_text}

=============================================================================

IMPORTANT NOTICE:

- The Vigenère cipher is stronger than Caesar but still vulnerable to cryptanalysis.
- Ensure the key is kept secret and is sufficiently complex.
- A longer key improves security significantly.

=============================================================================\n""")

def vigenere_decrypt():
    user_text = helper.str_validation("\nEnter text to decrypt: ")
    key = helper.str_validation("Enter decryption key (lowercase only): ")
    decrypted_text = helper.convert_to_char_lower(
        vigenere_cipher(helper.char_to_num_lower(user_text), helper.char_to_num_lower(key), False)
    )
    print(f"""
=============================================================================
                            DECRYPTION SUCCESSFUL 
=============================================================================
              
RESULTS:              
              
Decrypted Text:     {decrypted_text}

=============================================================================

SECURITY NOTE:

- The key must match exactly for proper decryption.
- The Vigenère cipher is resistant to frequency analysis but can be broken with known-plaintext attacks.
- For better security, consider using modern encryption algorithms.

=============================================================================\n""")
    
def print_info():
    print("""\n=============================================================================
          \nVersion 1.0.0\n\nOrigin:

    Sample Origin for VIGENERE Encryption
          
Use Case:         
          
    Sample Text

Pros:
          
    - More secure than the Caesar cipher due to its polyalphabetic nature.
    - Harder to crack using frequency analysis compared to simple substitution ciphers.
          
Cons:

    - Vulnerable to repeated key attacks if the key is short.
    - Requires key management for encryption and decryption.
            
=============================================================================\n""")

def run():
    banner = pyfiglet.figlet_format("VIGENERE Encryption", font="cybermedium")
    print(f"""\n=============================================================================

{banner}\nSelect an option below to proceed:\n""")
    
    while True:
        choice = helper.get_menu_choice()
        
        if choice == 1:
            vigenere_encrypt()
        elif choice == 2:
            vigenere_decrypt()
        elif choice == 3:
            print_info()
        elif choice == 4:
            print("""\nReturning to the Main Menu...\n
=============================================================================\n""")
            break