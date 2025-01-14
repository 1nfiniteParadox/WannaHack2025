from pwn import remote

conn = remote('wannahack.iitbhucybersec.in', 36186)
low, high = 1, 100000000

for _ in range(30):
    conn.recvuntil(b'YOUR GUESS: ')
    guess = str((low + high) // 2)
    conn.sendline(guess)

    feedback = conn.recvline().decode().strip()
    if "GO LOWER" in feedback:
        high = int(guess) - 1
    elif "GO HIGHER" in feedback:
        low = int(guess) + 1
    elif "CORRECT" in feedback:
        break

print(conn.recvall().decode())
conn.close()
