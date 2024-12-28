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

psum = 0
a = 0
maxdif = 0
done = 0

for a in range(1000000):
    k = 1
    psum = 0
    if a%10000 == 0:
        print(a)
    while psum < 1000000:
        psum = sum(prinos[a:a+k])
        if psum in prinos:
            if k > maxdif:
                print(psum,a,k)
                maxdif = k
        k += 1
