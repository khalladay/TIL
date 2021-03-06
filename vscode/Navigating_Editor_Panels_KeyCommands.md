# Navigating Editor Panels With Key Commands In VSCode

When running with vs-vim, it's helpful to be able to snap focus to different panels in the editor (like search, or console), and then back to your actual content panels without needing to use a mouse. The commands for navigating to various non-content windows are listed in the editor: 

* Search in files - ctrl+shift+f
* Terminal - ctrl + `
* Console - ctrl + shift + y
* Output - ctrl + shift + u 

Not immediately visible in the menus is the shortcut to return to content: 

* Return to panel - ctrl + [panel number]

For example, if you had a split layout with 2 panels split vertically, ctrl+1 would jump to the left panel, and ctrl+2 would jump to the rightmost one (or create it, if one doesn't exist)