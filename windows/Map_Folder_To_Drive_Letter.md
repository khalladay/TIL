# Map Folder To Drive Letter 

I set this up a long time ago and forgot how I did it (and then a windows update broke whatever I did). In order to speed up navigating my computer from a shell, I map my Development directory as a W: drive. 

Doing this in a terminal is super easy: 

'''powershell
Subst W: <path to folder>
'''

The trick is getting this to run at startup so you don't have to do it every time. For that, you can add a key to your registry to run the above command on startup: 

1. Create a new item in the following directory: 

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```
2. Set the value of that key to the command from above (Subst W: ....)

