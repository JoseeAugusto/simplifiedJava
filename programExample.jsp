.class public programExample
.super java/lang/Object
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 300
bipush 5
istore 0
bipush 10
istore 1
iload 0
istore 2
iload 1
istore 3
iload 2
iload 3
if_icmpeq true4
ldc 0
goto cmp_end4
true4:
ldc 1
cmp_end4:
istore 4
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 4
invokevirtual java/io/PrintStream/print(Z)V
return
.end method
