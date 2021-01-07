def findSum(s):
    i = 0
    sum = 0
    while(i<len(s)):
        if s[i].isdigit():
            temp = ""
            while(i<len(s) and s[i].isdigit()):
                temp+=s[i]
                i+=1
            sum = sum + int(temp)
        i+=1
    return sum
