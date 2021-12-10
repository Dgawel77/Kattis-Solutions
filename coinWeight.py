# m, k = map(int, input().split())
# total = 0
# if k == 1:
#     print((m-1) * (2*k+1)**2)
# elif m == 1:
#     print(3)
# else:
#     for x in range(1, k+1):
#         total = (total + (k // x) * 2 - 1) % 998244353
#     print((m-1)*((2*k+1)**2 - total * 2) % 998244353)

# def pow(a,k):
#     'fast exponentiation'
#     res=1
#     while k:
#         if k&1:
#             res = (a*res) % 998244353
#         k >>= 1
#         a = (a*a) % 998244353
#     return res % 998244353

# m, k = map(int, input().split())

# mu = {}        # multipliers
# primes = []    # prime numbers in increasing order
# comp = []      # composite numbers whose prime factorization is of the form
#                # p1*p2*p3*...*pk where k>=2 and pi != pj
# numlst = [i for i in range(2,k+1)]
# while len(numlst) > 0:
#     p = numlst[0]      # first element p of lst is a prime number
#     mu[p] = -1         # multiplicative factor for prime p is -1
#     numlst = [i for i in numlst if i%p != 0] # remove multiples of p from lst
#     tmplist = []       
#     for i in comp:     # compute all comp numbers of type p*i where i is a comp
#         if p*i <= k:   # that is a product of smaller primes 
#             mu[p*i] = -mu[i]
#             tmplist.append(p*i)
#     comp += tmplist
#     for i in primes:   # compute all comp numbers of type p*i where i is a
#         if p*i <= k:   # smaller prime
#             mu[p*i] = 1
#             comp.append(p*i)
#     primes.append(p)

# # print(primes)
# # print(comp)
# # print(mu)

# # the maximum number of coins is (2k+1)**m ...
# total = pow(2*k+1, m) % 998244353
# # ... minus those combinations that are multiples of each other 
# for i in range(2, k+1):
#     if i in mu:
#         total += (mu[i] * pow(k//i * 2 + 1, m) - mu[i])
#         total = total % 998244353

# print(total)


def pow(a,k):
    'fast exponentiation'
    res=1
    while k:
        if k&1:
            res = (a*res) % 998244353
        k >>= 1
        a = (a*a) % 998244353
    return res % 998244353


N,tot=2000007,0
mu,pr,iss,pw=[0]*N,[0]*N,[0]*N,[0]*N
mu[1]=1

m, k = map(int, input().split())

for i in range (2,k+1):
    if not iss[i]:
        mu[i]=-1
        tot+=1
        pr[tot]=i
    j=1
    while pr[j]*i<=k:
        iss[i*pr[j]]=1
        if not (i%pr[j]):
            break
        mu[i*pr[j]]=-mu[i]
        j+=1

# the maximum number of coins is (2k+1)**m ...
total = pow(2*k+1, m) % 998244353
# ... minus those combinations that are multiples of each other 
for i in range(2, k+1):
    # if i in mu:
    total += (mu[i] * pow(k//i * 2 + 1, m) - mu[i])
    total = total % 998244353

print(total)

