def firstAlphabet(self, S):
    lst = S.split()
    res = ""
    for i in lst:
        res+=(i[0])
    return res
