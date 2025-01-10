import random
import string

def encrypt_with_random_letters(message):
   
    interval = random.randint(2, 20)
    
    
    encrypted_message = []
    
    
    for i in range(len(message)):
        
        encrypted_message.append(message[i])
        
        
        if (i + 1) % interval == 0 and (i + 1) != len(message):  
            random_letter = random.choice(string.ascii_lowercase)  
            encrypted_message.append(random_letter)  

    encrypted_message_str = ''.join(encrypted_message)
    
    return encrypted_message_str, interval


message = "send cheese"
encrypted_message, interval = encrypt_with_random_letters(message)
print(f"Original message: '{message}'")
print(f"Random interval: {interval}")
print(f"Encrypted message: '{encrypted_message}'")