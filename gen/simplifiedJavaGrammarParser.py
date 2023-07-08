# Generated from C:/Users/jose1/Documents/UFPI/6º período/Compiladores/trabFinal/javaSimplificado\simplifiedJavaGrammar.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,304,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,62,8,1,10,1,12,1,65,9,1,3,1,67,8,
        1,1,1,1,1,1,1,1,1,5,1,73,8,1,10,1,12,1,76,9,1,1,1,5,1,79,8,1,10,
        1,12,1,82,9,1,1,1,1,1,1,2,1,2,1,2,5,2,89,8,2,10,2,12,2,92,9,2,1,
        2,5,2,95,8,2,10,2,12,2,98,9,2,1,2,1,2,1,3,1,3,1,3,1,3,4,3,106,8,
        3,11,3,12,3,107,1,4,1,4,1,4,5,4,113,8,4,10,4,12,4,116,9,4,1,4,1,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,130,8,5,10,5,12,5,
        133,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,146,8,6,
        1,7,1,7,1,7,1,7,1,7,5,7,153,8,7,10,7,12,7,156,9,7,3,7,158,8,7,1,
        7,1,7,1,8,1,8,3,8,164,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,174,
        8,9,10,9,12,9,177,9,9,1,9,3,9,180,8,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,5,10,189,8,10,10,10,12,10,192,9,10,1,10,1,10,1,10,1,11,1,11,
        1,11,1,11,1,11,5,11,202,8,11,10,11,12,11,205,9,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,220,8,13,
        10,13,12,13,223,9,13,1,14,1,14,1,14,5,14,228,8,14,10,14,12,14,231,
        9,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,
        244,8,16,10,16,12,16,247,9,16,1,17,1,17,1,17,1,17,1,17,1,17,5,17,
        255,8,17,10,17,12,17,258,9,17,1,18,1,18,1,18,1,18,1,18,1,18,5,18,
        266,8,18,10,18,12,18,269,9,18,1,19,1,19,1,19,1,19,1,19,1,19,5,19,
        277,8,19,10,19,12,19,280,9,19,1,20,1,20,1,20,3,20,285,8,20,1,21,
        1,21,1,21,3,21,290,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,3,22,302,8,22,1,22,0,4,32,34,36,38,23,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,6,2,0,5,5,30,30,
        1,0,31,34,1,0,19,22,1,0,23,24,1,0,25,26,1,0,27,28,318,0,49,1,0,0,
        0,2,54,1,0,0,0,4,85,1,0,0,0,6,101,1,0,0,0,8,109,1,0,0,0,10,121,1,
        0,0,0,12,145,1,0,0,0,14,147,1,0,0,0,16,161,1,0,0,0,18,167,1,0,0,
        0,20,183,1,0,0,0,22,196,1,0,0,0,24,209,1,0,0,0,26,213,1,0,0,0,28,
        224,1,0,0,0,30,232,1,0,0,0,32,237,1,0,0,0,34,248,1,0,0,0,36,259,
        1,0,0,0,38,270,1,0,0,0,40,284,1,0,0,0,42,289,1,0,0,0,44,301,1,0,
        0,0,46,48,3,2,1,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,
        1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,53,3,4,2,0,53,1,1,0,0,0,54,
        55,5,35,0,0,55,66,5,1,0,0,56,57,5,30,0,0,57,63,5,35,0,0,58,59,5,
        2,0,0,59,60,5,30,0,0,60,62,5,35,0,0,61,58,1,0,0,0,62,65,1,0,0,0,
        63,61,1,0,0,0,63,64,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,66,56,1,
        0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,69,5,3,0,0,69,70,5,4,0,0,70,
        74,7,0,0,0,71,73,3,6,3,0,72,71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,
        0,74,75,1,0,0,0,75,80,1,0,0,0,76,74,1,0,0,0,77,79,3,12,6,0,78,77,
        1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,83,1,0,0,0,
        82,80,1,0,0,0,83,84,5,6,0,0,84,3,1,0,0,0,85,86,5,7,0,0,86,90,5,4,
        0,0,87,89,3,6,3,0,88,87,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,
        1,0,0,0,91,96,1,0,0,0,92,90,1,0,0,0,93,95,3,12,6,0,94,93,1,0,0,0,
        95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,98,96,1,
        0,0,0,99,100,5,6,0,0,100,5,1,0,0,0,101,102,5,8,0,0,102,105,5,4,0,
        0,103,106,3,8,4,0,104,106,3,10,5,0,105,103,1,0,0,0,105,104,1,0,0,
        0,106,107,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,7,1,0,0,0,
        109,114,5,35,0,0,110,111,5,2,0,0,111,113,5,35,0,0,112,110,1,0,0,
        0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,
        0,116,114,1,0,0,0,117,118,5,4,0,0,118,119,5,30,0,0,119,120,5,9,0,
        0,120,9,1,0,0,0,121,122,5,10,0,0,122,123,5,35,0,0,123,124,5,11,0,
        0,124,131,7,1,0,0,125,126,5,2,0,0,126,127,5,35,0,0,127,128,5,11,
        0,0,128,130,7,1,0,0,129,125,1,0,0,0,130,133,1,0,0,0,131,129,1,0,
        0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,135,5,9,
        0,0,135,11,1,0,0,0,136,146,3,16,8,0,137,146,3,18,9,0,138,146,3,30,
        15,0,139,140,3,14,7,0,140,141,5,9,0,0,141,146,1,0,0,0,142,146,3,
        20,10,0,143,146,3,22,11,0,144,146,3,24,12,0,145,136,1,0,0,0,145,
        137,1,0,0,0,145,138,1,0,0,0,145,139,1,0,0,0,145,142,1,0,0,0,145,
        143,1,0,0,0,145,144,1,0,0,0,146,13,1,0,0,0,147,148,5,35,0,0,148,
        157,5,1,0,0,149,154,3,32,16,0,150,151,5,2,0,0,151,153,3,32,16,0,
        152,150,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,
        155,158,1,0,0,0,156,154,1,0,0,0,157,149,1,0,0,0,157,158,1,0,0,0,
        158,159,1,0,0,0,159,160,5,3,0,0,160,15,1,0,0,0,161,163,3,26,13,0,
        162,164,3,28,14,0,163,162,1,0,0,0,163,164,1,0,0,0,164,165,1,0,0,
        0,165,166,5,6,0,0,166,17,1,0,0,0,167,168,5,12,0,0,168,169,5,1,0,
        0,169,170,3,32,16,0,170,171,5,3,0,0,171,175,5,4,0,0,172,174,3,12,
        6,0,173,172,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,
        0,0,176,179,1,0,0,0,177,175,1,0,0,0,178,180,5,13,0,0,179,178,1,0,
        0,0,179,180,1,0,0,0,180,181,1,0,0,0,181,182,5,6,0,0,182,19,1,0,0,
        0,183,184,5,14,0,0,184,185,5,1,0,0,185,190,3,32,16,0,186,187,5,2,
        0,0,187,189,3,32,16,0,188,186,1,0,0,0,189,192,1,0,0,0,190,188,1,
        0,0,0,190,191,1,0,0,0,191,193,1,0,0,0,192,190,1,0,0,0,193,194,5,
        3,0,0,194,195,5,9,0,0,195,21,1,0,0,0,196,197,5,15,0,0,197,198,5,
        1,0,0,198,203,5,35,0,0,199,200,5,2,0,0,200,202,5,35,0,0,201,199,
        1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,206,
        1,0,0,0,205,203,1,0,0,0,206,207,5,3,0,0,207,208,5,9,0,0,208,23,1,
        0,0,0,209,210,5,16,0,0,210,211,3,32,16,0,211,212,5,9,0,0,212,25,
        1,0,0,0,213,214,5,17,0,0,214,215,5,1,0,0,215,216,3,32,16,0,216,217,
        5,3,0,0,217,221,5,4,0,0,218,220,3,12,6,0,219,218,1,0,0,0,220,223,
        1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,27,1,0,0,0,223,221,1,
        0,0,0,224,225,5,18,0,0,225,229,5,4,0,0,226,228,3,12,6,0,227,226,
        1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,29,1,
        0,0,0,231,229,1,0,0,0,232,233,5,35,0,0,233,234,5,11,0,0,234,235,
        3,32,16,0,235,236,5,9,0,0,236,31,1,0,0,0,237,238,6,16,-1,0,238,239,
        3,34,17,0,239,245,1,0,0,0,240,241,10,2,0,0,241,242,7,2,0,0,242,244,
        3,34,17,0,243,240,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,
        1,0,0,0,246,33,1,0,0,0,247,245,1,0,0,0,248,249,6,17,-1,0,249,250,
        3,36,18,0,250,256,1,0,0,0,251,252,10,2,0,0,252,253,7,3,0,0,253,255,
        3,36,18,0,254,251,1,0,0,0,255,258,1,0,0,0,256,254,1,0,0,0,256,257,
        1,0,0,0,257,35,1,0,0,0,258,256,1,0,0,0,259,260,6,18,-1,0,260,261,
        3,38,19,0,261,267,1,0,0,0,262,263,10,2,0,0,263,264,7,4,0,0,264,266,
        3,38,19,0,265,262,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,268,
        1,0,0,0,268,37,1,0,0,0,269,267,1,0,0,0,270,271,6,19,-1,0,271,272,
        3,40,20,0,272,278,1,0,0,0,273,274,10,2,0,0,274,275,7,5,0,0,275,277,
        3,40,20,0,276,273,1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,279,
        1,0,0,0,279,39,1,0,0,0,280,278,1,0,0,0,281,282,5,26,0,0,282,285,
        3,40,20,0,283,285,3,42,21,0,284,281,1,0,0,0,284,283,1,0,0,0,285,
        41,1,0,0,0,286,287,5,29,0,0,287,290,3,42,21,0,288,290,3,44,22,0,
        289,286,1,0,0,0,289,288,1,0,0,0,290,43,1,0,0,0,291,292,5,1,0,0,292,
        293,3,32,16,0,293,294,5,3,0,0,294,302,1,0,0,0,295,302,5,35,0,0,296,
        302,5,31,0,0,297,302,5,32,0,0,298,302,5,33,0,0,299,302,5,34,0,0,
        300,302,3,14,7,0,301,291,1,0,0,0,301,295,1,0,0,0,301,296,1,0,0,0,
        301,297,1,0,0,0,301,298,1,0,0,0,301,299,1,0,0,0,301,300,1,0,0,0,
        302,45,1,0,0,0,28,49,63,66,74,80,90,96,105,107,114,131,145,154,157,
        163,175,179,190,203,221,229,245,256,267,278,284,289,301
    ]

class simplifiedJavaGrammarParser ( Parser ):

    grammarFileName = "simplifiedJavaGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "':'", "'void'", 
                     "'end'", "'main'", "'var'", "';'", "'const'", "'='", 
                     "'while'", "'break;'", "'print'", "'scanf'", "'return'", 
                     "'if'", "'else'", "'>='", "'<='", "'>'", "'<'", "'=='", 
                     "'!='", "'+'", "'-'", "'*'", "'/'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "TYPE", "INT", "FLOAT", 
                      "STRING", "BOOLEAN", "ID", "WS", "CommentInOneLine", 
                      "CommentOnMultipleLines" ]

    RULE_program = 0
    RULE_functionDeclarationArea = 1
    RULE_main = 2
    RULE_variablesDeclarationArea = 3
    RULE_variablesDeclaration = 4
    RULE_constantsDeclaration = 5
    RULE_commands = 6
    RULE_callFunctionCommand = 7
    RULE_ifCommand = 8
    RULE_whileCommand = 9
    RULE_printCommand = 10
    RULE_scanfCommand = 11
    RULE_returnCommand = 12
    RULE_ifBlock = 13
    RULE_elseBlock = 14
    RULE_assigmentCommand = 15
    RULE_expression = 16
    RULE_term = 17
    RULE_term2 = 18
    RULE_term3 = 19
    RULE_term4 = 20
    RULE_term5 = 21
    RULE_factor = 22

    ruleNames =  [ "program", "functionDeclarationArea", "main", "variablesDeclarationArea", 
                   "variablesDeclaration", "constantsDeclaration", "commands", 
                   "callFunctionCommand", "ifCommand", "whileCommand", "printCommand", 
                   "scanfCommand", "returnCommand", "ifBlock", "elseBlock", 
                   "assigmentCommand", "expression", "term", "term2", "term3", 
                   "term4", "term5", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    TYPE=30
    INT=31
    FLOAT=32
    STRING=33
    BOOLEAN=34
    ID=35
    WS=36
    CommentInOneLine=37
    CommentOnMultipleLines=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.MainContext,0)


        def functionDeclarationArea(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaGrammarParser.FunctionDeclarationAreaContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaGrammarParser.FunctionDeclarationAreaContext,i)


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = simplifiedJavaGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 46
                self.functionDeclarationArea()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationAreaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(simplifiedJavaGrammarParser.ID)
            else:
                return self.getToken(simplifiedJavaGrammarParser.ID, i)

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(simplifiedJavaGrammarParser.TYPE)
            else:
                return self.getToken(simplifiedJavaGrammarParser.TYPE, i)

        def variablesDeclarationArea(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaGrammarParser.VariablesDeclarationAreaContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaGrammarParser.VariablesDeclarationAreaContext,i)


        def commands(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaGrammarParser.CommandsContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaGrammarParser.CommandsContext,i)


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_functionDeclarationArea

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclarationArea" ):
                listener.enterFunctionDeclarationArea(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclarationArea" ):
                listener.exitFunctionDeclarationArea(self)




    def functionDeclarationArea(self):

        localctx = simplifiedJavaGrammarParser.FunctionDeclarationAreaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDeclarationArea)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(simplifiedJavaGrammarParser.ID)
            self.state = 55
            self.match(simplifiedJavaGrammarParser.T__0)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 56
                self.match(simplifiedJavaGrammarParser.TYPE)
                self.state = 57
                self.match(simplifiedJavaGrammarParser.ID)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 58
                    self.match(simplifiedJavaGrammarParser.T__1)
                    self.state = 59
                    self.match(simplifiedJavaGrammarParser.TYPE)
                    self.state = 60
                    self.match(simplifiedJavaGrammarParser.ID)
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 68
            self.match(simplifiedJavaGrammarParser.T__2)
            self.state = 69
            self.match(simplifiedJavaGrammarParser.T__3)
            self.state = 70
            _la = self._input.LA(1)
            if not(_la==5 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 71
                self.variablesDeclarationArea()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34359988224) != 0):
                self.state = 77
                self.commands()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
            self.match(simplifiedJavaGrammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variablesDeclarationArea(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaGrammarParser.VariablesDeclarationAreaContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaGrammarParser.VariablesDeclarationAreaContext,i)


        def commands(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaGrammarParser.CommandsContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaGrammarParser.CommandsContext,i)


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = simplifiedJavaGrammarParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(simplifiedJavaGrammarParser.T__6)
            self.state = 86
            self.match(simplifiedJavaGrammarParser.T__3)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 87
                self.variablesDeclarationArea()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34359988224) != 0):
                self.state = 93
                self.commands()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self.match(simplifiedJavaGrammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesDeclarationAreaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variablesDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaGrammarParser.VariablesDeclarationContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaGrammarParser.VariablesDeclarationContext,i)


        def constantsDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaGrammarParser.ConstantsDeclarationContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaGrammarParser.ConstantsDeclarationContext,i)


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_variablesDeclarationArea

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariablesDeclarationArea" ):
                listener.enterVariablesDeclarationArea(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariablesDeclarationArea" ):
                listener.exitVariablesDeclarationArea(self)




    def variablesDeclarationArea(self):

        localctx = simplifiedJavaGrammarParser.VariablesDeclarationAreaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variablesDeclarationArea)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(simplifiedJavaGrammarParser.T__7)
            self.state = 102
            self.match(simplifiedJavaGrammarParser.T__3)
            self.state = 105 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 105
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [35]:
                        self.state = 103
                        self.variablesDeclaration()
                        pass
                    elif token in [10]:
                        self.state = 104
                        self.constantsDeclaration()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 107 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(simplifiedJavaGrammarParser.ID)
            else:
                return self.getToken(simplifiedJavaGrammarParser.ID, i)

        def TYPE(self):
            return self.getToken(simplifiedJavaGrammarParser.TYPE, 0)

        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_variablesDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariablesDeclaration" ):
                listener.enterVariablesDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariablesDeclaration" ):
                listener.exitVariablesDeclaration(self)




    def variablesDeclaration(self):

        localctx = simplifiedJavaGrammarParser.VariablesDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variablesDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(simplifiedJavaGrammarParser.ID)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 110
                self.match(simplifiedJavaGrammarParser.T__1)
                self.state = 111
                self.match(simplifiedJavaGrammarParser.ID)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
            self.match(simplifiedJavaGrammarParser.T__3)
            self.state = 118
            self.match(simplifiedJavaGrammarParser.TYPE)
            self.state = 119
            self.match(simplifiedJavaGrammarParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantsDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.terminal = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(simplifiedJavaGrammarParser.ID)
            else:
                return self.getToken(simplifiedJavaGrammarParser.ID, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(simplifiedJavaGrammarParser.STRING)
            else:
                return self.getToken(simplifiedJavaGrammarParser.STRING, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(simplifiedJavaGrammarParser.INT)
            else:
                return self.getToken(simplifiedJavaGrammarParser.INT, i)

        def BOOLEAN(self, i:int=None):
            if i is None:
                return self.getTokens(simplifiedJavaGrammarParser.BOOLEAN)
            else:
                return self.getToken(simplifiedJavaGrammarParser.BOOLEAN, i)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(simplifiedJavaGrammarParser.FLOAT)
            else:
                return self.getToken(simplifiedJavaGrammarParser.FLOAT, i)

        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_constantsDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantsDeclaration" ):
                listener.enterConstantsDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantsDeclaration" ):
                listener.exitConstantsDeclaration(self)




    def constantsDeclaration(self):

        localctx = simplifiedJavaGrammarParser.ConstantsDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constantsDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(simplifiedJavaGrammarParser.T__9)
            self.state = 122
            self.match(simplifiedJavaGrammarParser.ID)
            self.state = 123
            self.match(simplifiedJavaGrammarParser.T__10)
            self.state = 124
            localctx.terminal = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                localctx.terminal = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 125
                self.match(simplifiedJavaGrammarParser.T__1)
                self.state = 126
                self.match(simplifiedJavaGrammarParser.ID)
                self.state = 127
                self.match(simplifiedJavaGrammarParser.T__10)
                self.state = 128
                localctx.terminal = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                    localctx.terminal = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self.match(simplifiedJavaGrammarParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifCommand(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.IfCommandContext,0)


        def whileCommand(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.WhileCommandContext,0)


        def assigmentCommand(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.AssigmentCommandContext,0)


        def callFunctionCommand(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.CallFunctionCommandContext,0)


        def printCommand(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.PrintCommandContext,0)


        def scanfCommand(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.ScanfCommandContext,0)


        def returnCommand(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.ReturnCommandContext,0)


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_commands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommands" ):
                listener.enterCommands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommands" ):
                listener.exitCommands(self)




    def commands(self):

        localctx = simplifiedJavaGrammarParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_commands)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.ifCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.whileCommand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.assigmentCommand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.callFunctionCommand()
                self.state = 140
                self.match(simplifiedJavaGrammarParser.T__8)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 142
                self.printCommand()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 143
                self.scanfCommand()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 144
                self.returnCommand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallFunctionCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplifiedJavaGrammarParser.ID, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaGrammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_callFunctionCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallFunctionCommand" ):
                listener.enterCallFunctionCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallFunctionCommand" ):
                listener.exitCallFunctionCommand(self)




    def callFunctionCommand(self):

        localctx = simplifiedJavaGrammarParser.CallFunctionCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_callFunctionCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(simplifiedJavaGrammarParser.ID)
            self.state = 148
            self.match(simplifiedJavaGrammarParser.T__0)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67175972866) != 0):
                self.state = 149
                self.expression(0)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 150
                    self.match(simplifiedJavaGrammarParser.T__1)
                    self.state = 151
                    self.expression(0)
                    self.state = 156
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 159
            self.match(simplifiedJavaGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifBlock(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.IfBlockContext,0)


        def elseBlock(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.ElseBlockContext,0)


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_ifCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfCommand" ):
                listener.enterIfCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfCommand" ):
                listener.exitIfCommand(self)




    def ifCommand(self):

        localctx = simplifiedJavaGrammarParser.IfCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.ifBlock()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 162
                self.elseBlock()


            self.state = 165
            self.match(simplifiedJavaGrammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.ExpressionContext,0)


        def commands(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaGrammarParser.CommandsContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaGrammarParser.CommandsContext,i)


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_whileCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileCommand" ):
                listener.enterWhileCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileCommand" ):
                listener.exitWhileCommand(self)




    def whileCommand(self):

        localctx = simplifiedJavaGrammarParser.WhileCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(simplifiedJavaGrammarParser.T__11)
            self.state = 168
            self.match(simplifiedJavaGrammarParser.T__0)
            self.state = 169
            self.expression(0)
            self.state = 170
            self.match(simplifiedJavaGrammarParser.T__2)
            self.state = 171
            self.match(simplifiedJavaGrammarParser.T__3)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34359988224) != 0):
                self.state = 172
                self.commands()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 178
                self.match(simplifiedJavaGrammarParser.T__12)


            self.state = 181
            self.match(simplifiedJavaGrammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaGrammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_printCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintCommand" ):
                listener.enterPrintCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintCommand" ):
                listener.exitPrintCommand(self)




    def printCommand(self):

        localctx = simplifiedJavaGrammarParser.PrintCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_printCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(simplifiedJavaGrammarParser.T__13)
            self.state = 184
            self.match(simplifiedJavaGrammarParser.T__0)
            self.state = 185
            self.expression(0)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 186
                self.match(simplifiedJavaGrammarParser.T__1)
                self.state = 187
                self.expression(0)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 193
            self.match(simplifiedJavaGrammarParser.T__2)
            self.state = 194
            self.match(simplifiedJavaGrammarParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScanfCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(simplifiedJavaGrammarParser.ID)
            else:
                return self.getToken(simplifiedJavaGrammarParser.ID, i)

        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_scanfCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScanfCommand" ):
                listener.enterScanfCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScanfCommand" ):
                listener.exitScanfCommand(self)




    def scanfCommand(self):

        localctx = simplifiedJavaGrammarParser.ScanfCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_scanfCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(simplifiedJavaGrammarParser.T__14)
            self.state = 197
            self.match(simplifiedJavaGrammarParser.T__0)
            self.state = 198
            self.match(simplifiedJavaGrammarParser.ID)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 199
                self.match(simplifiedJavaGrammarParser.T__1)
                self.state = 200
                self.match(simplifiedJavaGrammarParser.ID)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
            self.match(simplifiedJavaGrammarParser.T__2)
            self.state = 207
            self.match(simplifiedJavaGrammarParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_returnCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnCommand" ):
                listener.enterReturnCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnCommand" ):
                listener.exitReturnCommand(self)




    def returnCommand(self):

        localctx = simplifiedJavaGrammarParser.ReturnCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_returnCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(simplifiedJavaGrammarParser.T__15)
            self.state = 210
            self.expression(0)
            self.state = 211
            self.match(simplifiedJavaGrammarParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.ExpressionContext,0)


        def commands(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaGrammarParser.CommandsContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaGrammarParser.CommandsContext,i)


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_ifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlock" ):
                listener.enterIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlock" ):
                listener.exitIfBlock(self)




    def ifBlock(self):

        localctx = simplifiedJavaGrammarParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(simplifiedJavaGrammarParser.T__16)
            self.state = 214
            self.match(simplifiedJavaGrammarParser.T__0)
            self.state = 215
            self.expression(0)
            self.state = 216
            self.match(simplifiedJavaGrammarParser.T__2)
            self.state = 217
            self.match(simplifiedJavaGrammarParser.T__3)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34359988224) != 0):
                self.state = 218
                self.commands()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commands(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaGrammarParser.CommandsContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaGrammarParser.CommandsContext,i)


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_elseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseBlock" ):
                listener.enterElseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseBlock" ):
                listener.exitElseBlock(self)




    def elseBlock(self):

        localctx = simplifiedJavaGrammarParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_elseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(simplifiedJavaGrammarParser.T__17)
            self.state = 225
            self.match(simplifiedJavaGrammarParser.T__3)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34359988224) != 0):
                self.state = 226
                self.commands()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigmentCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplifiedJavaGrammarParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_assigmentCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssigmentCommand" ):
                listener.enterAssigmentCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssigmentCommand" ):
                listener.exitAssigmentCommand(self)




    def assigmentCommand(self):

        localctx = simplifiedJavaGrammarParser.AssigmentCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assigmentCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(simplifiedJavaGrammarParser.ID)
            self.state = 233
            self.match(simplifiedJavaGrammarParser.T__10)
            self.state = 234
            self.expression(0)
            self.state = 235
            self.match(simplifiedJavaGrammarParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None
            self.inhType = None


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_
            self.inhType = ctx.inhType


    class GoTermContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoTerm" ):
                listener.enterGoTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoTerm" ):
                listener.exitGoTerm(self)


    class ComparativeOperationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.ExpressionContext,0)

        def term(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparativeOperation" ):
                listener.enterComparativeOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparativeOperation" ):
                listener.exitComparativeOperation(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = simplifiedJavaGrammarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = simplifiedJavaGrammarParser.GoTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 238
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 245
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = simplifiedJavaGrammarParser.ComparativeOperationContext(self, simplifiedJavaGrammarParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 240
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 241
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 242
                    self.term(0) 
                self.state = 247
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class GotTerm2Context(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term2(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.Term2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotTerm2" ):
                listener.enterGotTerm2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotTerm2" ):
                listener.exitGotTerm2(self)


    class EqualDiffOperationContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.TermContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.TermContext,0)

        def term2(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.Term2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualDiffOperation" ):
                listener.enterEqualDiffOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualDiffOperation" ):
                listener.exitEqualDiffOperation(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = simplifiedJavaGrammarParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = simplifiedJavaGrammarParser.GotTerm2Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 249
            self.term2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 256
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = simplifiedJavaGrammarParser.EqualDiffOperationContext(self, simplifiedJavaGrammarParser.TermContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 251
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 252
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==23 or _la==24):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 253
                    self.term2(0) 
                self.state = 258
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_term2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class PlusMinusOperationContext(Term2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.Term2Context
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term2(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.Term2Context,0)

        def term3(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.Term3Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlusMinusOperation" ):
                listener.enterPlusMinusOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlusMinusOperation" ):
                listener.exitPlusMinusOperation(self)


    class GoTerm3Context(Term2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.Term2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def term3(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.Term3Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoTerm3" ):
                listener.enterGoTerm3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoTerm3" ):
                listener.exitGoTerm3(self)



    def term2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = simplifiedJavaGrammarParser.Term2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_term2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = simplifiedJavaGrammarParser.GoTerm3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 260
            self.term3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = simplifiedJavaGrammarParser.PlusMinusOperationContext(self, simplifiedJavaGrammarParser.Term2Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term2)
                    self.state = 262
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 263
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==25 or _la==26):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 264
                    self.term3(0) 
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_term3

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class MultDivOperationContext(Term3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.Term3Context
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term3(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.Term3Context,0)

        def term4(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.Term4Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultDivOperation" ):
                listener.enterMultDivOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultDivOperation" ):
                listener.exitMultDivOperation(self)


    class GoTerm4Context(Term3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.Term3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def term4(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.Term4Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoTerm4" ):
                listener.enterGoTerm4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoTerm4" ):
                listener.exitGoTerm4(self)



    def term3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = simplifiedJavaGrammarParser.Term3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_term3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = simplifiedJavaGrammarParser.GoTerm4Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 271
            self.term4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = simplifiedJavaGrammarParser.MultDivOperationContext(self, simplifiedJavaGrammarParser.Term3Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term3)
                    self.state = 273
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 274
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==27 or _la==28):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 275
                    self.term4() 
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_term4

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_



    class GoTerm5Context(Term4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.Term4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def term5(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.Term5Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoTerm5" ):
                listener.enterGoTerm5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoTerm5" ):
                listener.exitGoTerm5(self)


    class UnaryMinusOperationContext(Term4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.Term4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def term4(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.Term4Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusOperation" ):
                listener.enterUnaryMinusOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusOperation" ):
                listener.exitUnaryMinusOperation(self)



    def term4(self):

        localctx = simplifiedJavaGrammarParser.Term4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_term4)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                localctx = simplifiedJavaGrammarParser.UnaryMinusOperationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.match(simplifiedJavaGrammarParser.T__25)
                self.state = 282
                self.term4()
                pass
            elif token in [1, 29, 31, 32, 33, 34, 35]:
                localctx = simplifiedJavaGrammarParser.GoTerm5Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.term5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_term5

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_



    class GoFactorContext(Term5Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.Term5Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoFactor" ):
                listener.enterGoFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoFactor" ):
                listener.exitGoFactor(self)


    class NotOperationContext(Term5Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.Term5Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def term5(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.Term5Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotOperation" ):
                listener.enterNotOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotOperation" ):
                listener.exitNotOperation(self)



    def term5(self):

        localctx = simplifiedJavaGrammarParser.Term5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_term5)
        try:
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                localctx = simplifiedJavaGrammarParser.NotOperationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(simplifiedJavaGrammarParser.T__28)
                self.state = 287
                self.term5()
                pass
            elif token in [1, 31, 32, 33, 34, 35]:
                localctx = simplifiedJavaGrammarParser.GoFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_



    class BoolTerminalContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(simplifiedJavaGrammarParser.BOOLEAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolTerminal" ):
                listener.enterBoolTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolTerminal" ):
                listener.exitBoolTerminal(self)


    class CallFunctionTerminalContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def callFunctionCommand(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.CallFunctionCommandContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallFunctionTerminal" ):
                listener.enterCallFunctionTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallFunctionTerminal" ):
                listener.exitCallFunctionTerminal(self)


    class OpenCloseParantesisTerminalContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpenCloseParantesisTerminal" ):
                listener.enterOpenCloseParantesisTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpenCloseParantesisTerminal" ):
                listener.exitOpenCloseParantesisTerminal(self)


    class IdTerminalContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(simplifiedJavaGrammarParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdTerminal" ):
                listener.enterIdTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdTerminal" ):
                listener.exitIdTerminal(self)


    class IntTerminalContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(simplifiedJavaGrammarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntTerminal" ):
                listener.enterIntTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntTerminal" ):
                listener.exitIntTerminal(self)


    class FloatTerminalContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(simplifiedJavaGrammarParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatTerminal" ):
                listener.enterFloatTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatTerminal" ):
                listener.exitFloatTerminal(self)


    class StringTerminalContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a simplifiedJavaGrammarParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(simplifiedJavaGrammarParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringTerminal" ):
                listener.enterStringTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringTerminal" ):
                listener.exitStringTerminal(self)



    def factor(self):

        localctx = simplifiedJavaGrammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_factor)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                localctx = simplifiedJavaGrammarParser.OpenCloseParantesisTerminalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(simplifiedJavaGrammarParser.T__0)
                self.state = 292
                self.expression(0)
                self.state = 293
                self.match(simplifiedJavaGrammarParser.T__2)
                pass

            elif la_ == 2:
                localctx = simplifiedJavaGrammarParser.IdTerminalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(simplifiedJavaGrammarParser.ID)
                pass

            elif la_ == 3:
                localctx = simplifiedJavaGrammarParser.IntTerminalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.match(simplifiedJavaGrammarParser.INT)
                pass

            elif la_ == 4:
                localctx = simplifiedJavaGrammarParser.FloatTerminalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 297
                self.match(simplifiedJavaGrammarParser.FLOAT)
                pass

            elif la_ == 5:
                localctx = simplifiedJavaGrammarParser.StringTerminalContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 298
                self.match(simplifiedJavaGrammarParser.STRING)
                pass

            elif la_ == 6:
                localctx = simplifiedJavaGrammarParser.BoolTerminalContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 299
                self.match(simplifiedJavaGrammarParser.BOOLEAN)
                pass

            elif la_ == 7:
                localctx = simplifiedJavaGrammarParser.CallFunctionTerminalContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 300
                self.callFunctionCommand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expression_sempred
        self._predicates[17] = self.term_sempred
        self._predicates[18] = self.term2_sempred
        self._predicates[19] = self.term3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term2_sempred(self, localctx:Term2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def term3_sempred(self, localctx:Term3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




