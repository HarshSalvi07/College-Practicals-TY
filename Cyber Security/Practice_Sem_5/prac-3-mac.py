import hmac
import hashlib

def generate_mac(message, key):
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()

message = input("Enter the message: ")
key = input("Enter the secret key: ")

mac = generate_mac(message, key)
print("\nGenerated MAC:", mac)

received_message = input("\nEnter received message: ")
received_key = input("Enter secret key: ")
received_mac = input("Enter received MAC: ")

new_mac = generate_mac(received_message, received_key)

if hmac.compare_digest(new_mac, received_mac):
    print("\nMAC Verified Successfully!")
    print("Message is Authentic. Data Integrity Maintained.")
else:
    print("\nMAC Verification Failed!")
    print("Message Tampered or Incorrect Key!")

tampered = input("\nEnter modified message: ")
tampered_mac = generate_mac(tampered, key)

print("\nOriginal MAC:", mac)
print("Modified MAC:", tampered_mac)

if not hmac.compare_digest(mac, tampered_mac):
    print("Message Tampering Detected!")
else:
    print("No Tampering Detected!")