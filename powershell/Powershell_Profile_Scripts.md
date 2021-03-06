# Powershell Profile Scripts

Just like a bash profile, powershell supports profile scripts that run whenever a session is started. There's a few different locations that you can put these, but for my purposes, I want to set a profile for my user, all hosts, which means I need to create a file called "Profile.ps1" here: 

```
$Home\[My ]Documents\WindowsPowerShell\Profile.ps1
```

You can see what profile is currently loaded by examining the $Profile var in a powershell terminal. (or $PROFILE.AllUsersCurrentHost, $PROFILE.AllUsersAllHosts, $PROFILE.CurrentUserAllHosts)

Once you have a profile file there, you may get an error like: 

```powershell
File C:\Users\Kyle Halladay\Documents\WindowsPowerShell\profile.ps1 cannot be loaded because running scripts is
disabled on this system. For more information, see about_Execution_Policies at
https:/go.microsoft.com/fwlink/?LinkID=135170.
```

If so, you need to change your execution policy, with the following command (in an admin prompt)

```powershell
#Set policy to RemoteSigned (includes your own unsigned scripts)
Set-ExecutionPolicy RemoteSigned
```