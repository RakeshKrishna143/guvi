def gcd(a, b): 
    print(a,b)
    if (a == 0 or b == 0):
        return 0
    if (a==1 or  b==1):
        return 1
    if (a == b):
        return a
    if (a > b):
        return gcd(a - b, b)
    return gcd(a, b - a) 
		 


a = 68
b = 16
print(gcd(a, b) )

