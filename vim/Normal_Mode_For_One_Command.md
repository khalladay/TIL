# Switch To Normal Mode For One Command

While in Insert Mode, it's pretty common to want to execute  a single normal mode command for navigation reasons (like '$' to jump to the end of a line).
The command for that is <C-o>, which is the vim nomenclature way of saying "ctrl + o" 

If you, for example, want to add a command to insert mode to jump you to the end of a line, you'd add the following to your vimrc: 

```vim
#Adds "ctrl+e" as an insert mode shortcut to jump to the end of the line
inoremap <C-e> <C-o>$
```