a,b = 0,1
n = int(input("Length of fibonacci sequence: "))

while b < n:
    print(b)
    a,b = b, a+b
