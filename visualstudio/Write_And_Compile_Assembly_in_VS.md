# Writing Assembly in Visual Studio

To make a VS project support .asm files, go to Project->Build Customizations, and enable "masm." Once that's done, you should be able to add .asm files (just use the wizard to create a .cpp and specify the asm extension instead) that will compile into .o's for the project. 

If you want to create an asm only project, you'll also want to go into your project settings and change the Linker option "Entry Point" so that you can specify the name of your program's entry point, rather than have the linker look for crtmain. 

There's no syntax highlighting out of the box, but the VS extension ASMDude is pretty solid. 

Also - if you're doing this to get the hex bytes for assembly instructions, just set a breakpoint on whatever instruction you want the bytes for, debug to there, and switch to the Disassembly debug view. That view has an option (configurable at the top of the panel) to "Show Code Bytes", which is what you're after. 
