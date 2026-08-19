def encrypt(text):
    even = ""
    odd = ""

    for i in range(len(text)):
        if i%2 == 0:
            even += text[i]
        else:
            odd += text[i]
    return even + odd

def decrypt(cipher):
    text = ""

    mid = (len(cipher) + 1) // 2
    even = cipher[:mid]
    odd = cipher[mid:]

    for i in range(len(odd)):
        text += even[i]
        text += odd[i]

    if len(even) > len(odd):
        text += even[-1]

    return text

msg = input("Enter a message: ")

enc = encrypt(msg)
print("Encrypted Message: ",enc)

dec = decrypt(enc)
print("Decrypted Message: ",dec)