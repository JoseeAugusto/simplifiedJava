.class public programExample
.super java/lang/Object
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 300
ldc 5
istore 0
ldc 5
istore 1
iload 0
iload 1
iadd
istore 2
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 2
invokevirtual java/io/PrintStream/print(I)V
return
.end method
