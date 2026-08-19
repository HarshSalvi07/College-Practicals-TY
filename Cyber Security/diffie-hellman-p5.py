## Diffie-Hellman key exchange
p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

## Public keys
A = pow(g, a, p)
B = pow(g, b, p)

## Shared secret keys
KA = pow(B, a, p)
KB = pow(A, b, p)

print("\nAlice's public key: ", A)
print("Bob's Public Key: ", B)

print("\nAlice's Shared Secret: ", KA)
print("Bob's Shared Secret: ", KB)

if KA == KB:
    print("\nKey Exchange Successfull!")
    