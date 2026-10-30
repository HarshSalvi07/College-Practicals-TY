def caesar(text,key):
    result = ""
    for char in text:
        if char.isalpha():
            cipher = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            result += cipher
        else:
            result += char
    return result

def decrypt_caesar(text, key):
    return caesar(text,-key)

plain_text = input("Enter Plain Text: ").lower().strip()
cipher_text = caesar(plain_text, 5)

print("Plain Text: ", plain_text)
print("Cipher Text: ", cipher_text)
print("Decrypt Text: ", decrypt_caesar(cipher_text,5))