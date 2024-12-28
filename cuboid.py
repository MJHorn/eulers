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
            for z in range(y,M+1):
                s1 = math.sqrt(x**2 + (y+z)**2)
                if s1%1 == 0:
                    print(x,y,z,s1,s1**2-x**2)
                    intcount += 1
                    if intcount%1000 == 0:
                        print("Up to ",intcount)
               

print(M)