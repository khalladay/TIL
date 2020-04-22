# Use "Requires" Statements to Ensure Preconditions

 I had a need to ensure that a powershell script was run as admin (since I wanted to automate chocolatey installs), and stumbled on this handy powershell feature. You can add #Requires statements to the beginning of a script to set preconditions that must be met in order for a script to run. 
 
 ```powershell
#Requires -Assembly { <Path to .dll> | <.NET assembly specification> }
#Requires -Version <N>[.<n>]
#Requires -PSSnapin <PSSnapin-Name> [-Version <N>[.<n>]]
#Requires -Modules { <Module-Name> | <Hashtable> }
#Requires -PSEdition <PSEdition-Name>
#Requires -ShellId <ShellId> -PSSnapin <PSSnapin-Name> [-Version <N>[.<n>]]
#Requires -RunAsAdministrator
 ```
 
 More info on msdn [here](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_requires?view=powershell-7)