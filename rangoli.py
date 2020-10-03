n=int(input("Enter"))
L=[]
for x in range(n):
    for y in range(x+1):
        pattern=chr(97+n-y+1)
        L.append(pattern)
        print(pattern)

n=int(input("Enter"))
L=[]
for x in range(n):
    pattern=chr(ord('a')+n-y-1) for y in range(x+1)
    print(pattern)

n=int(input("Enter"))
L=[]
for x in range(n):
    pattern='-'.join(chr(ord('a')+n-y-1) for y in range(x+1))
    print(pattern)

