def decrypt(ciphertext, key):
    plaintext = ""
    divisor = key * 311
    for num in ciphertext:
        plaintext += (chr(num // divisor))
    return plaintext

def decrypt_xor(ciphertext, key):
    plaintext = ""
    key_len = len(key)
    for i, char in enumerate(ciphertext):
        key_char = key[i % key_len]
        decrypt_char = chr(ord(char) ^ ord(key_char))
        plaintext += decrypt_char
    return plaintext[::-1]

def generate(g, x, p):
    return pow(g, x) % p

p = 97 
g = 31
a = 95 
b = 21

key = "trudeau"

u = generate(g, a, p)
v = generate(g, b, p)
key_shared = generate(u, b, p)

ciphertext = [237915, 1850450, 1850450, 158610, 2458455, 2273410, 1744710, 1744710, 1797580, 1110270, 0, 2194105, 555135, 132175, 1797580, 0, 581570, 2273410, 26435, 1638970, 634440, 713745, 158610, 158610, 449395, 158610, 687310, 1348185, 845920, 1295315, 687310, 185045, 317220, 449395]

plaintext_after_decrypt1 = decrypt(ciphertext, key_shared)
plaintext_after_decrypt2 = decrypt_xor(plaintext_after_decrypt1, key)

print(f"the flag is: {plaintext_after_decrypt2}")