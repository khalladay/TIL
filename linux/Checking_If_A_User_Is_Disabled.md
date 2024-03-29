# Checking If A User's Account Is Disabled On A Linux Machine

There's a bunch of ways to disable an account: 

* You can add a '!' to the start of the password hash in the shadow file with usermod -L
* you can set the account to expired 
* you can change the default shell to /bin/false or /sbin/nologin

Determining _if_ an account is disabled requires checking all three

```bash
; look for an 'L' in the output of passwd to specify a locked account
passwd --status [username]

; chage displays if an account is expired
chage -l [username]

; look for what the default shell is for the user
grep ^[username] /etc/passwd
```