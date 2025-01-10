def add_person(**kwargs):
    name = kwargs.get('name')
    address = kwargs.get('address')
    age = kwargs.get('age')
    
    # You can now use name, address, and age as needed
    print(f"Name: {name}, Address: {address}, Age: {age}")

# Example usage
add_person(name="Rohan", address="Kathmandu ", age=18)