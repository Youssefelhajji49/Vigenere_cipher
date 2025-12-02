import string


def vigenere_cipher (text, key):
   
    text = text.upper()  
    key = key.upper()
    crypted_text = ""
    j = 0  
    for c in text:
        if c.isalpha():  
            shift = ord(key[j % len(key)]) - ord('A')  
            new_c = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))  
            crypted_text += new_c  
            j += 1  
        else:
            crypted_text += c  
    return crypted_text 

print(vigenere_cipher(text = 'bonjour' , key= 'cle'))