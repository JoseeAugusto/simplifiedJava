.class public ex
.super java/lang/Object
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 300
ldc 0.0
fstore 0
ldc 0.0
fstore 1
ldc 10.0
fstore 2
fload 2
fstore 0
ldc 5.0
fstore 3
fload 3
fstore 1
fload 0
fstore 4
fload 1
fstore 5
fload 4
fload 5
fadd
fstore 6
ldc 2
istore 7
iload 7
i2f
fstore 7
fload 6
fload 7
fdiv
fstore 8
ldc 7.0
fstore 9
fload 8
fload 9
fcmpl
ifge true10
ldc 0
goto cmp_end10
true10:
ldc 1
cmp_end10:
istore 10
iload 10
ldc 0
if_icmpeq if_0
ldc "aprovado\n"
astore 11
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 11
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
goto end_else_0
if_0:
ldc "reprovado\n"
astore 12
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 12
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
end_else_0:
return
.end method
