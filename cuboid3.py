import math

threshold = 10**6
intcount = 2060

M=100
all = []

while intcount < threshold:
    oldM = M
    M = oldM + 1
    for x in range(oldM+1,M+1):
        for ypz in range(2,2*x):
            s = math.sqrt(ypz**2 + x**2)
            if s%1 == 0:
                for y in range(1,ypz):
                    z=ypz-y
                    if max([x,y,z]) <= M :
                        if y <= z:
                            #print(x,y,z)
                            intcount += 1
                            all.append(tuple(sorted([x,y,z])))
                            if intcount%100000 == 0:
                                print("Up to ",intcount)




print(M)