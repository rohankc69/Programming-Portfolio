def is_prime(n):
    if n <= 1:
        return False  
    if n <= 3:
        return True  
    
   
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  
    
    return True


print(is_prime(70))   
print(is_prime(30))   
print(is_prime(40))   
print(is_prime(80))   
print(is_prime(26))   
print(is_prime(4))  
print(is_prime(76))  
print(is_prime(100))  