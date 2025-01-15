## Description
So I was recently rewatching "The Social Network" (you can find it on Netflix'''). Anyway, Mark Zuckerberg decides to create a website called FaceMash, and for that, he needs Facebook images from multiple dorms. Naturally, he writes a script to grab data from all over the campus network.

He gets into a lot of trouble, ignoring that and do the same thing, scrape the data of each hostel, merge into one, and submit it on the verification page, that will give you the flag.

'''or you can just sail the high seas, or maybe just [youtube](https://www.youtube.com/watch?v=MIIPn95YYHs)

## Solution
The challenge was of scraping data from 5 different hostel pages and submit it in a particular format to get the flag.

For Hostel A
The data was in tables
![Pasted image 20250114184627.png](./files/20250114184627.png)

This is the code I used to scrape data from Hostel A
![Hostel A.py](./files/Hostel_A.py)

For Hostel B
The data was in cards
![Pasted image 20250114191525.png](./files/20250114191525.png)

This is the code I used to scrape data from Hostel B
![Hostel B.py](./files/Hostel_B.py)

For Hostel C
The data was in the following form
![Pasted image 20250114191745.png](./files/20250114191745.png)

This is the code I used to scrape data from Hostel C
![Hostel C.py](./files/Hostel_C.py)

For Hostel D
The data was in the following form
![Pasted image 20250114194451.png](./files/20250114194451.png)

This is the code I used to scrape data from Hostel D
![Hostel D.py](./files/Hostel_D.py)

For Hostel E
The data was in the following form
![Pasted image 20250114194554.png](./files/20250114194554.png)
The page has lazy loading so I changed my code accordingly.

This is the code I used to scrape data from Hostel E
![Hostel E.py](./files/Hostel_E.py)

After that I compiled and submitted the data in the portal and received the flag.
![Pasted image 20250114200358.png](./files/20250114200358.png)

## Flag
WannaHack{r3plt1llian_bill10na1r3_QE3sq5Fc}
