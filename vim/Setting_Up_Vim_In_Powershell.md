# Setting Up Vim In Powershell

I don't know what the default powershell text editor is (if there is one), but installing vim in a way that makes it accessible from powershell is easy (at least, on Windows 10). There's a module that you can install called PSReadLine, which allows you to "customize the command-line editing environment in PowerShell." It comes pre-installed on Win10. You can check if you have it with the following one liner.

```powershell
Get-Module -Name PSReadline -ListAvailable
```

If that shows your PSReadline version is 1.2 or later, you're good to go. If you need to install it, you can use the snippet below (which will also set up nuget if you haven't done that before):

```powershell
# Search for it
Find-Package -Name PSReadline

# install it with -Force to overwrite the older version if you have it
Install-Package -Name PSReadline -Force
```

Now to actually get Vim, use something like the following (adjusted for a newer version of vim if you want)

```powershell
Invoke-WebRequest -Uri https://ftp.nluug.nl/pub/vim/pc/gvim80-586.exe `
  -Outfile ~\Downloads\gvim80-586.exe
```

Then run the exe that is downloaded to get things setup. Then to finish off the setup (so that powershell actually lets you use vim), you need to add the following to your Powershell Profile: 

```powershell
# Add these lines to your $PROFILE
New-Alias -Name vi -Value 'C:\Program Files (x86)\vim\vim80\vim.exe'
New-Alias -Name vim -Value 'C:\Program Files (x86)\vim\vim80\vim.exe'

Set-PSReadlineOption -EditMode vi -BellStyle None
```

If after adding the above to your profile, you get errors when starting powershell sessions about being unable to load PS-Readline, you need to change your execution policy, with the following command (in an admin prompt)

```powershell
#Set policy to RemoteSigned (includes your own unsigned scripts)
Set-ExecutionPolicy RemoteSigned
```