# Implicit Vulkan Layers

In addition to layers that are specified in code to be loaded by a vulkan application (aka "Explicit Layers"), Vulkan also supports "Implicit Layers", which are layers that will be loaded when any vulkan application is launched on a target machine. 

This can cause problems if something installs an implicit layer incorrectly, or installs a malicious implicit layer. For services like Steam and EGS, the in game overlays provided by those services are installed on the host system as implicit layers. 

On Windows, installing an implicit layer means adding a registry key to one of the following paths: 

```
HKEY_CURRENT_USER\Software\Khronos\Vulkan\ImplicitLayers
HKEY_LOCAL_MACHINE\Software\Khronos\Vulkan\ImplicitLayers
```

An installed implicit layer will add a value to one of these registry paths with the form 

| KEY | VALUE|
|-----|------|
| Path to json file | 0 | 

If the value is anything except a 0 DWORD, the implicit layer will not be loaded. If it _is_ 0, the vulkan application will look for a json file located at the path specified in the key, and use the information in that json file to load the layer.
