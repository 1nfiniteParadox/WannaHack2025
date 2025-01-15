## Description
I found this messy javascript somewhere...have fun understanding it :)

## Given Files
![chall.js](./files/chall.js)

## Solution
The description hints at messy. 
So I asked ChatGPT to simplify this code.

![challenge.js](./files/challenge.js)

Used this code to bruteforce and find the key.

![bruteforce.py](./files/bruteforce.py)

Upon analyzing the simplified code I realized that the flag and the key can be used interchangeably and since I know that the flag will be of the form "WannaHack{".
I used it as the possible key, the code in return gave me the actual key - **monkey**

![Pasted image 20250114205720.png](./files/20250114205720.png)

When I ran the code again, this time with "monkey" as the possible key, it gave me the flag.

![Pasted image 20250114205813.png](./files/20250114205813.png)

## Flag
WannaHack{M355Y_08FU5C473D_J5}
