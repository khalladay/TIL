# Zeroing a Register

There's a ton of ways to do this, but only one _best_ way.

You'd think it would be 

```asm
mov eax,0
```

Which is very fast (1 instruction per cycle), but is 5 bytes long. Honestly this is probably good enough for almost all cases, but there's a smaller (so less i-cache misses) and faster (due to CPU trickery) option. Instead of the above, you should instead use:

```asm
xor eax,eax
```

Which is smaller (2 bytes), and can execute at a rate of 4 instructions per cycle due to CPU trickery. Modern x86/x64 CPUs also have special case handling for xor-ing a register with itself so that it doesn't introduce a data dependency with other instructions that use the register. This all still works if you use 64 bit registers.

More info here: https://randomascii.wordpress.com/2012/12/29/the-surprising-subtleties-of-zeroing-a-register/
