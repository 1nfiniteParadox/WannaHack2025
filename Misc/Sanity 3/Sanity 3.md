## Description
You are getting to close to insanity :)
You know there are channels hidden from you?

## Solution
The description hinted at hidden channels.
I downloaded and installed a discord plugin named _$ShowHiddenChannels$_.
This allowed me to view the title and description of hidden channels which can't be accessed due to Role Restrictions.

I found 2 hidden channels which could potentially have the flag.

![[Pasted image 20250114012007.png]]

![[Pasted image 20250114012036.png]]

The title of this channel seemed like a Base 64 encoding.
Since, discord titles are forced into lower case only. I figured that some letters must be in upper case for the decoding to work properly.
After some trial and error I found the correct string - **V2FubmFIYWNre2Qxc2MwcmRf**

![[Pasted image 20250114012950.png]]

I got the first half of the flag - **WannaHack{d1sc0rd_**

![[Pasted image 20250114013229.png]]

The description of the channel "part-2" was a Base 64 encoded string which gave the second half of the flag - **k1_mkc_6969}**

## Flag
WannaHack{d1sc0rd_k1_mkc_6969}