def frequency_analysis(message):
  
    letter_counts = {}
    
    
    for char in message.lower():  
        if char.isalpha():  
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    
 
    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    
  
    print("Six most common letters:")
    for letter, count in sorted_letters[:6]:
        print(f"{letter}: {count}")


if __name__ == "__main__":
    message = """
    Tqfdmbtrm tgfo xmbk. Fqfbsqbtm yplz cbmlbozqo eib tgfo. Ltzl tgfo cbrffbo
    tgfo yfohbo bqfxfq.
    """
    frequency_analysis(message)
