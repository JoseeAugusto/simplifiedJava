.class public ex
.super java/lang/Object
.method public static soma()I
.limit stack 5
.limit locals 300
bipush 0
istore 1
ldc 3
istore 2
iload 2
istore 1
iload 1
istore 3
iload 1
istore 4
iload 3
iload 4
iadd
istore 5
iload 5
ireturn
return
.end method
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 300
invokestatic ex.soma()I
istore 0
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 0
invokevirtual java/io/PrintStream/print(I)V
ldc 10
istore 6
