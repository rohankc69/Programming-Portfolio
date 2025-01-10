import sys  

def compare_files(file1, file2):
    """
    Function to compare the contents of two files.
    
    Parameters:
    file1 (str): The name of the first file to compare.
    file2 (str): The name of the second file to compare.
    """
    try:
        
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
          
            content1 = f1.read()
            content2 = f2.read()
            
            
            if content1 == content2:
                print("The files are the same.")
            else:
                print("The files are different.")
    
    except FileNotFoundError as e:
        
        print(f"Error: {e}")
    except Exception as e:
        
        print(f"An error occurred: {e}")

if __name__ == "__main__":
   
    if len(sys.argv) != 3:
        
        print("Usage: python diff.py <file1> <file2>")
    else:
        
        compare_files(sys.argv[1], sys.argv[2])