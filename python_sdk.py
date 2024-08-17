# Create a new account
from algosdk import account, encoding

# Generate a new account
private_key, address = account.generate_account()

print("Private key: ", private_key)
print("Address: ", address)

# Check if the address is valid
if encoding.is_valid_address(address):
    print("Invalid address: ", address)
else:
    print("The address is not valid")
