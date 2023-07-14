.class public ex2
.super java/lang/Object
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 300
ldc 5
istore 0
ldc 2
istore 1
iload 0
iload 1
if_icmpgt true2
ldc 0
goto cmp_end2
true2:
ldc 1
cmp_end2:
istore 2
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 2
invokevirtual java/io/PrintStream/print(Z)V
return
.end method
