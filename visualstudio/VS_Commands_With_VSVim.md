# Execute Visual Studio Commands With VsVim

Any command that you can assign a key combination to in Visual Studio can be assigned a corresponding command for it in VsVim. 

This is especially helpful for things like ctrl-K + ctrl-O (which toggles between header/implementation files), which doesn't appear to work with VsVim enabled. 

You can add a VS command to your vimrc file like this: 

```
:nnoremap ko :vsc EditorContextMenu.CodeWindow.ToggleHeaderCodeFile<CR>
```

It's important to always end the command with <CR>, otherwise VS won't recognize the command. 

You can figure out the name of the command you want by looking at the Tools->Options->Environment->Keyboard menu in Visual studio
