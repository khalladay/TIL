# Setting Sleep Resolution

I was using Sleep to artificially limit frame rate in a project to make some temporal artifacts more noticeable. 

```c++
float targetFrameTime = floorf(1000 / (float)MaxFps);
if (deltaT < targetFrameTime)
{
    Sleep(targetFrameTime - deltaT);
}
```

This worked great if I wanted my MaxFps to be 60, but no matter what I set MaxFps to, I always got roughly 60 fps (actually a little bit slower).  

Turns out that by default Sleep on windows has a resolution of about 16 ms. To change it, you need to call [timeBeginPeriod](https://docs.microsoft.com/en-us/windows/win32/api/timeapi/nf-timeapi-timebeginperiod) to change the resolution of "periodic" timers. The high performance timer isn't affected by this function call. 

Fixing the frame rate limiter so it actually did what I wanted it to do looked like this: 

```c++
float targetFrameTime = floorf(1000 / (float)MaxFps);
if (deltaT < targetFrameTime)
{
    timeBeginPeriod(1);
    Sleep(targetFrameTime - deltaT);
    timeEndPeriod(1);
}
```