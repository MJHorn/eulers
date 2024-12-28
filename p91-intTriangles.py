# Euler Problem #91 - Right Triangles with Integer Coordinates. 
# Solved. Easy one!

import math

gridx = 51
gridy = 51

matches = []

for p1x in range(0,gridx):
    print(p1x)
    for p1y in range(0,gridy):
        for p2x in range(0,gridx):
            for p2y in range(0,gridy):
                d1 = math.sqrt((p2x-p1x)**2 + (p2y-p1y)**2)
                d2 = math.sqrt((p1x)**2 + (p1y)**2)
                d3 = math.sqrt((p2x)**2 + (p2y)**2)
                sides = sorted([d1,d2,d3])
                if not ((p1x == 0 and p1y ==0) or (p2x == 0 and p2y == 0)):
                    if not (p1x == p2x and p1y == p2y):
                        if round(sides[2]**2,6) == round(sides[1]**2 + sides[0]**2,6):
                            #print(f"({p1x}, {p1y}), ({p2x}, {p2y})")
                            matches.append(tuple(sorted(((p1x,p1y),(p2x,p2y)))))
                        #else:
                            #print(sides[2]**2, sides[1]**2 + sides[0]**2)

print(matches)
print(len(set(matches)))