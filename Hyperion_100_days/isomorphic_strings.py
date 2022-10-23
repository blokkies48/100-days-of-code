def func2(word_1: str,word_2: str, lst: list) -> int:
    return abs(lst.index(word_1) - lst.index(word_2))

word1 = "the"
word2 = "fox"
S = [ "the","quick", "brown", "fox", 
     "quick"]

print(func2(word1,word2,S))