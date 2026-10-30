from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

message = b"Harsh Salvi"

signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Original Message: ", message.decode())
print("Digital Signature: ",signature.hex())

try:
    public_key.verify(
        signature,message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("\n Signature Verified successfully")
except:
    print("\n Signature Verification failed")

modified_message = b"Cristiano Ronaldo"
print("\n Modified Message: ",modified_message.decode())

try:
    public_key.verify(
        signature,modified_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature Verification: SUCCESS")
except Exception:
    print("Signature Verification: FAILED")