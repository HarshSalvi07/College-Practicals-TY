from math import gcd

def mod_inverse(e, phi):
    for d in range(1,phi):
        if (d*e)%phi == 1:
            return d
    return None

p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))

n = p*q
phi = (p-1)*(q-1)

e = int(input("Enter the value of E: "))
while gcd(e,phi)!=1:
    print("E must be co-prime with", phi)
    e = int(input("Enter another value of E: "))

d = mod_inverse(e,phi)
print("\nPublic Key: ",(e,n))
print("Private Key: ",(d,n))

message = int(input("Enter message (number less than n): "))

cipher = pow(message, e, n)
print("Encrypted Message: ",cipher)

plain = pow(cipher, d, n)
print("Decrypted Message: ",plain)