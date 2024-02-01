# Setting up a PCH

1. In your project settings, go to C/C++ -> Precompiled Headers and set the "Precompiled Header" option to "Use /Yu"
2. Enter the name that you want your precompiled header file to have
3. Set your output file location
4. In your solution, create a .h and a .cpp using the precompiled header file name (ie: pch.h / pch.cpp)
5. In the header, add all the includes you want your precompiled header to contain
6. In the cpp file, add a single line, including the header. 
7. Go to the properties for the .cpp file and change the precompiled header settings for that file only to "Create (/Yc)"