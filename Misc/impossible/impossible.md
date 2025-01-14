## Description
Pretty sure my flag is safe as these conditions are IMPOSSIBLE lol

## Given Files
![[chall.py]]

## Solution
You want a string which satisfies the following conditions:
`len(s) >= 20
`len(s.upper()) == 25

In Python, the `str.upper()` function converts all lowercase letters in a string to their uppercase equivalents. For the German letter Eszett (ß), when you apply `str.upper()`, it will be converted to 'SS' since there is no single uppercase equivalent for 'ß'.

So, I input the string "ßßßßßßßßßßßßa" and got the flag

(The above string after `s.upper()` becomes "SSSSSSSSSSSSSSSSSSSSSSSSA")

## Flag
WannaHack{m0r3_l1k3_1_4m_p0551bl3_nhTTXAME}