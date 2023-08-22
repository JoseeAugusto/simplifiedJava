.class public code
.super java/lang/Object
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 300
bipush 5
istore 0
ldc 10.0
fstore 1
ldc 50.0
fstore 2
ldc "oi"
astore 3
iload 0
istore 4
fload 1
fstore 5
fload 2
fstore 6
fload 5
fload 6
fdiv
fstore 7
iload 4
i2f
fstore 4
fload 4
fload 7
fadd
fstore 8
getstatic java/lang/System/out Ljava/io/PrintStream;
fload 8
invokevirtual java/io/PrintStream/print(F)V
ldc "\n"
astore 9
aload 3
astore 10
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 9
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 10
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
return
.end method
