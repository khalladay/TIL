# Have Robocopy Copy a Directory Recursively

Usually this comes up when writing post build events in VS to copy content folders to build directories, but whatever. Let's say you have the following robocopy command:

```xml
robocopy  $(SolutionDir)..\content $(OutDir)content
```

but you want it to also copy all subdirectories of the content folder recursively. Add the /E argument

```xml
robocopy  $(SolutionDir)..\content $(OutDir)content /E
```