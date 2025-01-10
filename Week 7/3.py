def main():
   
    country_capitals = {}

    while True:
      
        country = input("Enter the name of a country (or type 'exit' to quit): ").strip()

        
        if country.lower() == 'exit':
            print("Exiting the program.")
            break

       
        normalized_country = country.lower()

       
        if normalized_country in country_capitals:
            print(f"The capital of {country} is {country_capitals[normalized_country]}.")
        else:
            
            capital = input(f"I don't know the capital of {country}. Please enter it: ").strip()
            
            country_capitals[normalized_country] = capital
            print(f"Thank you! The capital of {country} has been recorded as {capital}.")

if __name__ == "__main__":
    main()