# Create a New User On A Linux Machine

```bash
sudo useradd -u 1500 -s /bin/bash -m -d /customhome -g LoginGroupName [UserName]
```

* -s specifies login shell (s for shell)
* -m creates a user home directory in /home/username
* -d lets you specify a home directory
* -g lets you specify the login group for the user
* -u lets you specify a specific user id