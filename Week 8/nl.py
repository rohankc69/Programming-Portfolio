import sys  

def nl(file_name):
    """
    Function to print the contents of a file with line numbers.
    
    Parameters:
    file_name (str): The name of the file to read.
    """
    try:
        
        with open(file_name, 'r') as file:
            
            for line_number, line in enumerate(file, start=1):
                
                print(f"{line_number}\t{line}", end='')  
    except FileNotFoundError:
        #
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        
        print(f"An error occurred: {e}")

if __name__ == "__main__":
   
    if len(sys.argv) != 2:
        
        print("Usage: python nl.py <filename>")
    else:
       
        nl(sys.argv[1])