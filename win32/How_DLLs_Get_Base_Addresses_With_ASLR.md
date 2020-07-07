# How Do DLLs Get Assigned Base Addresses When ASLR Is Enabled? 

Raymond Chen has an article about this ([link](https://devblogs.microsoft.com/oldnewthing/20160413-00/?p=93301)). 

Essentially, whenever a DLL is loaded into memory the first time, ASLR will pick a random base address for it to load into. As long as it stays in memory, that chosen address with be the base address for all processes that load that dll (unless there's a conflict and it needs to be relocated in a different process).

Essentially, if you know the base address of a dll in one process, you know it for all processes (within a margin of error). 

This means you can do stupid stuff like get the address that a dll was loaded at in a remote process by just loading it in your own process while the target process is running. 

Note that DLL base addresses must be multiples of 64k. 

Also note that DLLs get loaded into the same base address to facilitate sharing of memory. Basically everything in a DLL is copy-on-write, so unless you modify something (data, or codepage), your process doesn't have to allocate memory to duplicate that dll. 

