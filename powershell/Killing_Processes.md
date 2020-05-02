# Killing Processes

Powershell uses the Stop-Process commandlet to kill running processes. You can use it to easily kill a single process by Id, or all processes that share a name, like so: 

```powershell
Stop-Process -Name Notepad -Force
Stop-Process -Id 3321 -Force
```

The "-Force" option tells the commandlet to skip asking you to confirm that you want to kill a process (alternatively, the -Confirm option will _require_ that you confirm this action). 
