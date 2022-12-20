import bitcoin import *
# Create Private Key
Private_key = random_key()
print(Private_key)
# Create Public key
public_key = privtopub(Private_key)
print(public_key)
# Create a Bitcoin Address
address = pubtoaddr(public_key)
print("my Address is : " + address)