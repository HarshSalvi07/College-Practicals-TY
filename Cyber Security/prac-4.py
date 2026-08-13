#Import RSA functioality for generating RsA public and private keys
from cryptography.hazmat.primitives.asymmetric import rsa

#Import padding required for  secure rsa singnatures
from cryptography.hazmat.primitives.asymmetric import padding

#Import SHA-256 hash algorithm 
from cryptography.hazmat.primitives import hashes

#Generate an RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

#Obtain the original message that will be digitally signed
public_key = private_key.public_key()

#Define the original message that will be digitaslly signed
message = b"Cyber Security Practical"

#Generate the digital signiture using the private key
signature = private_key.sign(
    message,

    #Use RSA-PSS padding for secure RSA signartursa
    padding.PSS(

        #Use MGF1 WITH SHA-256
        mgf=padding.MGF1(hashes.SHA256()),

        #uSE A SALT having the  same length as SHA-2565 output

        salt_length=padding.PSS.MAX_LENGTH
    ),

    # Use SHA-256 as the hashing algorithm
    hashes.SHA256()

)

#Display the original message
print("\nDigital Signature:")
print(signature.hex())

#verify the digital signature using the public kry
try:
    #Verify the digital signature against the origanl message
    public_key.verify(
        signature,
        message,

        #Use the same RSA-PSS padding during verification
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("\nSignature Verificatrion: SUCCESS")

    print("The Message is authentic and has not been modified.")
except Exception:
    print("\nSigature Verification: FAILED")

    print("The message is not authetic or has been modified")

modified_message = b"Cyber Security Practical - Modified"

#Display the modified message
print("\nModified Message: ")
print(modified_message.decode())

try:
    public_key.verify(
        signature,
        modified_message,

        #Use the same RSA-PSS padding
        padding.PSS
        (mgf=padding.MGF1(hashes.SHA256()),
         salt_length=padding.PSS.MAX_LENGTH
         ),
         hashes.SHA256()
    )

    print("\nModified Message Verification: SUCCESS")

except Exception:
    print("\nModified Message Verification: FAILED")

    print("The message has been modified, so the signature is invalid")