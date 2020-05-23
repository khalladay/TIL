# Speeding Up Searches With Memchr()

When I was working on render-with-notepad, I had a case where I needed to search a buffer for all instances of a byte pattern. I when about it the super naiive way: 

```c
char* FindPattern(char* src, size_t srcLen, char* pattern, size_t patternLen)
{
  char* cur = src;
  size_t curPos = 0;

  while (curPos < srcLen)
  {
    if (memcmp(cur,pattern,patternLen) == 0)
    {
      return cur;
    }

    curPos++;
    cur = &src[curPos];
  }
  return nullptr;
}
```

This did the job, but is excessively slow (since it searches for the byte pattern starting at every possible address). To speed this (and things like it up), you can use memchr(), which searches a buffer for the first instance of a byte and returns a pointer to it. In the case above, I could greatly speed things up by searching for the first instance of the first byte of the pattern, and only memcmping after the first byte was found. 

```c
void* memchr(void* ptr, int value, size_t num);
const void* memchr(const void* ptr, int value, size_t num);

//ptr is a pointer to the block of memory to search
//value is the value to be located, treated as an unsigned int internally
//num is the number of bytes to be analyzed
```
