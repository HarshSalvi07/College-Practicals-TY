#Encryption code
def encrypt(text, shift):
    result = ""             #Stores encrypted messsage

    #Upper case english alphabets
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Read each character one by one
    for ch in text:

        #Encrypt only if the character is in alphabet
        if ch in alphabets:

            #Finding the position of the character
            index = alphabets.index(ch)

            #Shift the position and wrap around using modulus
            new_index = (index + shift) % 26

            #Add the encrypted character
            result += alphabets[new_index]

        else:
            #Keep spaces and speacial characters unchanged
            result += ch

    return result


#Decryption code
def decrypt(text, shift):
    result = ""           #Stores decrypted message

    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Read each encrypted character
    for ch in text:

        if ch in alphabets:

            #Finding the position of the character
            index = alphabets.index(ch)

            #Shift backwards to get original letter
            new_index = (index - shift) % 26

            #Add decrypted character
            result += alphabets[new_index]

        else:
            #Leave spaces and symbols unchanged
            result += ch
    return result


#Taking input from the user
message = input("Enter message: ").upper()          #Convert input to uppercase

shift = int(input("Enter Shift: "))         #Number of positions to shift

#Encrypt the message
cipher = encrypt(message, shift)
print("Encrypted message:" , cipher)

#Decrypt the message
plain = decrypt(cipher, shift)
print("Decrypted message:", plain)

