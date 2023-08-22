.class public code
.super java/lang/Object
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 300
bipush 0
istore 0
ldc 5
istore 1
ldc 4
istore 2
iload 1
iload 2
if_icmpgt true3
ldc 0
goto cmp_end3
true3:
ldc 1
cmp_end3:
istore 3
iload 3
istore 0
iload 0
istore 4
iload 4
ldc 0
if_icmpeq if_0
iload 0
istore 5
iload 5
ldc 0
if_icmpeq if_1
ldc "entrei aqui\n"
astore 6
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 6
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
if_1:
iload 0
istore 7
iload 7
ldc 1
ixor
istore 8
iload 8
ldc 0
if_icmpeq if_2
ldc "entrei aqui 2\n"
astore 9
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 9
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
goto end_else_2
if_2:
ldc "falhou\n"
astore 10
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 10
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
end_else_2:
goto end_else_0
if_0:
end_else_0:
ldc 0
istore 11
iload 11
ldc 0
if_icmpeq if_3
goto end_else_3
if_3:
ldc "entrei nesse else"
astore 12
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 12
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
end_else_3:
return
.end method
