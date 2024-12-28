import math

threshold = 10
intcount = 0

M=0
all = []

while intcount < threshold:
    oldM = M
    M = oldM + 1
    for x in range(oldM+1,M+1):
        for y in range(1,M+1):
        # go through square numbers bigger than x**2 to calculate possible zs
            z=y-1
            while ((z < M) and (intcount < threshold)):
                z+=1
                possibleBase = x+1
                possibleZ = math.sqrt(possibleBase**2 - x**2) - y
                if possibleZ%1 == 0:
#                s1 = math.sqrt(x**2 + (y+z)**2)
#                if s1%1 == 0:
                    print(x,y,z)
                    intcount += 1
                    if intcount%1000 == 0:
                        print("Up to ",intcount)
                    #elif intcount>threshold:
                    #    print(M,intcount)               

print(M)