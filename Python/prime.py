# Normal intuitive prime finder
MAX_VAL = input("Input a number: ")
for x in range(2, MAX_VAL + 1):
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        print(x)

# Faster intuitive prime finder
from math import sqrt, floor
MAX_VAL = input("Input a number: ")
for x in range(2, int(MAX_VAL) + 1):
    for i in range(2, floor(sqrt(x))):
        if x % i == 0:
            break
    else:
        print(x)

# Sieve of Aratosthenes
MAX_VAL = int(input("Input a number: "))
prime_list = [] 
for i in range(MAX_VAL+1):
    prime_list.append(i)

prime_list[0]=0
prime_list[1]=0   

p = 2
while (p * p <= MAX_VAL): 
    if (p != 0): 
        for i in range(p*2, MAX_VAL+1, p): 
            prime_list[i] = 0

    p += 1

print("All the prime numbers up to", MAX_VAL, "are:")
for i in range(len(prime_list)):
    if (prime_list[i] != 0):
        print(prime_list[i], end=" ")

# 1 Line prime finder
print( list( x for x in range( 2, int( input( "Pick a number: " ) ) + 1 ) if all( map( lambda s: x % s, range( 2, x ) ) ) ) )
