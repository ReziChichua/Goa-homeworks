def speedify(st): 
    result = [' '] * (len(st) + 25)
    
  
    for index, char in enumerate(st):
      
        new_position = index + ord(char) - ord('A')

        result[new_position] = char

    return ''.join(result).rstrip()