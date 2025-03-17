def get_permutations(txt):
    listoftxt = []
    if len(listoftxt)==1:
        return listoftxt
    for i in range(len(txt)):
        listoftxt.append(txt[i])
    return get_permutations    


