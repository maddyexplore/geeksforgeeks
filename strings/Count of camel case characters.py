for i in range(int(input())):
    temp = input()
    cnt=0
    for i in temp:
        if i.isupper():
            cnt+=1
    print(cnt)
