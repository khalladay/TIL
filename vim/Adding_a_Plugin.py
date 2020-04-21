# Vim Plugins

You can see loaded plugins using 

```vim
:scriptnames
```

The canonical way to add a vim plugin manually appears to be to place the file inside one of the following two directories, depending on platform: 

```vim
~/.vim/pack
~/vimfiles/pack #windows 
```

That didn't work for me though. On my install (and maybe I installed vim weirdly?), my vimfiles folder was located in 

```vim
C:\Program Files (x86)\Vim\vimfiles
```

So it's worth checking out your :scriptnames output to see where things live. Placing my desired plugin in the above folder caused vim to load my plugin on start. 

