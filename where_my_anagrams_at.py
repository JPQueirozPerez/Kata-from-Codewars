def anagrams(word, words):
    ana = []
    for i in range(len(words)):
        if(sorted(word) == sorted(words[i])): 
            ana.append(words[i])
    return ana
