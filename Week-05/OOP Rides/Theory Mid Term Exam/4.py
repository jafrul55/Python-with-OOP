def Anagram(words):
    anagram_dic = {}
    for word in words:
        sorted_word = "".join(sorted(word))
    
        if sorted_word in anagram_dic:
            anagram_dic[sorted_word].append(word)
        else:
            anagram_dic[sorted_word] = [word]
    return list(anagram_dic.values())


LIST = ['eat','ate','done','tea','soup','node']
val = Anagram(LIST)
print(val)

        
