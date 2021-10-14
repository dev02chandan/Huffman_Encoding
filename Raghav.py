def count_freq(code):
  freq = {}
  char = []                                                    # This list will hold distinct elements from the given string
  for i in code:
    if i not in char:
      char.append(i) 
        
  charCount = []                                               # This list will hold Frequency of each element in the char list
  for i in char:
    charCount.append(code.count(i))


  freq= {char[i]:charCount[i] for i in range(len(char))}
  return freq
