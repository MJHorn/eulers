from operator import itemgetter
import csv
import matplotlib.pyplot as plt

def quad(p1):
  if p1[0] == 0 or p1[1] == 0:
    p1.append(0)
  else:
    if p1[0] < 0 and p1[1] < 0:
      p1.append(3)
    elif p1[0] < 0 and p1[1] > 0:
      p1.append(2)
    elif p1[0] > 0 and p1[1] > 0:
      p1.append(1)
    else:
      p1.append(4)
  return p1

def xint(p1,p2):
  return p1[0] - p1[1]*((p2[0] - p1[0])/(p2[1] - p1[1]))

def plot(points):
  plt.polygon(points[0][0],points[0][1],'ro-')
  plt.plot(points[1][0],points[1][1],'ro-')
  plt.plot(points[2][0],points[2][1],'ro-')
  plt.show()



notSum = 0
inclSum = 0
tris = []
pflag = 0

with open('triangles.txt') as csvfile:

  readCSV = csv.reader(csvfile, delimiter=',')

  for row in readCSV:
    Triangles = list(map(int,row)) 
    #Triangles = [-340,495,-153,-910,835,-947]
    #Triangles = [-175,41,-421,-714,574,-645]

    p1 = quad([Triangles[0],Triangles[1]])
    p2 = quad([Triangles[2],Triangles[3]])
    p3 = quad([Triangles[4],Triangles[5]])

    points = [p1,p2,p3]

    quads = list(set([p1[2],p2[2],p3[2]]))

    points = sorted(points, key=itemgetter(2))

    if (points[0][0] == 0) or (points[0][1] == 0) or (points[0][2] == 0):
      print(points)
      pflag = 1
      
    if len(quads) == 3:
      if sum(i < 3 for i in quads) == 2: #two points up
        int1 = xint(points[0],points[2])
        int2 = xint(points[1],points[2])
      else: # two points down
        int1 = xint(points[0],points[1])
        int2 = xint(points[0],points[2])
    elif len(quads) < 3:
      int1 = 1
      int2 = 1
    else:
      print("WEIRD")

    if int1*int2 <= 0:
      if pflag == 1:
        print("Origin included")
      inclSum += 1
      points.append("YES")
      tris.append(points)
    else:
      if pflag == 1:
        print("Origin not included")
      notSum += 1
      points.append("NO")
      tris.append(points)  
      
    pflag = 0    

print(inclSum)