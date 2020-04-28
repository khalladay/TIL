# Vim Plugins

You can see loaded plugins using 

```vim
:scriptnames
```
Vim 8.0 added it's own package management, so the only thing you need to do is clone a package repository and put it in 

```vim
~/.vim/pack/<any string>/start/
```

I've set it up so all my plugins are stored in a separate folder, as submodules of a vim_setup repo that I keep separate from a given system's active config. That folder contains a batch script (and shell script) for copying the plugin files and the vimrc to the right spot depending on platform. 

That way to upadte my plugins I just need to update all the submodules of that repo. 
