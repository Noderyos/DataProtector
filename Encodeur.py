import os
from hashlib import *

file_input = input("Chemin du fichier : ")
key = sha256(input("Mot de passe : ").encode('utf-8')).digest()
if ".ncrypt" in file_input:
    with open(file_input, 'rb') as f_input:
        with open(file_input.replace(".ncrypt",""),"wb") as f_output:
            i = 0
            while f_input.peek():
                c = ord(f_input.read(1))
                j = i % len(key)
                b = bytes([c^key[j]])
                f_output.write(b)
                i = i + 1
    print("Fichier Décodé")
else:
    with open(file_input, 'rb') as f_input:
        with open(file_input + ".ncrypt","wb") as f_output:
            i = 0
            while f_input.peek():
                c = ord(f_input.read(1))
                j = i % len(key)
                b = bytes([c^key[j]])
                f_output.write(b)
                i = i + 1
    print("Fichier Encodé")
os.remove(file_input)
