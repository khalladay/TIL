# Macros for Project Directories

These are pulled straight from the MS Documentation [here](https://docs.microsoft.com/en-us/cpp/build/reference/common-macros-for-build-commands-and-properties?view=msvc-160), but I had never seen that page before, so now that I found it, I'm reproducing it here. 

|Macro	| Description |
|-------|--------------|
|$(Configuration) |	The name of the current project configuration, for example, "Debug". |
|$(DevEnvDir) |	The installation directory of Visual Studio (defined as drive + path); includes the trailing backslash '\'. |
|$(FrameworkDir)	| The directory into which the .NET Framework was installed. |
|$(FrameworkSDKDir)	| The directory into which you installed the .NET Framework. The .NET Framework could have been installed as part of Visual Studio or separately. |
|$(FrameworkVersion)	| The version of the .NET Framework used by Visual Studio. Combined with $(FrameworkDir), the full path to the version of the .NET Framework use by Visual Studio. |
|$(OutDir)	| Path to the output file directory. If it's a relative path, output files go to this path appended to the project directory. This path should have a trailing slash. It resolves to the value for the Output Directory property. Don't use $(IntDir) to define this property. |
|$(Platform)	 | The name of current project platform, for example, "Win32". |
|$(PlatformShortName)	| The short name of current architecture, for example, "x86" or "x64". |
|$(ProjectDir) |	The directory of the project (defined as drive + path); includes the trailing backslash '\'. |
|$(ProjectExt) |	The file extension of the project. It includes the '.' before the file extension. |
|$(ProjectFileName)	| The file name of the project (defined as base name + file extension). |
|$(ProjectName) |	The base name of the project. |
|$(ProjectPath) |	The absolute path name of the project (defined as drive + path + base name + file extension). |
|$(SolutionDir) |	The directory of the solution (defined as drive + path); includes the trailing backslash '\'. Defined only when building a solution in the IDE. |
|$(SolutionExt) |	The file extension of the solution. It includes the '.' before the file extension. Defined only when building a solution in the IDE. |
|$(SolutionFileName)	| The file name of the solution (defined as base name + file extension). Defined only when building a solution in the IDE. |
|$(SolutionName)	 | The base name of the solution. Defined only when building a solution in the IDE. |
|$(SolutionPath) |	The absolute path name of the solution (defined as drive + path + base name + file extension). Defined only when building a solution in the IDE. |
|$(TargetDir) |	The directory of the primary output file for the build (defined as drive + path); includes the trailing backslash '\'. |
|$(TargetExt) |	The file extension of the primary output file for the build. It includes the '.' before the file extension. |
|$(TargetFileName) | 	The file name of the primary output file for the build (defined as base name + file extension). |
|$(TargetName) |	The base name of the primary output file for the build. |
|$(TargetPath) |	The absolute path name of the primary output file for the build (defined as drive + path + base name + file extension). |
|$(VSInstallDir)	| The directory into which you installed Visual Studio. This property contains the version of the targeted Visual Studio toolset, which might be different that the host Visual Studio. For example, when building with $(PlatformToolset) = v110, $(VSInstallDir) contains the path to the Visual Studio 2012 installation. |
