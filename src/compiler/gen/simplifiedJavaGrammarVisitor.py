# Generated from c:\Users\cassi\Documents\dev\uni\compilers\simple-java-compiler\simple-java\simplifiedJavaGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .simplifiedJavaGrammarParser import simplifiedJavaGrammarParser
else:
    from simplifiedJavaGrammarParser import simplifiedJavaGrammarParser

# This class defines a complete generic visitor for a parse tree produced by simplifiedJavaGrammarParser.

class simplifiedJavaGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by simplifiedJavaGrammarParser#program.
    def visitProgram(self, ctx:simplifiedJavaGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#functionDeclarationArea.
    def visitFunctionDeclarationArea(self, ctx:simplifiedJavaGrammarParser.FunctionDeclarationAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#main.
    def visitMain(self, ctx:simplifiedJavaGrammarParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#variablesDeclarationArea.
    def visitVariablesDeclarationArea(self, ctx:simplifiedJavaGrammarParser.VariablesDeclarationAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#variablesDeclaration.
    def visitVariablesDeclaration(self, ctx:simplifiedJavaGrammarParser.VariablesDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#constantsDeclaration.
    def visitConstantsDeclaration(self, ctx:simplifiedJavaGrammarParser.ConstantsDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#commands.
    def visitCommands(self, ctx:simplifiedJavaGrammarParser.CommandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#callFunctionCommand.
    def visitCallFunctionCommand(self, ctx:simplifiedJavaGrammarParser.CallFunctionCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#ifCommand.
    def visitIfCommand(self, ctx:simplifiedJavaGrammarParser.IfCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#whileCommand.
    def visitWhileCommand(self, ctx:simplifiedJavaGrammarParser.WhileCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#breakCommand.
    def visitBreakCommand(self, ctx:simplifiedJavaGrammarParser.BreakCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#printCommand.
    def visitPrintCommand(self, ctx:simplifiedJavaGrammarParser.PrintCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#scanfCommand.
    def visitScanfCommand(self, ctx:simplifiedJavaGrammarParser.ScanfCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#returnCommand.
    def visitReturnCommand(self, ctx:simplifiedJavaGrammarParser.ReturnCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#ifBlock.
    def visitIfBlock(self, ctx:simplifiedJavaGrammarParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#elseBlock.
    def visitElseBlock(self, ctx:simplifiedJavaGrammarParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#assigmentCommand.
    def visitAssigmentCommand(self, ctx:simplifiedJavaGrammarParser.AssigmentCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#goTerm.
    def visitGoTerm(self, ctx:simplifiedJavaGrammarParser.GoTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#comparativeOperation.
    def visitComparativeOperation(self, ctx:simplifiedJavaGrammarParser.ComparativeOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#gotTerm2.
    def visitGotTerm2(self, ctx:simplifiedJavaGrammarParser.GotTerm2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#equalDiffOperation.
    def visitEqualDiffOperation(self, ctx:simplifiedJavaGrammarParser.EqualDiffOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#plusMinusOperation.
    def visitPlusMinusOperation(self, ctx:simplifiedJavaGrammarParser.PlusMinusOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#goTerm3.
    def visitGoTerm3(self, ctx:simplifiedJavaGrammarParser.GoTerm3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#multDivOperation.
    def visitMultDivOperation(self, ctx:simplifiedJavaGrammarParser.MultDivOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#goTerm4.
    def visitGoTerm4(self, ctx:simplifiedJavaGrammarParser.GoTerm4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#unaryMinusOperation.
    def visitUnaryMinusOperation(self, ctx:simplifiedJavaGrammarParser.UnaryMinusOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#goTerm5.
    def visitGoTerm5(self, ctx:simplifiedJavaGrammarParser.GoTerm5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#notOperation.
    def visitNotOperation(self, ctx:simplifiedJavaGrammarParser.NotOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#goFactor.
    def visitGoFactor(self, ctx:simplifiedJavaGrammarParser.GoFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#openCloseParantesisTerminal.
    def visitOpenCloseParantesisTerminal(self, ctx:simplifiedJavaGrammarParser.OpenCloseParantesisTerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#idTerminal.
    def visitIdTerminal(self, ctx:simplifiedJavaGrammarParser.IdTerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#intTerminal.
    def visitIntTerminal(self, ctx:simplifiedJavaGrammarParser.IntTerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#floatTerminal.
    def visitFloatTerminal(self, ctx:simplifiedJavaGrammarParser.FloatTerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#stringTerminal.
    def visitStringTerminal(self, ctx:simplifiedJavaGrammarParser.StringTerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#boolTerminal.
    def visitBoolTerminal(self, ctx:simplifiedJavaGrammarParser.BoolTerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplifiedJavaGrammarParser#callFunctionTerminal.
    def visitCallFunctionTerminal(self, ctx:simplifiedJavaGrammarParser.CallFunctionTerminalContext):
        return self.visitChildren(ctx)



del simplifiedJavaGrammarParser