cubeNumberSum = 0
cubeNumber = 0
i = 0
while cubeNumber < 50000000:
    cubeNumber = i**3
    if cubeNumber < 50000000:
      cubeNumberSum += cubeNumber
    i += 1
print(cubeNumberSum)