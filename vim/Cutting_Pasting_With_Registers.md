# Cutting and Pasting With Vim Registers

By default, deleting anything in vim also copies it. This is really annoying when you want to delete some text and then paste in something else, since you'll end up just pasting back in what you copy. Luckily vim has better clipboard support than it initially seems. 

Vim's version of a clipboard is a series of "registers" which save text to them. By default, everything writes to the volatile default register, but yanking text also write the contents of that yank to a numbered register as well. Vim keeps 10 yank registers in memory, numbered 0 to 9. 0 is the most recently yanked thing, 9 is the oldest yanked thing in memory. 

You can paste from a yank register like so:

```
"0p
"1p
"2p
```
You can also explicitly paste or delete to the default register with ""p / ""d

Also, any command that would write to the default register can be redirected to write to a different register. For example, saving the contents of a delete to register 1:

```
"1d
```

There are other registers with specific uses as well. Maybe one day I'll need one of them too. 
