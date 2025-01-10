import sys  

def grep(pattern, file_name):
    """
    Function to search for a pattern in a file and print matching lines.
    
    Parameters:
    pattern (str): The string to search for in the file.
    file_name (str): The name of the file to search.
    """
    try:
      
        with open(file_name, 'r') as file:
           
            found = False
            
            
            for line_number, line in enumerate(file, start=1):
                
                if pattern in line:
                    
                    print(f"{line_number}: {line}", end='') 
                    found = True
            
        
            if not found:
                print(f"No lines found containing '{pattern}' in '{file_name}'.")
    
    except FileNotFoundError:
        
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        
        print("Usage: python grep.py <pattern> <filename>")
    else:
        
        grep(sys.argv[1], sys.argv[2])