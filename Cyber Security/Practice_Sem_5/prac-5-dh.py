p = int(input("Enter prime number(p): "))
g = int(input("Enter primitive root(g): "))

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

A = pow(g,a,p)
B = pow(g,b,p)

KA = pow(B,a,p)
KB = pow(A,b,p)

print("\n Alice's public key: ",A)
print("\n Bob's public key: ",B)

print("\n Alice's shared secret key: ",KA)
print("\n Bob's shared secret key: ",KB)

if KA == KB:
    print("Key exchange successfull")
else:
    print("Key exchange failed")