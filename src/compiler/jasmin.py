from error import ErrorVariableNotFoundAtSymbolTable

class Jasmin:
    MAX_LOCALS = 300

    def __init__(self, filename, symbolTable):
        self.fileName = filename
        self.file = open(filename + '.jsp', 'w+')
        self.initFile()
        self.symbolTable = symbolTable

        self.top_index = 0
        self.label_count = 0

    def __write(self, string):
        for s in string.split('\n'):
            if s.strip():
                self.file.write(s.strip() + "\n")

    def initFile(self):
        self.__write(
            """
            .class public {}
            .super java/lang/Object
            """.format(self.fileName)
        )

    def getVar(self, varName, scopeController):
        if self.symbolTable[varName]:
            variable = self.symbolTable[varName]
        else:
            raise ErrorVariableNotFoundAtSymbolTable(varName, scopeController)

        return variable

    def create(self, varName, varType, scopeControl, const: False, val: 0):
        variable = self.getVar(varName, scopeControl)
        if varType == 'bool' and val == 'True':
            val = 1
        elif varType == 'bool' and val == 'False':
            val = 0
        elif varType == 'float' and val == 0:
            val = 0.0
        elif varType == 'str' and val == 0:
            val = "\"\""
        if variable.type == 'int' or variable.type == 'bool':
            self.__write(
                """
                bipush {}
                istore {}
                """.format(val, variable.address)
            )
        elif variable.type == 'float':
            self.__write(
                """
                ldc {}
                fstore {}
                """.format(val, variable.address)
            )
        elif variable.type == 'str':
            self.__write(
                """
                ldc {}
                astore {}
                """.format(val, variable.address)
            )
  
    def createMain(self):
        self.__write(
            """
            .method public static main([Ljava/lang/String;)V
            .limit stack 10
            .limit locals {}
            """.format(self.MAX_LOCALS)
        )

    def createFunction(self, name, parameters):
        param = ''
        for p in parameters:
            param += typeConvert(self.symbolTable[p].type)

        self.__write(
            """
            .method public static {}({}){}
            .limit stack 5
            .limit locals {}
            """.format(name, param, typeConvert(self.symbolTable[name].type), self.MAX_LOCALS)
        )
        for idx, p in enumerate(parameters):
            self.symbolTable[p].address = idx

    def closeFunction(self):
        self.__write(
            """
            return
            .end method
            """
        )

    def createReturnCommand(self, val, type):
        returnType = typeConvert(type)
        if (returnType == 'V'):
            self.__write(
                """
                return
                """
            )
            return

        self.loadTemp(val, type)
        if returnType == 'I' or returnType == 'Z':
            self.__write(
                """
                ireturn
                """
            )
        elif returnType == 'F':
            self.__write(
                """
                freturn
                """
            )
        elif returnType == 'V':
            self.__write(
                """
                return
                """
            )
        elif returnType == 'Ljava/lang/String;':
            self.__write(
                """
                areturn
                """
            )

    def createFunctionCall(self, func_name, params, types):
        variable = self.symbolTable[func_name]
        args = ''
        for p, t in zip(params, types):
            self.loadTemp(p, t)
            args += typeConvert(t)
        self.__write(
            """
            invokestatic {}.{}({}){}
            """.format(self.fileName, func_name, args, typeConvert(variable.type))
        )
        return self.storeVal(variable.type, variable.address)

    def createTemp(self, val, type, addr):
        self.__write(
            """
            ldc {}
            """.format(val)
        )
        return self.storeVal(type, addr)

    def storeVal(self, type, addr):
        if type == 'str':
            self.__write(
                """
                astore {}
                """.format(addr)
            )
        elif type == 'int' or type == 'bool':
            self.__write(
                """
                istore {}
                """.format(addr)
            )
        elif type == 'float':
            self.__write(
                """
                fstore {}
                """.format(addr)
            )
        return addr

    def loadTemp(self, val, type):
        if type == 'int' or type == 'bool':
            self.__write(
                """
                iload {}
                """.format(val)
            )
        elif type == 'float':
            self.__write(
                """
                fload {}
                """.format(val)
            )
        elif type == 'str':
            self.__write(
                """
                aload {}
                """.format(val)
            )

    def loadVar(self, var, scopeController, addr):
        varData = self.symbolTable[var]
        
        if varData.type == 'int' or varData.type == 'bool':
            self.__write(
                """
                    iload {}
                    """.format(varData.address)
            )
        elif varData.type == 'float':
            self.__write(
                """
                fload {}
                """.format(varData.address)
            )
        elif varData.type == 'str':
            self.__write(
                """
                aload {}
                """.format(varData.address)
            )
        return self.storeVal(varData.type, addr)

    def storeVar(self, var, val, address, scopeController):
        varData = self.getVar(var, scopeController)

        if varData.type == 'int' or varData.type == 'bool':
            self.__write(
                """
                iload {}
                istore {}
                """.format(val, address)
            )
        elif varData.type == 'float':
            self.__write(
                """
                fload {}
                fstore {}
                """.format(val, address)
            )
        elif varData.type == 'str':
            self.__write(
                """
                aload {}
                astore {}
                """.format(val, address)
            )

    def enterElse(self, index):
        self.__write(
            """
            goto end_else_{}
            if_{}:
            """.format(index, index)
        )

    def makeLabel(self, labelName):
        self.__write(
            """
            {}:
            """.format(labelName)
        )

    def print(self, typeVal):
        for type, val in typeVal:
            self.__write(
                """
                getstatic java/lang/System/out Ljava/io/PrintStream;
                """
            )
            self.loadTemp(val, type)
            self.__write(
                """
                invokevirtual java/io/PrintStream/print({})V
                """.format(typeConvert(type))
            )

    def scanf(self, var, controle_escopo):
        table = self.symbolTable[var]
        t = table.type

        self.__write(
            """
            new java/util/Scanner
            dup
            getstatic java/lang/System/in Ljava/io/InputStream;
            invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
            """
        )
        if t == 'str':
            self.__write(
                """
                invokevirtual java/util/Scanner/nextLine()Ljava/lang/String;
                """
            )
        elif t == 'int':
            self.__write(
                """
                invokevirtual java/util/Scanner/nextInt()I
                """.format(typeConvert(table.type))
            )
        elif t == 'float':
            self.__write(
                """
                invokevirtual java/util/Scanner/nextFloat()F
                """.format(typeConvert(table.type))
            )
        elif t == 'bool':
            self.__write(
                """
                invokevirtual java/util/Scanner/nextBoolean()Z
                """.format(typeConvert(table.type))
            )

        addr = self.storeVal(table.type, table.address)
        if not table.scope:
            self.storeVar(var, table.address, None, None)

    def enterIf(self, id):
        self.loadTemp(id, 'int')
        self.__write(
            """
            ldc 0
            if_icmpeq if_{}
            """.format(self.label_count, self.label_count)
        )
        self.label_count += 1
        return self.label_count - 1

    def initWhile(self, loop_idx):
        self.__write(
            """
            enter_while{}:
            """.format(loop_idx)
        )
        return "iload {}\n" + "ldc 1\nif_icmpne break{}".format(loop_idx)

    def exitWhile(self, loop_idx):
        self.__write(
            """
            goto enter_while{}
            break{}:
            """.format(loop_idx, loop_idx)
        )

    def breakWhile(self, loop_idx):
        self.__write(
            """
            goto break{}
            """.format(loop_idx)
        )

    def writeInh(self, line):
        self.__write(line)

    def add(self, type, addr1, addr2, addr3):
        self.loadTemp(addr1, type)
        self.loadTemp(addr2, type)
        if type == 'int':
            self.__write(
                """
                iadd
                """
            )
        elif type == 'float':
            self.__write(
                """
                fadd
                """
            )
        return self.storeVal(type, addr3)

    def sub(self, type, addr1, addr2, addr3):
        self.loadTemp(addr1, type)
        self.loadTemp(addr2, type)
        if type == 'int':
            self.__write(
                """
                isub
                """
            )
        elif type == 'float':
            self.__write(
                """
                fsub
                """
            )
        return self.storeVal(type, addr3)

    def mult(self, type, addr1, addr2, addr3):
        self.loadTemp(addr1, type)
        self.loadTemp(addr2, type)
        if type == 'int':
            self.__write(
                """
                imul
                """
            )
        elif type == 'float':
            self.__write(
                """
                fmul
                """
            )
        return self.storeVal(type, addr3)

    def div(self, type, addr1, addr2, addr3):
        self.loadTemp(addr1, type)
        self.loadTemp(addr2, type)
        if type == 'int':
            self.__write(
                """
                idiv
                """
            )
        elif type == 'float':
            self.__write(
                """
                fdiv
                """
            )
        return self.storeVal(type, addr3)

    def unaryMinus(self, type, addr1, addr3):
        self.loadTemp(addr1, type)
        if type == 'int':
            self.__write(
                """
                bipush -1
                imul
                """
            )
        elif type == 'float':
            self.__write(
                """
                ldc -1
                fmul
                """
            )
        return self.storeVal(type, addr3)

    def notOp(self, val, addr):
        self.loadTemp(val, 'bool')
        self.__write(
            """
            ldc 1
            ixor
            """
        )
        return self.storeVal('bool', addr)

    def compareExpressions(self, type, val1, val2, addr3, op):
        cmp = {'==': 'eq', '!=': 'ne', '>=': 'ge', '>': 'gt', '<=': 'le', '<': 'lt'}
        self.loadTemp(val1, type)
        self.loadTemp(val2, type)
        if type in ['int', 'bool']:
            self.__write(
                """
                if_icmp{} true{}
                """.format(cmp[op], addr3)
            )
        elif type == 'float':
            self.__write(
                """
                fcmpl
                if{} true{}
                """.format(cmp[op], addr3)
            )
        else:
            self.__write(
                """
                if_acmp{} true{}
                """.format(cmp[op], addr3)
            )
        self.__write(
            """
            ldc 0
            goto cmp_end{}
            true{}:
            ldc 1
            cmp_end{}:
            """.format(addr3, addr3, addr3, addr3)
        )
        return self.storeVal('bool', addr3)

    def intToFloat(self, addr):
        self.loadTemp(addr, "int")
        self.__write(
            """
            i2f
            """
        )
        return self.storeVal("float", addr)

    def closeMain(self):
        self.__write(
            """
            return
            .end method
            """
        )

class Id:
    def __init__(self, address: int = None, type=None, scope=None, isConstant: bool = False, isInitialized: bool = False, isFunction: bool = False):
        self.type = type
        self.scope = scope 
        self.address = address
        self.isConstant = isConstant
        self.isInitialized = isInitialized
        self.isFunction = isFunction

def typeConvert(type):
        descriptor = {'int': 'I', 'float': 'F', 'str': 'Ljava/lang/String;', 'bool': 'Z', None: 'V'}
        if type != 'int' and type != 'float' and type != 'str' and type != 'bool' and type != None:
            return descriptor[type.type]
        else:
            return descriptor[type]  

   