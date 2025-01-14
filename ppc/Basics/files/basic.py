from pwn import remote

# Connect to the given URL and port
r = remote('wannahack.iitbhucybersec.in', 18183)

# Function to calculate square and return the result
def get_square(number):
    return number * number

r.recvuntil("I GIVE: ")

# Start the interaction loop
for _ in range(100):
    # Receive input from the server
    r.recvuntil("I GIVE: ")
    input_number = int(r.recvline().decode().strip())
    print(input_number)
    
    # Calculate the square of the input number
    result = get_square(input_number)
    print(result)
    
    # Send the result back to the server
    r.sendline(str(result))
    print(r.recvline().decode().strip() , "\n")

# Final flag will be received after completing 100 rounds
flag = r.recvall().decode()
print("Flag:", flag)

r.close()
