# Manually Setting a DLL's Base Address

On modern Windows versions, a DLL's preferred base address is pretty much totally ignored because of ASLR. However, it _is_ possible to create a DLL that loads in at a specific address. 

First, you need to disable ASLR in the linker settings for that dll (via the "Dynamic Base" linker option. 

Next, you need to set the Base address (also a linker option), to the address that you want to load the dll into. Remember that for a 64 bit process, the virtual memory range is 0 - 0x7FFFFFFFFFFF, so don't set an address higher than this.

Even with a preferred base address set and ASLR disabled, there's still no guarantee that you'll end up loading the DLL at that address unless you also enable the "Fixed Base Address" linker setting, which will cause the DLL to fail to load if it can't be loaded at it's preferred base.

If you've set your DLL's base address to a value outside the range of a 32 bit exe ( 0 - 0x7FFFFFFF ), the EXE loading the dll needs to enable the linker setting "Enable Large Addresses."

Finally, note that a DLL's base address must be a multiple of 64k, or else the Linker will error out.
