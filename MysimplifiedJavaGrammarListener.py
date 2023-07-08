# Generated from C:/Users/jose1/Documents/UFPI/6� per�odo/Compiladores/trabFinal/javaSimplificado\simplifiedJavaGrammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from gen.simplifiedJavaGrammarParser import simplifiedJavaGrammarParser
else:
    from gen.simplifiedJavaGrammarParser import simplifiedJavaGrammarParser
from jasmin import Jasmin, Id
from error import ErroTipoIncompativelDecl, ErroTipoInesperado, ErrorTypeNotReported, ErroBreak, ErrorDeclarationAlreadyMade, \
    ErrorVariableNotDeclared, ErrorTypeExpression, ErroTipoExpressaoDiferenteDeIncremento, ErroRetorno, \
    ErroDuplaExpressao, ErroArgumentoEsperado, ErroDeclaracaoDepoisDoBloco


# This class defines a complete listener for a parse tree produced by simplifiedJavaGrammarParser.
class MySimplifiedJavaGrammarListener(ParseTreeListener):
    symbolTable = {}
    symbolTableCopy = {}
    scopeController = False
    stackBlock = []
    newAddressController = 0

    def __init__(self, filename):
        self.jasmin = Jasmin(filename, self.symbolTable)
        self.label_id = 0

    # Enter a parse tree produced by simplifiedJavaGrammarParser#program.
    def enterProgram(self, ctx:simplifiedJavaGrammarParser.ProgramContext):
        print("Initializing semantic analisis")
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#program.
    def exitProgram(self, ctx:simplifiedJavaGrammarParser.ProgramContext):
        print("Exiting semantic analisis")
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#functionDeclarationArea.
    def enterFunctionDeclarationArea(self, ctx:simplifiedJavaGrammarParser.FunctionDeclarationAreaContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#functionDeclarationArea.
    def exitFunctionDeclarationArea(self, ctx:simplifiedJavaGrammarParser.FunctionDeclarationAreaContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#main.
    def enterMain(self, ctx:simplifiedJavaGrammarParser.MainContext):
        self.jasmin.createMain()
        self.scopeController = True
        self.stackBlock.append('function')
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#main.
    def exitMain(self, ctx:simplifiedJavaGrammarParser.MainContext):
        self.jasmin.closeMain()
        self.scopeController = False
        self.stackBlock.pop()
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#variablesDeclarationArea.
    def enterVariablesDeclarationArea(self, ctx:simplifiedJavaGrammarParser.VariablesDeclarationAreaContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#variablesDeclarationArea.
    def exitVariablesDeclarationArea(self, ctx:simplifiedJavaGrammarParser.VariablesDeclarationAreaContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#variablesDeclaration.
    def enterVariablesDeclaration(self, ctx:simplifiedJavaGrammarParser.VariablesDeclarationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#variablesDeclaration.
    def exitVariablesDeclaration(self, ctx:simplifiedJavaGrammarParser.VariablesDeclarationContext):
        for token in ctx.ID():
            print(token)
            print(ctx.TYPE().getText())
            if ctx.TYPE().getText() == '<missing <INVALID>>':
                raise ErrorTypeNotReported(ctx.start.line, token.getText())

            if token.getText() in self.symbolTable and self.symbolTable[token.getText()].scope == self.scopeController:
                raise ErrorDeclarationAlreadyMade(ctx.start.line, token.getText())

            if token.getText() in self.symbolTable and self.symbolTable[token.getText()].scope == False:
                self.symbolTableCopy[token.getText()] = self.symbolTable[token.getText()]

            self.symbolTable[token.getText()] = Id(type=ctx.TYPE().getText(), scope=self.scopeController, address=self.newAddressController)
            self.newAddressController += 1 # atualiza o proximo endereco disponivel
            self.jasmin.create(token.getText(), ctx.TYPE().getText(), self.scopeController, False, 0)
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#constantsDeclaration.
    def enterConstantsDeclaration(self, ctx:simplifiedJavaGrammarParser.ConstantsDeclarationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#constantsDeclaration.
    def exitConstantsDeclaration(self, ctx:simplifiedJavaGrammarParser.ConstantsDeclarationContext):
        countInt = 0
        countFloat = 0
        countBool = 0
        countString = 0
        i = 0
    
        for token in ctx.ID():
            if token.getText() in self.symbolTable and self.symbolTable[token.getText()].scope == self.scopeController:
                raise ErrorDeclarationAlreadyMade(ctx.start.line, token.getText())
            if token.getText() in self.symbolTable and self.symbolTable[token.getText()].scope == False:
                self.symbolTableCopy[token.getText()] = self.symbolTable[token.getText()]
            
            if ctx.INT(countInt) != None and ctx.INT(countInt).getText() == ctx.terminal[i].text:
                self.symbolTable[token.getText()] = Id(type='int', scope=self.scopeController,
                                                        address=self.newAddressController)
                self.newAddressController += 1 
                self.jasmin.create(token.getText(), 'int', self.scopeController, True, ctx.INT(countInt).getText())
                countInt += 1
            elif ctx.FLOAT(countFloat) != None and ctx.FLOAT(countFloat).getText() == ctx.terminal[i].text:
                self.symbolTable[token.getText()] = Id(type='float', scope=self.scopeController,
                                                        address=self.newAddressController)
                self.newAddressController += 1 
                self.jasmin.create(token.getText(), 'float', self.scopeController, True, ctx.FLOAT(countFloat).getText())
                countFloat += 1
            elif ctx.STRING(countString) != None and ctx.STRING(countString).getText() == ctx.terminal[i].text:
                self.symbolTable[token.getText()] = Id(type='str', scope=self.scopeController,
                                                        address=self.newAddressController)
                self.newAddressController += 1 
                self.jasmin.create(token.getText(), 'str', self.scopeController, True, ctx.STRING(countString).getText())
                countString += 1
            else:
                self.symbolTable[token.getText()] = Id(type='bool', scope=self.scopeController,
                                                        address=self.newAddressController)
                self.newAddressController += 1 
                self.jasmin.create(token.getText(), 'bool', self.scopeController, True, ctx.BOOLEAN(countBool).getText())
                countBool += 1
            i += 1
    
        pass


   # Enter a parse tree produced by simplifiedJavaGrammarParser#commands.
    def enterCommands(self, ctx:simplifiedJavaGrammarParser.CommandsContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#commands.
    def exitCommands(self, ctx:simplifiedJavaGrammarParser.CommandsContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#callFunctionCommand.
    def enterCallFunctionCommand(self, ctx:simplifiedJavaGrammarParser.CallFunctionCommandContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#callFunctionCommand.
    def exitCallFunctionCommand(self, ctx:simplifiedJavaGrammarParser.CallFunctionCommandContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#ifCommand.
    def enterIfCommand(self, ctx:simplifiedJavaGrammarParser.IfCommandContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#ifCommand.
    def exitIfCommand(self, ctx:simplifiedJavaGrammarParser.IfCommandContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#whileCommand.
    def enterWhileCommand(self, ctx:simplifiedJavaGrammarParser.WhileCommandContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#whileCommand.
    def exitWhileCommand(self, ctx:simplifiedJavaGrammarParser.WhileCommandContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#printCommand.
    def enterPrintCommand(self, ctx:simplifiedJavaGrammarParser.PrintCommandContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#printCommand.
    def exitPrintCommand(self, ctx:simplifiedJavaGrammarParser.PrintCommandContext):
        typeVal = []
        for expr in ctx.expression():
            typeVal.append((expr.type, expr.val))

        self.jasmin.print(typeVal)
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#scanfCommand.
    def enterScanfCommand(self, ctx:simplifiedJavaGrammarParser.ScanfCommandContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#scanfCommand.
    def exitScanfCommand(self, ctx:simplifiedJavaGrammarParser.ScanfCommandContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#returnCommand.
    def enterReturnCommand(self, ctx:simplifiedJavaGrammarParser.ReturnCommandContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#returnCommand.
    def exitReturnCommand(self, ctx:simplifiedJavaGrammarParser.ReturnCommandContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#ifBlock.
    def enterIfBlock(self, ctx:simplifiedJavaGrammarParser.IfBlockContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#ifBlock.
    def exitIfBlock(self, ctx:simplifiedJavaGrammarParser.IfBlockContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#elseBlock.
    def enterElseBlock(self, ctx:simplifiedJavaGrammarParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#elseBlock.
    def exitElseBlock(self, ctx:simplifiedJavaGrammarParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#assigmentCommand.
    def enterAssigmentCommand(self, ctx:simplifiedJavaGrammarParser.AssigmentCommandContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#assigmentCommand.
    def exitAssigmentCommand(self, ctx:simplifiedJavaGrammarParser.AssigmentCommandContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#goTerm.
    def enterGoTerm(self, ctx:simplifiedJavaGrammarParser.GoTermContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#goTerm.
    def exitGoTerm(self, ctx:simplifiedJavaGrammarParser.GoTermContext):
        ctx.type = ctx.term().type
        ctx.val = ctx.term().val
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#comparativeOperation.
    def enterComparativeOperation(self, ctx:simplifiedJavaGrammarParser.ComparativeOperationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#comparativeOperation.
    def exitComparativeOperation(self, ctx:simplifiedJavaGrammarParser.ComparativeOperationContext):
        expressionType = ctx.expression().type
        expressionVal = ctx.expression().val  # endereco de variavel temporario

        termType = ctx.term().type
        termVal = ctx.term().val  # endereco de variavel temporario

        if str(expressionType) != str(termType):
            raise ErrorTypeExpression(ctx.start.line, ctx.op.text, expressionType, termType)

        ctx.type = 'bool'
        ctx.val = self.jasmin.compareExpressions(expressionType, expressionVal, termVal, self.newAddressController, ctx.op.text)
        self.newAddressController += 1
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#gotTerm2.
    def enterGotTerm2(self, ctx:simplifiedJavaGrammarParser.GotTerm2Context):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#gotTerm2.
    def exitGotTerm2(self, ctx:simplifiedJavaGrammarParser.GotTerm2Context):
        ctx.type = ctx.term2().type
        ctx.val = ctx.term2().val
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#equalDiffOperation.
    def enterEqualDiffOperation(self, ctx:simplifiedJavaGrammarParser.EqualDiffOperationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#equalDiffOperation.
    def exitEqualDiffOperation(self, ctx:simplifiedJavaGrammarParser.EqualDiffOperationContext):
        termType = ctx.term().type
        termVal = ctx.term().val  

        term2Type = ctx.term2().type
        term2Val = ctx.term2().val 

        if str(termType) != str(term2Type):
            raise ErrorTypeExpression(ctx.start.line, ctx.op.text, termType, term2Type)

        ctx.type = 'bool'
        ctx.val = self.jasmin.compareExpressions(termType, termVal, term2Val, self.newAddressController, ctx.op.text)
        self.newAddressController += 1
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#plusMinusOperation.
    def enterPlusMinusOperation(self, ctx:simplifiedJavaGrammarParser.PlusMinusOperationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#plusMinusOperation.
    def exitPlusMinusOperation(self, ctx:simplifiedJavaGrammarParser.PlusMinusOperationContext):
        term2Type = ctx.term2().type
        term2Val = ctx.term2().val

        term3Type = ctx.term3().type
        term3Val = ctx.term3().val 

        if not ((term2Type == 'int') or (term2Type == 'float')): 
            raise ErrorTypeExpression(ctx.start.line, ctx.op.text, term2Type)
        elif not ((term3Type == 'int') or (term3Type == 'float')): 
            raise ErrorTypeExpression(ctx.start.line, ctx.op.text, term3Type)
        elif term2Type == 'float' and term3Type == 'float':
            ctx.type = 'float'
            val1, val2 = term2Val, term3Val
        elif term2Type == 'float':
            ctx.type = 'float'
            val1, val2 = term2Val, self.jasmin.int_to_float(term3Val)
        elif term3Type == 'float':
            ctx.type = 'float'
            val1, val2 = self.jasmin.int_to_float(term2Val), term3Val
        else:
            ctx.type = 'int'
            val1, val2 = term2Val, term3Val

        if ctx.op.text == '+':
            ctx.val = self.jasmin.add(ctx.type, val1, val2, self.newAddressController)
            self.newAddressController += 1
        else:
            ctx.val = self.jasmin.sub(ctx.type, val1, val2, self.newAddressController)
            self.newAddressController += 1
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#goTerm3.
    def enterGoTerm3(self, ctx:simplifiedJavaGrammarParser.GoTerm3Context):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#goTerm3.
    def exitGoTerm3(self, ctx:simplifiedJavaGrammarParser.GoTerm3Context):
        ctx.type = ctx.term3().type
        ctx.val = ctx.term3().val
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#multDivOperation.
    def enterMultDivOperation(self, ctx:simplifiedJavaGrammarParser.MultDivOperationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#multDivOperation.
    def exitMultDivOperation(self, ctx:simplifiedJavaGrammarParser.MultDivOperationContext):
        term3Type = ctx.term3().type
        term3Val = ctx.term3().val  

        term4Type = ctx.term4().type
        term4Val = ctx.term4().val 

        if not ((term3Type == 'int') or (term3Type == 'float')): 
            raise ErrorTypeExpression(ctx.start.line, ctx.op.text, term3Type)
        elif not ((term4Type == 'int') or (term4Type == 'float')): 
            raise ErrorTypeExpression(ctx.start.line, ctx.op.text, term4Type)
        elif term3Type == 'float' and term4Type == 'float':
            ctx.type = 'float'
            val1, val2 = term3Val, term4Val
        elif term3Type == 'float':
            ctx.type = 'float'
            val1, val2 = term3Val, self.jasmin.int_to_float(term4Val)
        elif term4Type == 'float':
            ctx.type = 'float'
            val1, val2 = self.jasmin.int_to_float(term3Val), term4Val
        else:
            ctx.type = 'int'
            val1, val2 = term3Val, term4Val

        if ctx.op.text == '*':
            ctx.val = self.jasmin.mult(ctx.type, val1, val2, self.newAddressController)
            self.newAddressController += 1
        else:
            ctx.val = self.jasmin.div(ctx.type, val1, val2, self.newAddressController)
            self.newAddressController += 1
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#goTerm4.
    def enterGoTerm4(self, ctx:simplifiedJavaGrammarParser.GoTerm4Context):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#goTerm4.
    def exitGoTerm4(self, ctx:simplifiedJavaGrammarParser.GoTerm4Context):
        ctx.type = ctx.term4().type
        ctx.val = ctx.term4().val
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#unaryMinusOperation.
    def enterUnaryMinusOperation(self, ctx:simplifiedJavaGrammarParser.UnaryMinusOperationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#unaryMinusOperation.
    def exitUnaryMinusOperation(self, ctx:simplifiedJavaGrammarParser.UnaryMinusOperationContext):
        if (ctx.term4().type == 'float') or (ctx.term4().type == 'int'):
            ctx.type = ctx.term4().type
        else:
            raise ErrorTypeExpression(ctx.start.line, ctx.op.text, ctx.term4().type)

        ctx.val = self.jasmin.unaryMinus(ctx.term4().type, ctx.term4().val, self.newAddressController)
        self.newAddressController += 1
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#goTerm5.
    def enterGoTerm5(self, ctx:simplifiedJavaGrammarParser.GoTerm5Context):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#goTerm5.
    def exitGoTerm5(self, ctx:simplifiedJavaGrammarParser.GoTerm5Context):
        ctx.type = ctx.term5().type
        ctx.val = ctx.term5().val
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#notOperation.
    def enterNotOperation(self, ctx:simplifiedJavaGrammarParser.NotOperationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#notOperation.
    def exitNotOperation(self, ctx:simplifiedJavaGrammarParser.NotOperationContext):
        if ctx.term5().type == 'bool':
            ctx.type = 'bool'
        else:
            raise ErrorTypeExpression(ctx.start.line, ctx.op.text, ctx.term5().type)

        ctx.val = self.jasmin.notOp(ctx.term5().val, self.newAddressController)
        self.newAddressController += 1
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#goFactor.
    def enterGoFactor(self, ctx:simplifiedJavaGrammarParser.GoFactorContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#goFactor.
    def exitGoFactor(self, ctx:simplifiedJavaGrammarParser.GoFactorContext):
        ctx.type = ctx.factor().type
        ctx.val = ctx.factor().val
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#openCloseParantesisTerminal.
    def enterOpenCloseParantesisTerminal(self, ctx:simplifiedJavaGrammarParser.OpenCloseParantesisTerminalContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#openCloseParantesisTerminal.
    def exitOpenCloseParantesisTerminal(self, ctx:simplifiedJavaGrammarParser.OpenCloseParantesisTerminalContext):
        ctx.type = ctx.expression().type
        ctx.val = ctx.expression().val
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#idTerminal.
    def enterIdTerminal(self, ctx:simplifiedJavaGrammarParser.IdTerminalContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#idTerminal.
    def exitIdTerminal(self, ctx:simplifiedJavaGrammarParser.IdTerminalContext):
        ctxId = ctx.ID().getText()
        if ctxId not in self.symbolTable:
            raise ErrorVariableNotDeclared(ctx.start.line, ctxId)

        ctx.type = self.symbolTable[ctxId].type
        ctx.val = self.jasmin.load_var(ctxId, self.scopeController, self.newAddressController)
        self.newAddressController += 1
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#intTerminal.
    def enterIntTerminal(self, ctx:simplifiedJavaGrammarParser.IntTerminalContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#intTerminal.
    def exitIntTerminal(self, ctx:simplifiedJavaGrammarParser.IntTerminalContext):
        ctx.type = 'int'
        ctx.val = self.newAddressController
        self.jasmin.create_temp(ctx.getText(), ctx.type, self.newAddressController)
        self.newAddressController += 1
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#floatTerminal.
    def enterFloatTerminal(self, ctx:simplifiedJavaGrammarParser.FloatTerminalContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#floatTerminal.
    def exitFloatTerminal(self, ctx:simplifiedJavaGrammarParser.FloatTerminalContext):
        ctx.type = 'float'
        ctx.val = self.newAddressController
        self.jasmin.create_temp(ctx.getText(), ctx.type, self.newAddressController)
        self.newAddressController += 1
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#stringTerminal.
    def enterStringTerminal(self, ctx:simplifiedJavaGrammarParser.StringTerminalContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#stringTerminal.
    def exitStringTerminal(self, ctx:simplifiedJavaGrammarParser.StringTerminalContext):
        ctx.type = 'str'
        ctx.val = self.newAddressController
        self.jasmin.create_temp(ctx.getText(), ctx.type, self.newAddressController)
        self.newAddressController += 1
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#boolTerminal.
    def enterBoolTerminal(self, ctx:simplifiedJavaGrammarParser.BoolTerminalContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#boolTerminal.
    def exitBoolTerminal(self, ctx:simplifiedJavaGrammarParser.BoolTerminalContext):
        ctx.type = 'bool'
        ctx.val = self.newAddressController
        self.jasmin.create_temp(0 if ctx.getText() == 'False' else 1, ctx.type, self.newAddressController)
        self.newAddressController += 1
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#callFunctionTerminal.
    def enterCallFunctionTerminal(self, ctx:simplifiedJavaGrammarParser.CallFunctionTerminalContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#callFunctionTerminal.
    def exitCallFunctionTerminal(self, ctx:simplifiedJavaGrammarParser.CallFunctionTerminalContext):
        ctx.type = ctx.callFunctionCommand().type
        ctx.val = ctx.callFunctionCommand().val
        pass



del simplifiedJavaGrammarParser