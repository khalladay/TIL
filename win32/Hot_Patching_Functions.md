# Hot Patching

Some windows dlls (like Kernel32) have been built with "hot patching" enabled. This means that every function in that dll starts with a useless Mov EDI,EDI instruction and is immediately preceeded by 5 bytes of nop instructions. 

The idea here is that if you want to hook (or "hot patch") any of these functions, you can override the MOV EDI,EDI with a 2 byte jump backwards (to the beginning of the nops), and then fill in the 5 bytes of nop with a 5 byte E9 relative jump to wherever you want to go. 

You can create your own hotpatchable binaries in visual studio with with the /hotpatch and /functionpadmin options, specified in 

```
Properties->C/C++->Command Line-> "Additional Options"
```

The /hotpatch option only matters for x86. For ARM or x64, you need /functionpadmin (at least, according to msdn) 

More info: blog.nettitude.com/uk/windows-inline-function-hooking
