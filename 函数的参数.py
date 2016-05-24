def power(x):
    return x*x
s=power(10)
print(s)



def power1(x, n):
    s1 = 1
    while n > 0:
        n = n - 1
        s1 = s1 * x
    return s1
ss=power1(5,4)
print(ss)