def find_factors(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    
    return factors


print(find_factors(13))  
print(find_factors(19))  
print(find_factors(35)) 