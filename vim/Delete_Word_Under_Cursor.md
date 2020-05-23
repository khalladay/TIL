# Deleting A Word Under The Cursor

There are a few different ways to delete a word under your cursor. 

If you're in insert mode, you have a lot of options

| Command | Effect | 
|--------|---------|
| dw     | Deletes from cursor to end of word (including trailing space) |
| daw    | Deletes entire word under cursor (including trailing space) |
| diw    | Deletes entire word under cursor (leaves whitespace alone) | 

You can also use bdw for "go to beginning of word, then dw" as a substitute for daw. 

If you want to end up in insert mode after the removal (which is likely): 

| Command | Effect | 
|---------|--------|
| cw | dw but you end up in insert mode
| caw | daw but you're in insert mode |
| ciw | you get the idea

If you're in edit mode, you likely just want to ctrl-c to go to insert mode for one command (if you're in VsVim and you've left ctrl-c / ctrl-v alone like I have, get creative with vimrc). 

In visual mode, just select what you want and press d to delete it. Or press c to delete it and end up in insert mode
