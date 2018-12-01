#include <MsgBoxConstants.au3>
For $i = 1 To 10 Step + 1
    Run("C:\Python27\Python.exe " &  @ScriptDir & "\crack" & string($i) & ".py")
Next