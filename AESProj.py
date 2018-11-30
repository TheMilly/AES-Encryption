from Crypto.Cipher import AES
import os
import base64
# Initialization
#-----------------------------------------------------------------------------------
# AES 128 -- 16 BYTE Blocks, AES 192 -- 24, AES 256 -- 32
BLOCK_SIZE = 16
key = os.urandom(16)
iv = os.urandom(16)

message = 'Please Encrypt this message! Please do not let this get hacked!'
#print("The key is: ", key)
#print("The IV is: ", iv)
#-----------------------------------------------------------------------------------

# Select Mode of Operation
#-----------------------------------------------------------------------------------
# When changing mode of operation, be sure to take into consideration if
# The selected mode utilizes an initialization vector
#mode = AES.MODE_OFB
#mode = AES.MODE_CBC
mode = AES.MODE_ECB
#-----------------------------------------------------------------------------------

# Create an AES object which contains the key, mode, and initialization vector
#-----------------------------------------------------------------------------------
cipher = AES.new(key,mode)
#cipher = AES.new(key,mode,iv)
#-----------------------------------------------------------------------------------

# Pad the message to have a multiple of 16 bytes 
def pad(s):
    return s + ((BLOCK_SIZE-len(s) % BLOCK_SIZE) * '{')

# Simply calling the aes encryption process on the message 
# (Note: Pad is called within the encryption method)
def encrypt(plaintext):
    global cipher
    return cipher.encrypt(pad(plaintext))

# Calling decrypt on the ecrypted ciphertext, notice how there will still
# be all the '{'s padded onto the original message. We must count these,
# and then only return the range of characters prior to the padding.
def decrypt(ciphertext):
    global cipher
    dec = cipher.decrypt(ciphertext)
    l = dec.count('{')
    return dec[:len(dec)-l]

#--------------------------------------------------------------------------
print("Message: ", message)
encrypted = encrypt(message)
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
# Must create new AES object to use when decrypting, since the other AES object
# was used to encrypt, its contents were altered. Ensure we are inputting the 
# same key,mode and iv paramaters into this decryption object.
cipher = AES.new(key,mode)
#cipher = AES.new(key,mode,iv)

decrypted = decrypt(encrypted)
#--------------------------------------------------------------------------

print("Encrypted Message: ", encrypted)
print("Decrypted Message: ", decrypted)
