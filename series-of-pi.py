from math import factorial
import numpy as np
import matplotlib.pyplot as plt

#question 
def ArcSin(iteration):
	s=0
	error=[]
	length=np.arange(iteration)
	for n in np.arange(iteration, dtype="int64"):
		a=factorial(2*n)/(factorial(n)*factorial(n))
		b=(16**n)*(2*n+1)
		series=3*a/b
		s=s+series
		er=np.abs(np.pi-s)
		error.append(er)
	return (length, error, s)
length, error, s=ArcSin(10)
fig, ax=plt.subplots()
ax.plot(length, error)
#ax.set_xscale("log")
plt.show()
print(s)


# def primes_upto(limit):
#     prime = [True] * limit
#     for n in range(2, limit):
#         if prime[n]:
#             yield n # n is a prime
#             for c in range(n*n, limit, n):
#                 prime[c] = False # mark composites

# primes=np.array(list(primes_upto(10000)))
# def LeonardEuler():
#     update=1
#     error=[]
#     for k in primes:
#         series=k**2/(k**2-1)
#         m=series
#         update=update*m
#         pi=np.sqrt(6*update)
#         er=np.abs(np.pi-pi)
#         error.append(er)
#     return (error, pi)
# error, pi=LeonardEuler()
# length=np.arange(1, len(primes)+1)
# fig, ax=plt.subplots()
# ax.plot(length, error)
# ax.set_xscale("log")
# plt.show()
# print(pi)