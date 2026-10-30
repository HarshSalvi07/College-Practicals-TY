from math import gcd

def mod_inverse(e,phi):
    for d in range(1,phi):
        if (d*e)%phi == 1:
            return d
    return None

p = int(input("Enter the first prime number(p): "))
q = int(input("Enter the second prime number(q): "))

n = p*q

phi = (p-1)*(q-1)

e = int(input("Enter a value of e: "))
while gcd(e,phi)!=1:
    print("e must be another co-prime with", phi)
    e = int(input("Enter another value for e: "))

d = mod_inverse(e,phi)
print("\n Public Key: ", (e,n))
print("\n Private Key: ", (d,n))

message = int(input("Enter Message(number less than n) : "))

cipher = pow(message, e, n)
print("Encrypted Message : ", cipher)

plain = pow(cipher, d, n)
print("Decrypted Message : ", plain)