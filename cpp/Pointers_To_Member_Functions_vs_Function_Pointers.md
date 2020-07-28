# Pointers To Member Functions Are Different From Regular Function Pointers

C Style function pointers are super. They're just pointers. Pass them to VirtualProtect, cast them to uint64_t, do whatever you want. 

Pointers to member functions are a distinctly c++ thing, and as such, are a colossal pain in the ass. For starters, you can't convert them to anything, even C style casts will fail. 

The syntax for them is pretty sane, but that's about where it ends: 
```c
//get a pointer to the "getNum" function for type "Num"
int (Num::*ptrName)() = &Num::getNum;
```

There's no portable way to get an address from them (it's UB). That being said, you _can_ get an address from them in MSVC if you're willing to write some really dumb code: 

```c++
int (Num:: * memberPtr)() = &Num::getNum;
uint8_t** ptrptr = (uint8_t * *)(&memberPtr);
void* memberAddr = (void*)(*ptrptr);
```

This is especially interesting because MSVC appears to not store absolute addresses in member function pointers, rather, it stores an offset to that function from the base address of that type's layout in memory. 

Regardless, the above probably won't work outside of MSVC. 

You can't call a member function without an object instance (since member functions use the thiscall convention in x86... I'm not sure there's such a thing as thiscall in x64 on windows, but it still passes the object as the first arg on the stack, which makes things messy to try to do in C++ syntax). 

Of course, calling this function with an object instance is possible: 

```c
Num n;
(n.*ptrName)();
```


