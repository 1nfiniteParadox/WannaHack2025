def decrypt_flag(flag_array, key):
    decrypted = ''
    for i in range(len(flag_array)):
        decrypted += chr(flag_array[i] ^ ord(key[i % len(key)]))
    return decrypted

# Encrypted flag array from the JavaScript code
flag_array = [58, 14, 0, 5, 4, 49, 12, 12, 5, 16, 40, 74, 88, 90, 55, 52, 85, 65, 43, 58, 91, 40, 81, 78, 94, 43, 49, 33, 80, 4]

# Known part of the message (we can guess some letters like "Welcome")
possible_keys = ['WannaHack{']

# Brute-force to check which key works
for key in possible_keys:
    decrypted_flag = decrypt_flag(flag_array, key)
    print(f'Trying key "{key}": {decrypted_flag}')
