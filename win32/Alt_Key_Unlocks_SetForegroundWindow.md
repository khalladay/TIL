# Alt Key Bypasses Foreground Lock

Microsoft really hates the idea of windows stealing focus. Raymond Chen even has a blog post about it somewhere, and the OS goes out of it's way to make it hard for one program to change the window that has current focus. 

There's a trick out there about calling AttachThreadInput and attaching to the currently open foreground window, yadda yadda. It's hacky and has issues (like both threads stopping responding if the attached to one does). There's an easier way. 

Windows has the function SetForegroundWindow, but for this most part this doesn't do much because of the os "foreground lock," which explicitly prevents this function from actually doing what it says it will. There are very specific ways to disable this lock, but the easiest is to press the alt key (or pretend you're pressing it in code). 

More info here: https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setforegroundwindow

