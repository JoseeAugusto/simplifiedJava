# Generated from c:\Users\cassi\Documents\dev\uni\compilers\simple-java-compiler\simple-java\simplifiedJavaGrammar.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(")
        buf.write("\u012f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\7\2\64\n\2\f\2\16\2\67\13\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\7\3C\n\3\f\3\16\3F\13\3\5\3H")
        buf.write("\n\3\3\3\3\3\3\3\3\3\5\3N\n\3\3\3\7\3Q\n\3\f\3\16\3T\13")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\5\4[\n\4\3\4\7\4^\n\4\f\4\16\4")
        buf.write("a\13\4\3\4\3\4\3\5\3\5\3\5\3\5\6\5i\n\5\r\5\16\5j\3\6")
        buf.write("\3\6\3\6\7\6p\n\6\f\6\16\6s\13\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u0081\n\7\f\7\16\7\u0084")
        buf.write("\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u0092\n\b\3\t\3\t\3\t\3\t\3\t\7\t\u0099\n\t\f\t\16")
        buf.write("\t\u009c\13\t\5\t\u009e\n\t\3\t\3\t\3\n\3\n\5\n\u00a4")
        buf.write("\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u00ae")
        buf.write("\n\13\f\13\16\13\u00b1\13\13\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\7\r\u00bc\n\r\f\r\16\r\u00bf\13\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\7\16\u00c9\n\16\f\16\16")
        buf.write("\16\u00cc\13\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\7\20\u00db\n\20\f\20\16\20\u00de")
        buf.write("\13\20\3\21\3\21\3\21\7\21\u00e3\n\21\f\21\16\21\u00e6")
        buf.write("\13\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\7\23\u00f3\n\23\f\23\16\23\u00f6\13\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\7\24\u00fe\n\24\f\24\16\24\u0101")
        buf.write("\13\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u0109\n\25\f")
        buf.write("\25\16\25\u010c\13\25\3\26\3\26\3\26\3\26\3\26\3\26\7")
        buf.write("\26\u0114\n\26\f\26\16\26\u0117\13\26\3\27\3\27\3\27\5")
        buf.write("\27\u011c\n\27\3\30\3\30\3\30\5\30\u0121\n\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u012d\n")
        buf.write("\31\3\31\2\6$&(*\32\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\2\b\3\2\37 \3\2!$\3\2\24\27\3\2\30\31")
        buf.write("\3\2\32\33\3\2\34\35\2\u013c\2\65\3\2\2\2\4;\3\2\2\2\6")
        buf.write("W\3\2\2\2\bd\3\2\2\2\nl\3\2\2\2\fx\3\2\2\2\16\u0091\3")
        buf.write("\2\2\2\20\u0093\3\2\2\2\22\u00a1\3\2\2\2\24\u00a7\3\2")
        buf.write("\2\2\26\u00b4\3\2\2\2\30\u00b6\3\2\2\2\32\u00c3\3\2\2")
        buf.write("\2\34\u00d0\3\2\2\2\36\u00d4\3\2\2\2 \u00df\3\2\2\2\"")
        buf.write("\u00e7\3\2\2\2$\u00ec\3\2\2\2&\u00f7\3\2\2\2(\u0102\3")
        buf.write("\2\2\2*\u010d\3\2\2\2,\u011b\3\2\2\2.\u0120\3\2\2\2\60")
        buf.write("\u012c\3\2\2\2\62\64\5\4\3\2\63\62\3\2\2\2\64\67\3\2\2")
        buf.write("\2\65\63\3\2\2\2\65\66\3\2\2\2\668\3\2\2\2\67\65\3\2\2")
        buf.write("\289\5\6\4\29:\7\2\2\3:\3\3\2\2\2;<\7%\2\2<G\7\3\2\2=")
        buf.write(">\7\37\2\2>D\7%\2\2?@\7\4\2\2@A\7\37\2\2AC\7%\2\2B?\3")
        buf.write("\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2EH\3\2\2\2FD\3\2\2")
        buf.write("\2G=\3\2\2\2GH\3\2\2\2HI\3\2\2\2IJ\7\5\2\2JK\7\6\2\2K")
        buf.write("M\t\2\2\2LN\5\b\5\2ML\3\2\2\2MN\3\2\2\2NR\3\2\2\2OQ\5")
        buf.write("\16\b\2PO\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2SU\3\2")
        buf.write("\2\2TR\3\2\2\2UV\7\7\2\2V\5\3\2\2\2WX\7\b\2\2XZ\7\6\2")
        buf.write("\2Y[\5\b\5\2ZY\3\2\2\2Z[\3\2\2\2[_\3\2\2\2\\^\5\16\b\2")
        buf.write("]\\\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`b\3\2\2\2a_")
        buf.write("\3\2\2\2bc\7\7\2\2c\7\3\2\2\2de\7\t\2\2eh\7\6\2\2fi\5")
        buf.write("\n\6\2gi\5\f\7\2hf\3\2\2\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2")
        buf.write("\2jk\3\2\2\2k\t\3\2\2\2lq\7%\2\2mn\7\4\2\2np\7%\2\2om")
        buf.write("\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2rt\3\2\2\2sq\3\2")
        buf.write("\2\2tu\7\6\2\2uv\7\37\2\2vw\7\n\2\2w\13\3\2\2\2xy\7\13")
        buf.write("\2\2yz\7%\2\2z{\7\f\2\2{\u0082\t\3\2\2|}\7\4\2\2}~\7%")
        buf.write("\2\2~\177\7\f\2\2\177\u0081\t\3\2\2\u0080|\3\2\2\2\u0081")
        buf.write("\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2")
        buf.write("\u0083\u0085\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0086\7")
        buf.write("\n\2\2\u0086\r\3\2\2\2\u0087\u0092\5\22\n\2\u0088\u0092")
        buf.write("\5\24\13\2\u0089\u0092\5\"\22\2\u008a\u008b\5\20\t\2\u008b")
        buf.write("\u008c\7\n\2\2\u008c\u0092\3\2\2\2\u008d\u0092\5\30\r")
        buf.write("\2\u008e\u0092\5\32\16\2\u008f\u0092\5\34\17\2\u0090\u0092")
        buf.write("\5\26\f\2\u0091\u0087\3\2\2\2\u0091\u0088\3\2\2\2\u0091")
        buf.write("\u0089\3\2\2\2\u0091\u008a\3\2\2\2\u0091\u008d\3\2\2\2")
        buf.write("\u0091\u008e\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0090\3")
        buf.write("\2\2\2\u0092\17\3\2\2\2\u0093\u0094\7%\2\2\u0094\u009d")
        buf.write("\7\3\2\2\u0095\u009a\5$\23\2\u0096\u0097\7\4\2\2\u0097")
        buf.write("\u0099\5$\23\2\u0098\u0096\3\2\2\2\u0099\u009c\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009e\3")
        buf.write("\2\2\2\u009c\u009a\3\2\2\2\u009d\u0095\3\2\2\2\u009d\u009e")
        buf.write("\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\7\5\2\2\u00a0")
        buf.write("\21\3\2\2\2\u00a1\u00a3\5\36\20\2\u00a2\u00a4\5 \21\2")
        buf.write("\u00a3\u00a2\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\3")
        buf.write("\2\2\2\u00a5\u00a6\7\7\2\2\u00a6\23\3\2\2\2\u00a7\u00a8")
        buf.write("\7\r\2\2\u00a8\u00a9\7\3\2\2\u00a9\u00aa\5$\23\2\u00aa")
        buf.write("\u00ab\7\5\2\2\u00ab\u00af\7\6\2\2\u00ac\u00ae\5\16\b")
        buf.write("\2\u00ad\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b2\u00b3\7\7\2\2\u00b3\25\3\2\2\2\u00b4")
        buf.write("\u00b5\7\16\2\2\u00b5\27\3\2\2\2\u00b6\u00b7\7\17\2\2")
        buf.write("\u00b7\u00b8\7\3\2\2\u00b8\u00bd\5$\23\2\u00b9\u00ba\7")
        buf.write("\4\2\2\u00ba\u00bc\5$\23\2\u00bb\u00b9\3\2\2\2\u00bc\u00bf")
        buf.write("\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00c0\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c1\7\5\2\2")
        buf.write("\u00c1\u00c2\7\n\2\2\u00c2\31\3\2\2\2\u00c3\u00c4\7\20")
        buf.write("\2\2\u00c4\u00c5\7\3\2\2\u00c5\u00ca\7%\2\2\u00c6\u00c7")
        buf.write("\7\4\2\2\u00c7\u00c9\7%\2\2\u00c8\u00c6\3\2\2\2\u00c9")
        buf.write("\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2")
        buf.write("\u00cb\u00cd\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce\7")
        buf.write("\5\2\2\u00ce\u00cf\7\n\2\2\u00cf\33\3\2\2\2\u00d0\u00d1")
        buf.write("\7\21\2\2\u00d1\u00d2\5$\23\2\u00d2\u00d3\7\n\2\2\u00d3")
        buf.write("\35\3\2\2\2\u00d4\u00d5\7\22\2\2\u00d5\u00d6\7\3\2\2\u00d6")
        buf.write("\u00d7\5$\23\2\u00d7\u00d8\7\5\2\2\u00d8\u00dc\7\6\2\2")
        buf.write("\u00d9\u00db\5\16\b\2\u00da\u00d9\3\2\2\2\u00db\u00de")
        buf.write("\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd")
        buf.write("\37\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e0\7\23\2\2\u00e0")
        buf.write("\u00e4\7\6\2\2\u00e1\u00e3\5\16\b\2\u00e2\u00e1\3\2\2")
        buf.write("\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5")
        buf.write("\3\2\2\2\u00e5!\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e8")
        buf.write("\7%\2\2\u00e8\u00e9\7\f\2\2\u00e9\u00ea\5$\23\2\u00ea")
        buf.write("\u00eb\7\n\2\2\u00eb#\3\2\2\2\u00ec\u00ed\b\23\1\2\u00ed")
        buf.write("\u00ee\5&\24\2\u00ee\u00f4\3\2\2\2\u00ef\u00f0\f\4\2\2")
        buf.write("\u00f0\u00f1\t\4\2\2\u00f1\u00f3\5&\24\2\u00f2\u00ef\3")
        buf.write("\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5")
        buf.write("\3\2\2\2\u00f5%\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f8")
        buf.write("\b\24\1\2\u00f8\u00f9\5(\25\2\u00f9\u00ff\3\2\2\2\u00fa")
        buf.write("\u00fb\f\4\2\2\u00fb\u00fc\t\5\2\2\u00fc\u00fe\5(\25\2")
        buf.write("\u00fd\u00fa\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3")
        buf.write("\2\2\2\u00ff\u0100\3\2\2\2\u0100\'\3\2\2\2\u0101\u00ff")
        buf.write("\3\2\2\2\u0102\u0103\b\25\1\2\u0103\u0104\5*\26\2\u0104")
        buf.write("\u010a\3\2\2\2\u0105\u0106\f\4\2\2\u0106\u0107\t\6\2\2")
        buf.write("\u0107\u0109\5*\26\2\u0108\u0105\3\2\2\2\u0109\u010c\3")
        buf.write("\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b)")
        buf.write("\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010e\b\26\1\2\u010e")
        buf.write("\u010f\5,\27\2\u010f\u0115\3\2\2\2\u0110\u0111\f\4\2\2")
        buf.write("\u0111\u0112\t\7\2\2\u0112\u0114\5,\27\2\u0113\u0110\3")
        buf.write("\2\2\2\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116")
        buf.write("\3\2\2\2\u0116+\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119")
        buf.write("\7\33\2\2\u0119\u011c\5,\27\2\u011a\u011c\5.\30\2\u011b")
        buf.write("\u0118\3\2\2\2\u011b\u011a\3\2\2\2\u011c-\3\2\2\2\u011d")
        buf.write("\u011e\7\36\2\2\u011e\u0121\5.\30\2\u011f\u0121\5\60\31")
        buf.write("\2\u0120\u011d\3\2\2\2\u0120\u011f\3\2\2\2\u0121/\3\2")
        buf.write("\2\2\u0122\u0123\7\3\2\2\u0123\u0124\5$\23\2\u0124\u0125")
        buf.write("\7\5\2\2\u0125\u012d\3\2\2\2\u0126\u012d\7%\2\2\u0127")
        buf.write("\u012d\7!\2\2\u0128\u012d\7\"\2\2\u0129\u012d\7#\2\2\u012a")
        buf.write("\u012d\7$\2\2\u012b\u012d\5\20\t\2\u012c\u0122\3\2\2\2")
        buf.write("\u012c\u0126\3\2\2\2\u012c\u0127\3\2\2\2\u012c\u0128\3")
        buf.write("\2\2\2\u012c\u0129\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012b")
        buf.write("\3\2\2\2\u012d\61\3\2\2\2\35\65DGMRZ_hjq\u0082\u0091\u009a")
        buf.write("\u009d\u00a3\u00af\u00bd\u00ca\u00dc\u00e4\u00f4\u00ff")
        buf.write("\u010a\u0115\u011b\u0120\u012c")
        return buf.getvalue()


class simplifiedJavaGrammarParser ( Parser ):

    grammarFileName = "simplifiedJavaGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "':'", "'end'", "'main'", 
                     "'var'", "';'", "'const'", "'='", "'while'", "'break;'", 
                     "'print'", "'scanf'", "'return'", "'if'", "'else'", 
                     "'>='", "'<='", "'>'", "'<'", "'=='", "'!='", "'+'", 
                     "'-'", "'*'", "'/'", "'!'", "<INVALID>", "'void'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TYPE", "VOID", "INT", "FLOAT", "STRING", 
                      "BOOLEAN", "ID", "WS", "CommentInOneLine", "CommentOnMultipleLines" ]

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
    RULE_breakCommand = 10
    RULE_printCommand = 11
    RULE_scanfCommand = 12
    RULE_returnCommand = 13
    RULE_ifBlock = 14
    RULE_elseBlock = 15
    RULE_assigmentCommand = 16
    RULE_expression = 17
    RULE_term = 18
    RULE_term2 = 19
    RULE_term3 = 20
    RULE_term4 = 21
    RULE_term5 = 22
    RULE_factor = 23

    ruleNames =  [ "program", "functionDeclarationArea", "main", "variablesDeclarationArea", 
                   "variablesDeclaration", "constantsDeclaration", "commands", 
                   "callFunctionCommand", "ifCommand", "whileCommand", "breakCommand", 
                   "printCommand", "scanfCommand", "returnCommand", "ifBlock", 
                   "elseBlock", "assigmentCommand", "expression", "term", 
                   "term2", "term3", "term4", "term5", "factor" ]

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
    TYPE=29
    VOID=30
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
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.MainContext,0)


        def EOF(self):
            return self.getToken(simplifiedJavaGrammarParser.EOF, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = simplifiedJavaGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==simplifiedJavaGrammarParser.ID:
                self.state = 48
                self.functionDeclarationArea()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.main()
            self.state = 55
            self.match(simplifiedJavaGrammarParser.EOF)
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

        def VOID(self):
            return self.getToken(simplifiedJavaGrammarParser.VOID, 0)

        def variablesDeclarationArea(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.VariablesDeclarationAreaContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclarationArea" ):
                return visitor.visitFunctionDeclarationArea(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclarationArea(self):

        localctx = simplifiedJavaGrammarParser.FunctionDeclarationAreaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDeclarationArea)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(simplifiedJavaGrammarParser.ID)
            self.state = 58
            self.match(simplifiedJavaGrammarParser.T__0)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==simplifiedJavaGrammarParser.TYPE:
                self.state = 59
                self.match(simplifiedJavaGrammarParser.TYPE)
                self.state = 60
                self.match(simplifiedJavaGrammarParser.ID)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==simplifiedJavaGrammarParser.T__1:
                    self.state = 61
                    self.match(simplifiedJavaGrammarParser.T__1)
                    self.state = 62
                    self.match(simplifiedJavaGrammarParser.TYPE)
                    self.state = 63
                    self.match(simplifiedJavaGrammarParser.ID)
                    self.state = 68
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 71
            self.match(simplifiedJavaGrammarParser.T__2)
            self.state = 72
            self.match(simplifiedJavaGrammarParser.T__3)
            self.state = 73
            _la = self._input.LA(1)
            if not(_la==simplifiedJavaGrammarParser.TYPE or _la==simplifiedJavaGrammarParser.VOID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==simplifiedJavaGrammarParser.T__6:
                self.state = 74
                self.variablesDeclarationArea()


            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << simplifiedJavaGrammarParser.T__10) | (1 << simplifiedJavaGrammarParser.T__11) | (1 << simplifiedJavaGrammarParser.T__12) | (1 << simplifiedJavaGrammarParser.T__13) | (1 << simplifiedJavaGrammarParser.T__14) | (1 << simplifiedJavaGrammarParser.T__15) | (1 << simplifiedJavaGrammarParser.ID))) != 0):
                self.state = 77
                self.commands()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
            self.match(simplifiedJavaGrammarParser.T__4)
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

        def variablesDeclarationArea(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.VariablesDeclarationAreaContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = simplifiedJavaGrammarParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(simplifiedJavaGrammarParser.T__5)
            self.state = 86
            self.match(simplifiedJavaGrammarParser.T__3)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==simplifiedJavaGrammarParser.T__6:
                self.state = 87
                self.variablesDeclarationArea()


            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << simplifiedJavaGrammarParser.T__10) | (1 << simplifiedJavaGrammarParser.T__11) | (1 << simplifiedJavaGrammarParser.T__12) | (1 << simplifiedJavaGrammarParser.T__13) | (1 << simplifiedJavaGrammarParser.T__14) | (1 << simplifiedJavaGrammarParser.T__15) | (1 << simplifiedJavaGrammarParser.ID))) != 0):
                self.state = 90
                self.commands()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(simplifiedJavaGrammarParser.T__4)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariablesDeclarationArea" ):
                return visitor.visitVariablesDeclarationArea(self)
            else:
                return visitor.visitChildren(self)




    def variablesDeclarationArea(self):

        localctx = simplifiedJavaGrammarParser.VariablesDeclarationAreaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variablesDeclarationArea)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(simplifiedJavaGrammarParser.T__6)
            self.state = 99
            self.match(simplifiedJavaGrammarParser.T__3)
            self.state = 102 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 102
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [simplifiedJavaGrammarParser.ID]:
                        self.state = 100
                        self.variablesDeclaration()
                        pass
                    elif token in [simplifiedJavaGrammarParser.T__8]:
                        self.state = 101
                        self.constantsDeclaration()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 104 
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariablesDeclaration" ):
                return visitor.visitVariablesDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variablesDeclaration(self):

        localctx = simplifiedJavaGrammarParser.VariablesDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variablesDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(simplifiedJavaGrammarParser.ID)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==simplifiedJavaGrammarParser.T__1:
                self.state = 107
                self.match(simplifiedJavaGrammarParser.T__1)
                self.state = 108
                self.match(simplifiedJavaGrammarParser.ID)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(simplifiedJavaGrammarParser.T__3)
            self.state = 115
            self.match(simplifiedJavaGrammarParser.TYPE)
            self.state = 116
            self.match(simplifiedJavaGrammarParser.T__7)
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
            self.terminal = []

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantsDeclaration" ):
                return visitor.visitConstantsDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def constantsDeclaration(self):

        localctx = simplifiedJavaGrammarParser.ConstantsDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constantsDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(simplifiedJavaGrammarParser.T__8)
            self.state = 119
            self.match(simplifiedJavaGrammarParser.ID)
            self.state = 120
            self.match(simplifiedJavaGrammarParser.T__9)
            self.state = 121
            localctx.terminal.append(self._input.LT(1))
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << simplifiedJavaGrammarParser.INT) | (1 << simplifiedJavaGrammarParser.FLOAT) | (1 << simplifiedJavaGrammarParser.STRING) | (1 << simplifiedJavaGrammarParser.BOOLEAN))) != 0)):
                localctx.terminal.append(self._errHandler.recoverInline(self))
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==simplifiedJavaGrammarParser.T__1:
                self.state = 122
                self.match(simplifiedJavaGrammarParser.T__1)
                self.state = 123
                self.match(simplifiedJavaGrammarParser.ID)
                self.state = 124
                self.match(simplifiedJavaGrammarParser.T__9)
                self.state = 125
                localctx.terminal.append(self._input.LT(1))
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << simplifiedJavaGrammarParser.INT) | (1 << simplifiedJavaGrammarParser.FLOAT) | (1 << simplifiedJavaGrammarParser.STRING) | (1 << simplifiedJavaGrammarParser.BOOLEAN))) != 0)):
                    localctx.terminal.append(self._errHandler.recoverInline(self))
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(simplifiedJavaGrammarParser.T__7)
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


        def breakCommand(self):
            return self.getTypedRuleContext(simplifiedJavaGrammarParser.BreakCommandContext,0)


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_commands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommands" ):
                listener.enterCommands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommands" ):
                listener.exitCommands(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommands" ):
                return visitor.visitCommands(self)
            else:
                return visitor.visitChildren(self)




    def commands(self):

        localctx = simplifiedJavaGrammarParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_commands)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.ifCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.whileCommand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.assigmentCommand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.callFunctionCommand()
                self.state = 137
                self.match(simplifiedJavaGrammarParser.T__7)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 139
                self.printCommand()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 140
                self.scanfCommand()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 141
                self.returnCommand()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 142
                self.breakCommand()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallFunctionCommand" ):
                return visitor.visitCallFunctionCommand(self)
            else:
                return visitor.visitChildren(self)




    def callFunctionCommand(self):

        localctx = simplifiedJavaGrammarParser.CallFunctionCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_callFunctionCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(simplifiedJavaGrammarParser.ID)
            self.state = 146
            self.match(simplifiedJavaGrammarParser.T__0)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << simplifiedJavaGrammarParser.T__0) | (1 << simplifiedJavaGrammarParser.T__24) | (1 << simplifiedJavaGrammarParser.T__27) | (1 << simplifiedJavaGrammarParser.INT) | (1 << simplifiedJavaGrammarParser.FLOAT) | (1 << simplifiedJavaGrammarParser.STRING) | (1 << simplifiedJavaGrammarParser.BOOLEAN) | (1 << simplifiedJavaGrammarParser.ID))) != 0):
                self.state = 147
                self.expression(0)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==simplifiedJavaGrammarParser.T__1:
                    self.state = 148
                    self.match(simplifiedJavaGrammarParser.T__1)
                    self.state = 149
                    self.expression(0)
                    self.state = 154
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 157
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfCommand" ):
                return visitor.visitIfCommand(self)
            else:
                return visitor.visitChildren(self)




    def ifCommand(self):

        localctx = simplifiedJavaGrammarParser.IfCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.ifBlock()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==simplifiedJavaGrammarParser.T__16:
                self.state = 160
                self.elseBlock()


            self.state = 163
            self.match(simplifiedJavaGrammarParser.T__4)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileCommand" ):
                return visitor.visitWhileCommand(self)
            else:
                return visitor.visitChildren(self)




    def whileCommand(self):

        localctx = simplifiedJavaGrammarParser.WhileCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(simplifiedJavaGrammarParser.T__10)
            self.state = 166
            self.match(simplifiedJavaGrammarParser.T__0)
            self.state = 167
            self.expression(0)
            self.state = 168
            self.match(simplifiedJavaGrammarParser.T__2)
            self.state = 169
            self.match(simplifiedJavaGrammarParser.T__3)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << simplifiedJavaGrammarParser.T__10) | (1 << simplifiedJavaGrammarParser.T__11) | (1 << simplifiedJavaGrammarParser.T__12) | (1 << simplifiedJavaGrammarParser.T__13) | (1 << simplifiedJavaGrammarParser.T__14) | (1 << simplifiedJavaGrammarParser.T__15) | (1 << simplifiedJavaGrammarParser.ID))) != 0):
                self.state = 170
                self.commands()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self.match(simplifiedJavaGrammarParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_breakCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakCommand" ):
                listener.enterBreakCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakCommand" ):
                listener.exitBreakCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakCommand" ):
                return visitor.visitBreakCommand(self)
            else:
                return visitor.visitChildren(self)




    def breakCommand(self):

        localctx = simplifiedJavaGrammarParser.BreakCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_breakCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(simplifiedJavaGrammarParser.T__11)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintCommand" ):
                return visitor.visitPrintCommand(self)
            else:
                return visitor.visitChildren(self)




    def printCommand(self):

        localctx = simplifiedJavaGrammarParser.PrintCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_printCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(simplifiedJavaGrammarParser.T__12)
            self.state = 181
            self.match(simplifiedJavaGrammarParser.T__0)
            self.state = 182
            self.expression(0)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==simplifiedJavaGrammarParser.T__1:
                self.state = 183
                self.match(simplifiedJavaGrammarParser.T__1)
                self.state = 184
                self.expression(0)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 190
            self.match(simplifiedJavaGrammarParser.T__2)
            self.state = 191
            self.match(simplifiedJavaGrammarParser.T__7)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScanfCommand" ):
                return visitor.visitScanfCommand(self)
            else:
                return visitor.visitChildren(self)




    def scanfCommand(self):

        localctx = simplifiedJavaGrammarParser.ScanfCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_scanfCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(simplifiedJavaGrammarParser.T__13)
            self.state = 194
            self.match(simplifiedJavaGrammarParser.T__0)
            self.state = 195
            self.match(simplifiedJavaGrammarParser.ID)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==simplifiedJavaGrammarParser.T__1:
                self.state = 196
                self.match(simplifiedJavaGrammarParser.T__1)
                self.state = 197
                self.match(simplifiedJavaGrammarParser.ID)
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
            self.match(simplifiedJavaGrammarParser.T__2)
            self.state = 204
            self.match(simplifiedJavaGrammarParser.T__7)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnCommand" ):
                return visitor.visitReturnCommand(self)
            else:
                return visitor.visitChildren(self)




    def returnCommand(self):

        localctx = simplifiedJavaGrammarParser.ReturnCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_returnCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(simplifiedJavaGrammarParser.T__14)
            self.state = 207
            self.expression(0)
            self.state = 208
            self.match(simplifiedJavaGrammarParser.T__7)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlock" ):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)




    def ifBlock(self):

        localctx = simplifiedJavaGrammarParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(simplifiedJavaGrammarParser.T__15)
            self.state = 211
            self.match(simplifiedJavaGrammarParser.T__0)
            self.state = 212
            self.expression(0)
            self.state = 213
            self.match(simplifiedJavaGrammarParser.T__2)
            self.state = 214
            self.match(simplifiedJavaGrammarParser.T__3)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << simplifiedJavaGrammarParser.T__10) | (1 << simplifiedJavaGrammarParser.T__11) | (1 << simplifiedJavaGrammarParser.T__12) | (1 << simplifiedJavaGrammarParser.T__13) | (1 << simplifiedJavaGrammarParser.T__14) | (1 << simplifiedJavaGrammarParser.T__15) | (1 << simplifiedJavaGrammarParser.ID))) != 0):
                self.state = 215
                self.commands()
                self.state = 220
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseBlock" ):
                return visitor.visitElseBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseBlock(self):

        localctx = simplifiedJavaGrammarParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_elseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(simplifiedJavaGrammarParser.T__16)
            self.state = 222
            self.match(simplifiedJavaGrammarParser.T__3)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << simplifiedJavaGrammarParser.T__10) | (1 << simplifiedJavaGrammarParser.T__11) | (1 << simplifiedJavaGrammarParser.T__12) | (1 << simplifiedJavaGrammarParser.T__13) | (1 << simplifiedJavaGrammarParser.T__14) | (1 << simplifiedJavaGrammarParser.T__15) | (1 << simplifiedJavaGrammarParser.ID))) != 0):
                self.state = 223
                self.commands()
                self.state = 228
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssigmentCommand" ):
                return visitor.visitAssigmentCommand(self)
            else:
                return visitor.visitChildren(self)




    def assigmentCommand(self):

        localctx = simplifiedJavaGrammarParser.AssigmentCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assigmentCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(simplifiedJavaGrammarParser.ID)
            self.state = 230
            self.match(simplifiedJavaGrammarParser.T__9)
            self.state = 231
            self.expression(0)
            self.state = 232
            self.match(simplifiedJavaGrammarParser.T__7)
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
            self.type = None
            self.inhType = None


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type = ctx.type
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoTerm" ):
                return visitor.visitGoTerm(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparativeOperation" ):
                return visitor.visitComparativeOperation(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = simplifiedJavaGrammarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = simplifiedJavaGrammarParser.GoTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 235
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = simplifiedJavaGrammarParser.ComparativeOperationContext(self, simplifiedJavaGrammarParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 237
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 238
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << simplifiedJavaGrammarParser.T__17) | (1 << simplifiedJavaGrammarParser.T__18) | (1 << simplifiedJavaGrammarParser.T__19) | (1 << simplifiedJavaGrammarParser.T__20))) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 239
                    self.term(0) 
                self.state = 244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
            self.type = None


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type = ctx.type


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGotTerm2" ):
                return visitor.visitGotTerm2(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualDiffOperation" ):
                return visitor.visitEqualDiffOperation(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = simplifiedJavaGrammarParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = simplifiedJavaGrammarParser.GotTerm2Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 246
            self.term2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = simplifiedJavaGrammarParser.EqualDiffOperationContext(self, simplifiedJavaGrammarParser.TermContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 248
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 249
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==simplifiedJavaGrammarParser.T__21 or _la==simplifiedJavaGrammarParser.T__22):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 250
                    self.term2(0) 
                self.state = 255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
            self.type = None


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_term2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type = ctx.type


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlusMinusOperation" ):
                return visitor.visitPlusMinusOperation(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoTerm3" ):
                return visitor.visitGoTerm3(self)
            else:
                return visitor.visitChildren(self)



    def term2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = simplifiedJavaGrammarParser.Term2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_term2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = simplifiedJavaGrammarParser.GoTerm3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 257
            self.term3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 264
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = simplifiedJavaGrammarParser.PlusMinusOperationContext(self, simplifiedJavaGrammarParser.Term2Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term2)
                    self.state = 259
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 260
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==simplifiedJavaGrammarParser.T__23 or _la==simplifiedJavaGrammarParser.T__24):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 261
                    self.term3(0) 
                self.state = 266
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
            self.type = None


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_term3

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type = ctx.type


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultDivOperation" ):
                return visitor.visitMultDivOperation(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoTerm4" ):
                return visitor.visitGoTerm4(self)
            else:
                return visitor.visitChildren(self)



    def term3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = simplifiedJavaGrammarParser.Term3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_term3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = simplifiedJavaGrammarParser.GoTerm4Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 268
            self.term4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = simplifiedJavaGrammarParser.MultDivOperationContext(self, simplifiedJavaGrammarParser.Term3Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term3)
                    self.state = 270
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 271
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==simplifiedJavaGrammarParser.T__25 or _la==simplifiedJavaGrammarParser.T__26):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 272
                    self.term4() 
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
            self.type = None


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_term4

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type = ctx.type



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoTerm5" ):
                return visitor.visitGoTerm5(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusOperation" ):
                return visitor.visitUnaryMinusOperation(self)
            else:
                return visitor.visitChildren(self)



    def term4(self):

        localctx = simplifiedJavaGrammarParser.Term4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_term4)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [simplifiedJavaGrammarParser.T__24]:
                localctx = simplifiedJavaGrammarParser.UnaryMinusOperationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(simplifiedJavaGrammarParser.T__24)
                self.state = 279
                self.term4()
                pass
            elif token in [simplifiedJavaGrammarParser.T__0, simplifiedJavaGrammarParser.T__27, simplifiedJavaGrammarParser.INT, simplifiedJavaGrammarParser.FLOAT, simplifiedJavaGrammarParser.STRING, simplifiedJavaGrammarParser.BOOLEAN, simplifiedJavaGrammarParser.ID]:
                localctx = simplifiedJavaGrammarParser.GoTerm5Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 280
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
            self.type = None


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_term5

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type = ctx.type



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoFactor" ):
                return visitor.visitGoFactor(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotOperation" ):
                return visitor.visitNotOperation(self)
            else:
                return visitor.visitChildren(self)



    def term5(self):

        localctx = simplifiedJavaGrammarParser.Term5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_term5)
        try:
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [simplifiedJavaGrammarParser.T__27]:
                localctx = simplifiedJavaGrammarParser.NotOperationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(simplifiedJavaGrammarParser.T__27)
                self.state = 284
                self.term5()
                pass
            elif token in [simplifiedJavaGrammarParser.T__0, simplifiedJavaGrammarParser.INT, simplifiedJavaGrammarParser.FLOAT, simplifiedJavaGrammarParser.STRING, simplifiedJavaGrammarParser.BOOLEAN, simplifiedJavaGrammarParser.ID]:
                localctx = simplifiedJavaGrammarParser.GoFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 285
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
            self.type = None


        def getRuleIndex(self):
            return simplifiedJavaGrammarParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type = ctx.type



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolTerminal" ):
                return visitor.visitBoolTerminal(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallFunctionTerminal" ):
                return visitor.visitCallFunctionTerminal(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpenCloseParantesisTerminal" ):
                return visitor.visitOpenCloseParantesisTerminal(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdTerminal" ):
                return visitor.visitIdTerminal(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntTerminal" ):
                return visitor.visitIntTerminal(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatTerminal" ):
                return visitor.visitFloatTerminal(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringTerminal" ):
                return visitor.visitStringTerminal(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = simplifiedJavaGrammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_factor)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                localctx = simplifiedJavaGrammarParser.OpenCloseParantesisTerminalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.match(simplifiedJavaGrammarParser.T__0)
                self.state = 289
                self.expression(0)
                self.state = 290
                self.match(simplifiedJavaGrammarParser.T__2)
                pass

            elif la_ == 2:
                localctx = simplifiedJavaGrammarParser.IdTerminalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.match(simplifiedJavaGrammarParser.ID)
                pass

            elif la_ == 3:
                localctx = simplifiedJavaGrammarParser.IntTerminalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 293
                self.match(simplifiedJavaGrammarParser.INT)
                pass

            elif la_ == 4:
                localctx = simplifiedJavaGrammarParser.FloatTerminalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 294
                self.match(simplifiedJavaGrammarParser.FLOAT)
                pass

            elif la_ == 5:
                localctx = simplifiedJavaGrammarParser.StringTerminalContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 295
                self.match(simplifiedJavaGrammarParser.STRING)
                pass

            elif la_ == 6:
                localctx = simplifiedJavaGrammarParser.BoolTerminalContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 296
                self.match(simplifiedJavaGrammarParser.BOOLEAN)
                pass

            elif la_ == 7:
                localctx = simplifiedJavaGrammarParser.CallFunctionTerminalContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 297
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
        self._predicates[17] = self.expression_sempred
        self._predicates[18] = self.term_sempred
        self._predicates[19] = self.term2_sempred
        self._predicates[20] = self.term3_sempred
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
         




