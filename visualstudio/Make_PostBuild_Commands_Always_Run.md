# Making VS Always Run Post-Build Commands

I use post-build commands to copy content (like shaders/textures) to the build directory of projects I'm working on. I hate that usually vs only runs post-build commands when it detects that something has changed in the project, requiring me to add whitespace or something before it'll copy the latest version of my shader to the output dir. 

Forcing VS to always run post-build commands is a little weird, but it saves me a ton of headache. First, you need to open up the .vcxproj file for the specific project that you want to have always run a post-build command for (NOT the solution that contains all your sub projects) in a text editor. 

Next you need to look for an xml tag that's called <PostBuildEvent>. If you've already created a post-build event in the project, you should find it, along with your post-build commands: 

```xml
<PostBuildEvent>
      <Command>SET ERRORLEVEL=0
rmdir /s /q $(OutDir)..\hook_content
rm $(OutDir)..\$(TargetName).dll
robocopy  $(SolutionDir)dxgi_proxy_dll\hook_content $(OutDir)..\hook_content
copy $(OutDir)$(TargetName).dll  $(OutDir)..\$(TargetName).dll
rmdir /s /q $(OutDir)</Command>
</PostBuildEvent>
```

Add the following bit of xml inside the PostBuildEvent tags (honestly I'm not sure if this part is required or if it's just the next bit that does the trick. I could test it but it's working for me now so yolo): 
```xml
<RunPostBuildEvent>Always</RunPostBuildEvent>
```

Then, somewhere else in the file, add this: 


```xml
 <PropertyGroup>
    <DisableFastUpToDateCheck>true</DisableFastUpToDateCheck>
  </PropertyGroup>
```

Source: [https://stackoverflow.com/questions/28916414/visual-studio-add-pre-build-event-that-always-runs-c-project](https://stackoverflow.com/questions/28916414/visual-studio-add-pre-build-event-that-always-runs-c-project)

Note: this appears to also work for prebuild events: [https://stackoverflow.com/questions/28916414/visual-studio-add-pre-build-event-that-always-runs-c-project](https://stackoverflow.com/questions/28916414/visual-studio-add-pre-build-event-that-always-runs-c-project)