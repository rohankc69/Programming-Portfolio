def encrypt_message(message):
   
    no_spaces = message.replace(" ", "")
    
    encrypted = no_spaces[::-1]
    return encrypted


print(encrypt_message("Hello World"))         
print(encrypt_message("This is a test"))       
print(encrypt_message("Encryption is fun"))     
print(encrypt_message("  Spaces   should  be removed  "))  