# Home Space In Stack Memory

It's common in windows assembly code to see lines like this: 

```x64
mov [rsp+8], rcx
```

This instruction moves the rcx register (the first of four arguments that can be passed in registers in the windows x64 calling convention) into "home space" (aka "shadow space"). According to the calling convention, callers MUST allocate 32 bytes of stack space to be used as home space before executing a _call_ instruction. Function prologues _may_ copy the values of the 4 argument registers into this shadow space. From what I can tell, this is mostly to aid in debugging, so that you can see the arguments passed to a function even if you break after that function has clobbered the register the arg was originally in. 

In optimized builds, it seems like the shadow space is used as scratch memory, rather than for storing copies of argument register data. 

