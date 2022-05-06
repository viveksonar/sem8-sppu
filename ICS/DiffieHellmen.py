#Diffie hellmen is a key exchange algorithm thorugh which sender and reciever gets a common generated shared key

p = int(input("enter prime no. : "))
g = int(input("enter primitve root (generator) for the above prime number : "))

a = int(input("input private key for A : "))
b = int(input("input private key for B : "))

A = (g**a)%p
B = (g**b)%p
# A and B are public key for user 'A' and 'B' respectively

secret_a = ( B**a) % p
secret_b = ( A**b) % p

if( secret_a == secret_b ):
	print("A and B can communicated using shared key ", secret_b)

else:
	print("common shared key could not be generated")

# The primitive root of a prime number n is an integer r between[1, n-1] such that the values of r^x(mod n) where x is in the range[0, n-2] are different.
