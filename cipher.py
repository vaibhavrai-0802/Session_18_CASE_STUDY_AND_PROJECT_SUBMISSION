import numpy as np
import os

class Cipher():
    key = np.random.randint(1,50)
    key_file = open("C:\\Users\\VAIBHAV\\Acadgild\\key", 'w')
    key_file.write(str(key))
    key_file.close()

    def __init__(self):
        self.in_str = input("Enter string to encrypt/decrypt: ")
    
    def encrypt(self):
        encrypt_chars = []
        key = Cipher.key
        for i in range(len(self.in_str)):
            #key_c = key[i % len(key)]
            encrypt_c = chr(ord(self.in_str[i]) + key % 256)
            encrypt_chars.append(encrypt_c)
        encrypt_string = "".join(encrypt_chars)
        print ("encoded_string: ", encrypt_string)
        return encrypt_string
    
    def decrypt(self, encr_str=""):
        decrypted_chars = []
        key = Cipher.key
        for i in range(len(encr_str)):
            #key_c = key[i % len(key)]
            decrypted_c = chr(ord(encr_str[i]) - key % 256)
            decrypted_chars.append(decrypted_c)
        decrypted_string = "".join(decrypted_chars)
        print ("decrypted_string: ", decrypted_string)
        return decrypted_string