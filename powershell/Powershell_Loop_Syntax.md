# Powershell Loop Syntax

Powershell loop syntax is pretty similar to .NET language loop syntax (or C-like loops in general). As a rule, continue; and break; statements work how you'd expect in all loop types.


## For Loops
For Loops are pretty much what you'd expect. The only wrinkle is that powershell uses weird comparison operators

| Operator | C Equivalent |
|----------|--------------|
| -eq | == | 
| -ne | != |
| -gt | > |
| -lt | < | 
| -le | <= |
| -ge | >= |

```powershell
for ($i = 0; $i -lt 3; $i++)
{
}
```

## For-Each Loops

For Each loops can take a few different forms in Powershell, but the simplest looks like this:

```powershell
foreach($placehold_var in $collection)
{
  
}
```

There's also the Foreach-Object commandlet (which confusingly uses '%' as an alias)

```powershell
# assuem you have an array
$d = $a,$b,$c

# write each one to the console
$d | ForEach-Object { Write-Host $_ } 

#also possible
$d | % { Write-Host $_}
```

## While Loops
Exactly what you'd expect, given the above

```powershell
$i = 0
while ($i -lt 5)
{
}
```

