'''
n=int(input("Enter"))
L=[]
for x in range(n):
    for y in range(x+1):
        pattern=chr(97+n-y+1)
        L.append(pattern)
        print(pattern)
'''

'''
n=int(input("Enter"))
L=[]
for x in range(n):
    pattern=chr(ord('a')+n-y-1) for y in range(x+1)
    print(pattern)
'''
'''
n=int(input("Enter"))
L=[]
for x in range(n):
    pattern='-'.join(chr(ord('a')+n-y-1) for y in range(x+1))
    print(pattern)
'''
n=int(input("Enter"))
local=n
L=[]
for x in range(n):
    pattern='-'.join(chr(ord('a')+n-y-1) for y in range(x+1))
    print((pattern+pattern[::-1][1:]).center(4*n-3,'-')) #explain the pattern of max length

for x in range(n-1):
    pattern='-'.join(chr(ord('a')+n-y-1) for y in range(n-x-1))
    print((pattern+pattern[::-1][1:]).center(4*n-3,'-')) #explain the pattern of max length


"""
n=1 : 1
n=2 : 3
n=3 : 9
n=4 : 7


"""
