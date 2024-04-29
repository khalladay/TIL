# Executing Batch Files in VS Postbuild Commands

If you want to run a batch file in a VS postbuild command, make sure to run it with the "call" function, and not just by it's path directly, otherwise the post build script will terminate when the first batch file you call is done, ignoring the rest of the postbuild script. 

Bad (second script never runs):
```
"$(ProjectDir)game_postbuild_tasks.bat" $(OutDir)content $(ProjectDir)content $(SolutionDir) $(OutDir)
"$(SolutionDir)engine_postbuild_tasks.bat" $(OutDir)content $(SolutionDir)engine_content $(SolutionDir) $(OutDir)
```


Good: 
```
call "$(ProjectDir)game_postbuild_tasks.bat" $(OutDir)content $(ProjectDir)content $(SolutionDir) $(OutDir)
call "$(SolutionDir)engine_postbuild_tasks.bat" $(OutDir)content $(SolutionDir)engine_content $(SolutionDir) $(OutDir)
```
