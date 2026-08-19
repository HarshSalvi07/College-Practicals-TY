p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root (g): "))

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

A = pow(g,a,p)
B = pow(g,b,p)

KA = pow(B,a,p)
KB = pow(A,b,p)

print("\nAlice's public key: ", A)
print("Bob's public key: ", B)

print("\nAlice's shared secret key: ", KA)
print("Bob's shared secret key: ", KB)


if KA == KB:
    print("\nKey exchange is SUCCESSFULL!")