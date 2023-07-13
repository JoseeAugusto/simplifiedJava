.class public programExample
.super java/lang/Object
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 300
bipush 0
istore 0
bipush 0
istore 1
ldc 0
istore 2
iload 2
istore 0
ldc 0
istore 3
iload 3
istore 1
enter_while0:
iload 0
istore 5
ldc 3
istore 6
iload 5
iload 6
if_icmplt true7
ldc 0
goto cmp_end7
true7:
ldc 1
cmp_end7:
istore 7
iload 0
istore 8
ldc 1
istore 9
iload 8
iload 9
iadd
istore 10
iload 10
istore 0
iload 0
istore 11
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 11
invokevirtual java/io/PrintStream/print(I)V
goto enter_while0
break0:
return
.end method
