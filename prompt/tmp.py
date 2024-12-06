def compress(s):
    res=""
    count=1
    last=s[0]
    for i in range(1,len(s)):
        if s[i]==last:
            count+=1
        else:
            last=s[i]
            res+=last+str(count)
            count=1
    return res

t = compress("aabbbca")
