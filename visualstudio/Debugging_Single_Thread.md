# Debugging a Single Thread In Visual Studio Code

Sometimes it's handy to be able to only run a single thread at a time while debugging a multithreaded application (ie: I want to break every time memory is allocated by code on thread X). To do this, at least in a limited way, you can "freeze" the threads you don't care about while a program is running and let the one thread that you want to debug continue to work.

 To do this, pause the program that you're debugging (or break at a breakpoint), and switch to the "Threads" window (ctrl+alt+h). Select all threads (ctrl-a) and then find the thread that you want to debug and ctrl+click on that to deselect it. 

 Then right click on the still selected bunch of threads and choose "Freeze." Now you can continue running the application and have only the thread you care about continue to execute. Hurray!
