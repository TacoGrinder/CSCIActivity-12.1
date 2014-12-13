__author__ = 'ortus'

#1
def mxel(l):
    m = []
    for i in l:
        n = max(i)
        m.append((n, i))
        m.sort()
        m.reverse()
    print(m)

#2
def mean(*a):
    q = 0
    for i in a:
        q += i
    z = q/len(a)
    print(z)

mxel([[1,2],[1,-1],[5,8],[-4,-2],[4,3]])

mean(1,2,3)