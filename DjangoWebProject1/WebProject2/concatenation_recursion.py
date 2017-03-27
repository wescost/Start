def is_concatenate(word, dictionary):
    if(word == ""):
        return True
    for i in range(1,len(word)+1):
        if(word[0:i] in dictionary and is_concatenate(word[i:], dictionary)):
                return True

    return False

print(is_concatenate("aaaaaaa",["aab","aa","aaa","cdf"]))