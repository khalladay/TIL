# Disabling Exceptions in a C++ Project

If you just set the project settings to disable exceptions, you can wind up with the error message

```xml
 warning C4530: C++ exception handler used, but unwind semantics are not enabled. Specify /EHsc
```

This comes from stl files that contain try/catch statements. If you want to silence the error (and make your executable smaller in the process), you also need to set the following preprocessor define for your project: 

```xml
_HAS_EXCEPTIONS=0
```
