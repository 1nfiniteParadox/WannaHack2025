## Description
A race condition in Apache HTTP Server mod_auth_digest allows bypassing access controls. Identify the version where this issue is fixed.

Flag Format WannaHack{x.x.x} where x.x.x is version required.

## Solution
The race condition in the mod_auth_digest module of the Apache HTTP Server, identified as CVE-2019-0217, was addressed in version 2.4.39.

## Flag
WannaHack{2.4.39}