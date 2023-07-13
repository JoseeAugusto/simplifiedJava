# Generated from C:/Users/jose1/Documents/UFPI/6º período/Compiladores/trabFinal/javaSimplificadoCompleto\simplifiedJavaGrammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .simplifiedJavaGrammarParser import simplifiedJavaGrammarParser
else:
    from simplifiedJavaGrammarParser import simplifiedJavaGrammarParser

# This class defines a complete listener for a parse tree produced by simplifiedJavaGrammarParser.
class simplifiedJavaGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by simplifiedJavaGrammarParser#program.
    def enterProgram(self, ctx:simplifiedJavaGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#program.
    def exitProgram(self, ctx:simplifiedJavaGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#functionDeclarationArea.
    def enterFunctionDeclarationArea(self, ctx:simplifiedJavaGrammarParser.FunctionDeclarationAreaContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#functionDeclarationArea.
    def exitFunctionDeclarationArea(self, ctx:simplifiedJavaGrammarParser.FunctionDeclarationAreaContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#main.
    def enterMain(self, ctx:simplifiedJavaGrammarParser.MainContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#main.
    def exitMain(self, ctx:simplifiedJavaGrammarParser.MainContext):
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
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#constantsDeclaration.
    def enterConstantsDeclaration(self, ctx:simplifiedJavaGrammarParser.ConstantsDeclarationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#constantsDeclaration.
    def exitConstantsDeclaration(self, ctx:simplifiedJavaGrammarParser.ConstantsDeclarationContext):
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


    # Enter a parse tree produced by simplifiedJavaGrammarParser#breakCommand.
    def enterBreakCommand(self, ctx:simplifiedJavaGrammarParser.BreakCommandContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#breakCommand.
    def exitBreakCommand(self, ctx:simplifiedJavaGrammarParser.BreakCommandContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#printCommand.
    def enterPrintCommand(self, ctx:simplifiedJavaGrammarParser.PrintCommandContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#printCommand.
    def exitPrintCommand(self, ctx:simplifiedJavaGrammarParser.PrintCommandContext):
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
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#comparativeOperation.
    def enterComparativeOperation(self, ctx:simplifiedJavaGrammarParser.ComparativeOperationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#comparativeOperation.
    def exitComparativeOperation(self, ctx:simplifiedJavaGrammarParser.ComparativeOperationContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#gotTerm2.
    def enterGotTerm2(self, ctx:simplifiedJavaGrammarParser.GotTerm2Context):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#gotTerm2.
    def exitGotTerm2(self, ctx:simplifiedJavaGrammarParser.GotTerm2Context):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#equalDiffOperation.
    def enterEqualDiffOperation(self, ctx:simplifiedJavaGrammarParser.EqualDiffOperationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#equalDiffOperation.
    def exitEqualDiffOperation(self, ctx:simplifiedJavaGrammarParser.EqualDiffOperationContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#plusMinusOperation.
    def enterPlusMinusOperation(self, ctx:simplifiedJavaGrammarParser.PlusMinusOperationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#plusMinusOperation.
    def exitPlusMinusOperation(self, ctx:simplifiedJavaGrammarParser.PlusMinusOperationContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#goTerm3.
    def enterGoTerm3(self, ctx:simplifiedJavaGrammarParser.GoTerm3Context):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#goTerm3.
    def exitGoTerm3(self, ctx:simplifiedJavaGrammarParser.GoTerm3Context):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#multDivOperation.
    def enterMultDivOperation(self, ctx:simplifiedJavaGrammarParser.MultDivOperationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#multDivOperation.
    def exitMultDivOperation(self, ctx:simplifiedJavaGrammarParser.MultDivOperationContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#goTerm4.
    def enterGoTerm4(self, ctx:simplifiedJavaGrammarParser.GoTerm4Context):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#goTerm4.
    def exitGoTerm4(self, ctx:simplifiedJavaGrammarParser.GoTerm4Context):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#unaryMinusOperation.
    def enterUnaryMinusOperation(self, ctx:simplifiedJavaGrammarParser.UnaryMinusOperationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#unaryMinusOperation.
    def exitUnaryMinusOperation(self, ctx:simplifiedJavaGrammarParser.UnaryMinusOperationContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#goTerm5.
    def enterGoTerm5(self, ctx:simplifiedJavaGrammarParser.GoTerm5Context):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#goTerm5.
    def exitGoTerm5(self, ctx:simplifiedJavaGrammarParser.GoTerm5Context):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#notOperation.
    def enterNotOperation(self, ctx:simplifiedJavaGrammarParser.NotOperationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#notOperation.
    def exitNotOperation(self, ctx:simplifiedJavaGrammarParser.NotOperationContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#goFactor.
    def enterGoFactor(self, ctx:simplifiedJavaGrammarParser.GoFactorContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#goFactor.
    def exitGoFactor(self, ctx:simplifiedJavaGrammarParser.GoFactorContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#openCloseParantesisTerminal.
    def enterOpenCloseParantesisTerminal(self, ctx:simplifiedJavaGrammarParser.OpenCloseParantesisTerminalContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#openCloseParantesisTerminal.
    def exitOpenCloseParantesisTerminal(self, ctx:simplifiedJavaGrammarParser.OpenCloseParantesisTerminalContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#idTerminal.
    def enterIdTerminal(self, ctx:simplifiedJavaGrammarParser.IdTerminalContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#idTerminal.
    def exitIdTerminal(self, ctx:simplifiedJavaGrammarParser.IdTerminalContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#intTerminal.
    def enterIntTerminal(self, ctx:simplifiedJavaGrammarParser.IntTerminalContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#intTerminal.
    def exitIntTerminal(self, ctx:simplifiedJavaGrammarParser.IntTerminalContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#floatTerminal.
    def enterFloatTerminal(self, ctx:simplifiedJavaGrammarParser.FloatTerminalContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#floatTerminal.
    def exitFloatTerminal(self, ctx:simplifiedJavaGrammarParser.FloatTerminalContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#stringTerminal.
    def enterStringTerminal(self, ctx:simplifiedJavaGrammarParser.StringTerminalContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#stringTerminal.
    def exitStringTerminal(self, ctx:simplifiedJavaGrammarParser.StringTerminalContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#boolTerminal.
    def enterBoolTerminal(self, ctx:simplifiedJavaGrammarParser.BoolTerminalContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#boolTerminal.
    def exitBoolTerminal(self, ctx:simplifiedJavaGrammarParser.BoolTerminalContext):
        pass


    # Enter a parse tree produced by simplifiedJavaGrammarParser#callFunctionTerminal.
    def enterCallFunctionTerminal(self, ctx:simplifiedJavaGrammarParser.CallFunctionTerminalContext):
        pass

    # Exit a parse tree produced by simplifiedJavaGrammarParser#callFunctionTerminal.
    def exitCallFunctionTerminal(self, ctx:simplifiedJavaGrammarParser.CallFunctionTerminalContext):
        pass



del simplifiedJavaGrammarParser