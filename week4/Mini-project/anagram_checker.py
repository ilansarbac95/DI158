# anagram_checker.py 
 
 class AnagramChecker: 
  def __init__(self): 
  """Loads the word list file into a variable.""" 
  with open("sowpods.txt", "r") as file: 
  self.word_list = [word.strip() for word in file] 
 

  def is_valid_word(self, word): 
  """Checks if the given word is a valid word.""" 
  return word.upper() in self.word_list 
 

  def get_anagrams(self, word): 
  """Finds all anagrams for the given word.""" 
  word = word.upper() 
  sorted_word = sorted(word) 
  anagrams = [] 
  for w in self.word_list: 
  if sorted(w) == sorted_word and w != word: 
  anagrams.append(w) 
  return anagrams 
 

  def is_anagram(self, word1, word2): 
  """Compares 2 words and returns True if they are anagrams, False if not.""" 
  word1 = word1.upper() 
  word2 = word2.upper() 
  return sorted(word1) == sorted(word2) and word1 != word2
