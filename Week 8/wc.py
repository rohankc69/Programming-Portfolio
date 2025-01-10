import sys  

def wc(file_name):
    """
    Function to count the number of lines and characters in a file.
    
    Parameters:
    file_name (str): The name of the file to analyze.
    """
    try:
        
        line_count = 0
        char_count = 0
        
      
        with open(file_name, 'r') as file:
            
            for line in file:
                line_count += 1  
                char_count += len(line)  
        
       
        print(f"Lines: {line_count}, Characters: {char_count}")
    
    except FileNotFoundError:
        
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        
        print("Usage: python wc.py <filename>")
    else:
       
        wc(sys.argv[1])