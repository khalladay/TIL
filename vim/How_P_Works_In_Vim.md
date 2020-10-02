# How 'p' works in vim

So 'p' obviously pastes in vim, and by default it pastes the content of the volatile register (or whatever register you specify), but where the pasted text goes can feel a little unpredictable at times. This is because the behaviour of 'p' is dependent on how the text in the register being pasted from was acquired. 

Commands in vim can operate in char-wise, line-wise or block-wise fashion. Even yanking text. 

* If the text being pasted was acquired from a char-wise operation (like 'y'), then it's pasted after the cursor (or before the cursor if using 'P').

* If the text was acquired from a line wise operation (like dd or yy), then the text will be inserted into the next line after the cursor 

* If the text was acquired from a block wise operation, (like v$y), then it's pasted immediately after the curson
