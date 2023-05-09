import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)


#comment these if you are decrypting
#print(f"chars: {chars}")
#print(f"key :{key}")


#encrypt
plain_text = input("enter text to encrypt :")
cipher_text = " "


for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]


print(f"original message is : {plain_text}")
print(f"encrypted message is : {cipher_text}")

#decrypt
cipher_text = input("enter text to decrypt :")
plain_text = " "


for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message is : {cipher_text}")
print(f"original message is : {plain_text}")