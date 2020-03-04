def max_dist(s):
    count = [0]*256
    n = len(s)
    for i in range(n):
        count[ord(s[i])] +=1
    m_dist = 0
    for i in range(256):
        if count[i]!=0:
            m_dist += 1
    return m_dist

def func(s):
    n = len(s)
    m_dist = max_dist(s)
    minl = n

    for i in range(n):
        for j in range(n):
            sub = s[i:j]
            nsub = len(sub)
            sub_dist = max_dist(sub)

            if (nsub < minl) and (m_dist == sub_dist):
                minl = nsub

    return minl

s = input()
print(func(s))
