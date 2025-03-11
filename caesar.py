import helper 
import pyfiglet

def caesar_cipher(txt_list, shift, encrypt=True):
    caesar = []
    shift = shift if encrypt else -shift  
    for value in txt_list: caesar.append((value + shift) % 26)
    return caesar

def caesar_encrypt():
    user_text = helper.str_validation("\nEnter text to encrypt: ")
    shift = helper.int_validation("Enter shift value: ")
    encrypted_text = helper.convert_to_char_lower(
        caesar_cipher(helper.char_to_num_lower(user_text), shift, True)
    )
    print(f"""
=============================================================================
                           ENCRYPTION SUCCESSFUL 
=============================================================================
              
RESULTS:                            
              
Encrypted Text:     {encrypted_text}

=============================================================================

IMPORTANT NOTICE:

- Ensure you remember the shift value for decryption.
- CAESAR Encryption is simple but can be cracked with frequency analysis.
- Consider using stronger encryption for sensitive data.

=============================================================================\n""")
    
def caesar_decrypt():
    user_text = helper.str_validation("\nEnter text to decrypt: ")
    shift = helper.int_validation("Enter shift value: ")
    decrypted_text = helper.convert_to_char_lower(
        caesar_cipher(helper.char_to_num_lower(user_text), shift, False)
    )
    print(f"""
=============================================================================
                            DECRYPTION SUCCESSFUL 
=============================================================================
              
RESULTS:              
              
Decrypted Text:     {decrypted_text}

=============================================================================

SECURITY NOTE:

- Ensure the decrypted message is handled securely.
- CAESAR Encryption provides basic security but is susceptible to brute force.
- Avoid using simple shift values like 1 or 2 for added security.

=============================================================================\n""")

def print_info():
    print("""\n=============================================================================
          \nVersion 1.0.0\n\nOrigin:

    The Caesar Cipher is one of the earliest known encryption techniques, 
    attributed to Julius Caesar, who used it in ancient Rome to protect 
    military messages. It operates by shifting each letter in the alphabet 
    by a fixed number of positions. While effective in ancient times, its 
    small keyspace of 25 possible shifts makes it highly vulnerable to modern 
    cryptanalysis.
          
Use Case:         
          
    A simple text-based game encrypts secret passcodes using a Caesar Cipher 
    with a predefined shift value. Players must decrypt the passcode to access 
    hidden levels.

Pros:
          
    - Simple and easy to implement.
    - Fast encryption and decryption process.
          
Cons:

    - Extremely weak security, easily broken with brute force or frequency analysis.
    - Only has 25 possible keys, making it impractical for real-world encryption.
            
=============================================================================\n""")
    
def run():
    banner = pyfiglet.figlet_format("CAESAR Encryption", font="cybermedium")
    print(f"""\n=============================================================================

{banner}\nSelect an option below to proceed:\n""")
    
    while True:
        choice = helper.get_menu_choice()
        
        if choice == 1:
            caesar_encrypt()
        elif choice == 2:
            caesar_decrypt()
        elif choice == 3:
            print_info()
        elif choice == 4:
            print("""\nReturning to the Main Menu...\n
=============================================================================\n""")
            break   
