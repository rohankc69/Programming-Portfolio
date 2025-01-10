import random
import string

def encrypt_with_random_letters(message):
    
    interval = random.randint(6, 30)
    print(f"Random interval for encryption: {interval}") 
    
   
    encrypted_message = []
    
    
    for i in range(len(message)):
       
        encrypted_message.append(message[i])
        
       
        if (i + 1) % interval == 0 and (i + 1) != len(message):  
            random_letter = random.choice(string.ascii_lowercase)  
            encrypted_message.append(random_letter)  #
            print(f"Inserted random letter '{random_letter}' after index {i}")  
    
    encrypted_message_str = ''.join(encrypted_message)
    
    return encrypted_message_str, interval

def decrypt_message(encoded_message, interval):
    
    original_message = []
    
    
    for i in range(len(encoded_message)):
       
        if (i + 1) % (interval + 1) != 0:  
            original_message.append(encoded_message[i])
    
  
    decrypted_message = ''.join(original_message)
    
    return decrypted_message


message = "send cheese"
encrypted_message, interval = encrypt_with_random_letters(message)
print(f"Original message: '{message}'")
print(f"Encrypted message: '{encrypted_message}'")


decrypted_message = decrypt_message(encrypted_message, interval)
print(f"Decrypted message: '{decrypted_message}'")