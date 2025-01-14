from pwn import xor

DATA = open('audio.wav', 'rb').read()
KEY = b'FAKE_KEY'       #I used the name of my favourite soup as the key. Good luck finding that out

print(xor(DATA, KEY))