def powern(x,n):
    s = 1 
    while n > 0:
        n = n-1
        s = s * x
    return s
a = powern (5,6)
print (a)
