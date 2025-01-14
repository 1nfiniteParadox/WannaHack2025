## Description
I made a file upload site, you can also share the uploaded files with your friends (if you have any).
Anyway in the root directory there exists a file flag.txt. I don't know what to do with it.

## Solution
Since the flag is in the root directory, I tried for path traversal.

![[Pasted image 20250114200837.png]]

First I uploaded any file to the system so that I can get the path in the url.

![[Pasted image 20250114201010.png]]

Now that I know the path, I simply edited it to "../flag.txt"

![[Pasted image 20250114201435.png]]

## Flag
WannaHack{tr4v3rs3_th3_p4th_6iS9zRNk}