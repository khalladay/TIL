# Jumping To EOL and Entering Insert Mode 

One major frustration I had with vim was that $i would jump me to the end of a line, but then enter insert mode with the cursor in front of the last character. I had somehow missed the fact that "a" command is supposed to be used when you want to enter insert mode after the currently highlighted char. 

| Command | Action | 
|---------|--------|
| a | Enter insert mode after the currently highlighted character | 
| $a | jump to the end of the line and enter insert mode | 
| A | the same as $a | 

