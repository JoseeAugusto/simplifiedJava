.class public ex
.super java/lang/Object
.method public static fat(I)I
.limit stack 5
.limit locals 300
iload 0
istore 2
ldc 1
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
iload 4
ldc 0
if_icmpeq if_0
iload 0
istore 5
iload 5
ireturn
goto end_else_0
if_0:
iload 0
istore 6
iload 0
istore 7
ldc 1
istore 8
iload 7
iload 8
isub
istore 9
iload 9
invokestatic ex.fat(I)I
istore 0
iload 6
iload 0
imul
istore 10
iload 10
ireturn
end_else_0:
return
.end method
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 300
ldc 6
istore 11
iload 11
invokestatic ex.fat(I)I
istore 0
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 0
invokevirtual java/io/PrintStream/print(I)V
return
.end method
