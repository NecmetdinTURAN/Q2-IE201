def get_permutations(txt=str):
    listoftxt = []
    right_to_the_before =
    left_to_the_before =
    listoftxt.append(txt[len(-1:)])
    return get_permutations(txt(:-1))+txt(len(txt)) txt(len(txt))+get_permutations(txt(:-1))


