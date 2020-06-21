# Disabling ASLR (Project Wide or System Wide) 

ASLR is great, until you need to set up a specific test case or try out something funky and it actively fights against you. 

If you need to disable ASLR for a single MSVC project, use the /DYNAMICBASE[:NO] linker option (Linker->Advanced->Randomized Base Address)

If for some reason you want to disable it system-wide (not a good idea, but I'm including it here because it was in the same SO post as the linker option), use the registry key below: 

```
HKLM\SYSTEM\CurrentlControlSet\Control\Session Manager\Memory Management\MoveImages
```
