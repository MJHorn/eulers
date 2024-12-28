limit = 1000000
primes = [True]*limit
primes[0] = primes[1] = False
sums = 0

for (a, isprime) in enumerate(primes):
  if isprime: 
    for n in range(a*a, limit, a):
      primes[n] = False

prinos = []

for n in range(len(primes)):
  if primes[n]:
    prinos.append(n)

