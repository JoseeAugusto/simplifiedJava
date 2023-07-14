.class public ex3
.super java/lang/Object
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 300
ldc 0.0
fstore 0
ldc 0.0
fstore 1
bipush 0
istore 2
ldc 10.0
fstore 3
fload 3
fstore 0
ldc 5.0
fstore 4
fload 4
fstore 1
fload 0
fstore 5
fload 1
fstore 6
fload 5
fload 6
ifgt true7
ldc 0
goto cmp_end7
true7:
ldc 1
cmp_end7:
istore 7
iload 7
istore 2
iload 2
istore 8
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 8
invokevirtual java/io/PrintStream/print(Z)V
return
.end method
