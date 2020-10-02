# String Substitution In Vim

Doing a "find and replace" operation on a line or block in vim uses sed style syntax: s/before/after

If you want to perform a string substitution on the first occurrence of a string in a line: 

```
:s/target/replacement
```

Performing that same subsittution on all occurrences of the target string in the line: 

```
:s/target/replacement/g
```

Performing that same action on all occurrences of the target string in the current selected block: 

```
:'<,'>s/\%Vtarget/replacement/g
```

The above looks cumbersome, but the opening '<,'> is added automatically by vsvim, so really the only typing difference is adding \%V to operate on the current block. Without that, the substitution can occur outside the bounds of the block, depending on cursor position.

You can google this and get a super detailed answer of course, with lots of options, but I haven't had to use those options yet.
