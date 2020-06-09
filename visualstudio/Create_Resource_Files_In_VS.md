# Creating Resource (RC) Files In Visual Studio

Creating Win32 GUI applications requires the use of Resource (or .rc) files to package up gui relevant resources, like icon files and string tables.

Creating these rc files can be done on the command line using the "RC" command line tool (accessible via the Developer Command Prompt), but you can also create these files directly inside Visual Studio.

Just create a "Resource" file in your project. Then double click on it to go to the "Resource View" in Visual Studio. From there, you can add or create resources that should be included with your project. Visual Studio will handle writing the .rc script and generating the resources.h header file for you. You simply need to include the generated resources.h and start using it.

Note that if you're creating menus or dialogs, the "properties" editor menu, which is what lets you actually change GUI elements in the editor, may be hidden by default. 
