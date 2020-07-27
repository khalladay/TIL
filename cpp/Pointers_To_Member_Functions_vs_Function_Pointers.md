# Pointers To Member Functions Are Different From Regular Function Pointers

C Style function pointers are super. They're just pointers. Pass them to VirtualProtect, cast them to uint64_t, do whatever you want. 

Pointers to member functions are a distinctly c++ thing, and as such, are a colossal pain in the ass. For starters, you can't convert them to anything, even C style casts will fail. You also can't get an actual address from them, since they aren't guaranteed to store an absolute address (msvc seems to have them store an offset to the function within the type's layout, it doesn't seem possible to get the base address of this type layout programmatically, although you might be able to search the process' address space for it?).  

The syntax for them is pretty sane: 
```c
//get a pointer to the "getNum" function for type "Num"
int (Num::*ptrName)() = &Num::getNum;
```

You can't call a member function without an object instance (since member functions use the thiscall convention in x86... I'm not sure there's such a thing as thiscall in x64 on windows, but it still passes the object as the first arg on the stack, which makes things messy to try to do in C++ syntax). 

Of course, calling this function with an object instance is possible: 

```c
Num n;
(n.*ptrName)();
```


