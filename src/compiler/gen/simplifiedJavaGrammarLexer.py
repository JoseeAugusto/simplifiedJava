# Generated from c:\Users\cassi\Documents\dev\uni\compilers\simple-java-compiler\simple-java\simplifiedJavaGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2(")
        buf.write("\u0113\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u00c0\n")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\3 \6 \u00c8\n \r \16 \u00c9")
        buf.write("\3!\6!\u00cd\n!\r!\16!\u00ce\3!\3!\6!\u00d3\n!\r!\16!")
        buf.write("\u00d4\3\"\3\"\7\"\u00d9\n\"\f\"\16\"\u00dc\13\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u00e9\n#\3$\3$\7$\u00ed")
        buf.write("\n$\f$\16$\u00f0\13$\3%\6%\u00f3\n%\r%\16%\u00f4\3%\3")
        buf.write("%\3&\3&\3&\3&\7&\u00fd\n&\f&\16&\u0100\13&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\7\'\u010a\n\'\f\'\16\'\u010d\13\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\4\u00fe\u010b\2(\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(\3\2\b\3\2\62;\3\2\60")
        buf.write("\60\3\2$$\4\2C\\c|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2")
        buf.write("\u011e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\3O\3\2\2\2\5Q\3\2\2\2\7S")
        buf.write("\3\2\2\2\tU\3\2\2\2\13W\3\2\2\2\r[\3\2\2\2\17`\3\2\2\2")
        buf.write("\21d\3\2\2\2\23f\3\2\2\2\25l\3\2\2\2\27n\3\2\2\2\31t\3")
        buf.write("\2\2\2\33{\3\2\2\2\35\u0081\3\2\2\2\37\u0087\3\2\2\2!")
        buf.write("\u008e\3\2\2\2#\u0091\3\2\2\2%\u0096\3\2\2\2\'\u0099\3")
        buf.write("\2\2\2)\u009c\3\2\2\2+\u009e\3\2\2\2-\u00a0\3\2\2\2/\u00a3")
        buf.write("\3\2\2\2\61\u00a6\3\2\2\2\63\u00a8\3\2\2\2\65\u00aa\3")
        buf.write("\2\2\2\67\u00ac\3\2\2\29\u00ae\3\2\2\2;\u00bf\3\2\2\2")
        buf.write("=\u00c1\3\2\2\2?\u00c7\3\2\2\2A\u00cc\3\2\2\2C\u00d6\3")
        buf.write("\2\2\2E\u00e8\3\2\2\2G\u00ea\3\2\2\2I\u00f2\3\2\2\2K\u00f8")
        buf.write("\3\2\2\2M\u0105\3\2\2\2OP\7*\2\2P\4\3\2\2\2QR\7.\2\2R")
        buf.write("\6\3\2\2\2ST\7+\2\2T\b\3\2\2\2UV\7<\2\2V\n\3\2\2\2WX\7")
        buf.write("g\2\2XY\7p\2\2YZ\7f\2\2Z\f\3\2\2\2[\\\7o\2\2\\]\7c\2\2")
        buf.write("]^\7k\2\2^_\7p\2\2_\16\3\2\2\2`a\7x\2\2ab\7c\2\2bc\7t")
        buf.write("\2\2c\20\3\2\2\2de\7=\2\2e\22\3\2\2\2fg\7e\2\2gh\7q\2")
        buf.write("\2hi\7p\2\2ij\7u\2\2jk\7v\2\2k\24\3\2\2\2lm\7?\2\2m\26")
        buf.write("\3\2\2\2no\7y\2\2op\7j\2\2pq\7k\2\2qr\7n\2\2rs\7g\2\2")
        buf.write("s\30\3\2\2\2tu\7d\2\2uv\7t\2\2vw\7g\2\2wx\7c\2\2xy\7m")
        buf.write("\2\2yz\7=\2\2z\32\3\2\2\2{|\7r\2\2|}\7t\2\2}~\7k\2\2~")
        buf.write("\177\7p\2\2\177\u0080\7v\2\2\u0080\34\3\2\2\2\u0081\u0082")
        buf.write("\7u\2\2\u0082\u0083\7e\2\2\u0083\u0084\7c\2\2\u0084\u0085")
        buf.write("\7p\2\2\u0085\u0086\7h\2\2\u0086\36\3\2\2\2\u0087\u0088")
        buf.write("\7t\2\2\u0088\u0089\7g\2\2\u0089\u008a\7v\2\2\u008a\u008b")
        buf.write("\7w\2\2\u008b\u008c\7t\2\2\u008c\u008d\7p\2\2\u008d \3")
        buf.write("\2\2\2\u008e\u008f\7k\2\2\u008f\u0090\7h\2\2\u0090\"\3")
        buf.write("\2\2\2\u0091\u0092\7g\2\2\u0092\u0093\7n\2\2\u0093\u0094")
        buf.write("\7u\2\2\u0094\u0095\7g\2\2\u0095$\3\2\2\2\u0096\u0097")
        buf.write("\7@\2\2\u0097\u0098\7?\2\2\u0098&\3\2\2\2\u0099\u009a")
        buf.write("\7>\2\2\u009a\u009b\7?\2\2\u009b(\3\2\2\2\u009c\u009d")
        buf.write("\7@\2\2\u009d*\3\2\2\2\u009e\u009f\7>\2\2\u009f,\3\2\2")
        buf.write("\2\u00a0\u00a1\7?\2\2\u00a1\u00a2\7?\2\2\u00a2.\3\2\2")
        buf.write("\2\u00a3\u00a4\7#\2\2\u00a4\u00a5\7?\2\2\u00a5\60\3\2")
        buf.write("\2\2\u00a6\u00a7\7-\2\2\u00a7\62\3\2\2\2\u00a8\u00a9\7")
        buf.write("/\2\2\u00a9\64\3\2\2\2\u00aa\u00ab\7,\2\2\u00ab\66\3\2")
        buf.write("\2\2\u00ac\u00ad\7\61\2\2\u00ad8\3\2\2\2\u00ae\u00af\7")
        buf.write("#\2\2\u00af:\3\2\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2\7")
        buf.write("p\2\2\u00b2\u00c0\7v\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5")
        buf.write("\7v\2\2\u00b5\u00c0\7t\2\2\u00b6\u00b7\7h\2\2\u00b7\u00b8")
        buf.write("\7n\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7c\2\2\u00ba\u00c0")
        buf.write("\7v\2\2\u00bb\u00bc\7d\2\2\u00bc\u00bd\7q\2\2\u00bd\u00be")
        buf.write("\7q\2\2\u00be\u00c0\7n\2\2\u00bf\u00b0\3\2\2\2\u00bf\u00b3")
        buf.write("\3\2\2\2\u00bf\u00b6\3\2\2\2\u00bf\u00bb\3\2\2\2\u00c0")
        buf.write("<\3\2\2\2\u00c1\u00c2\7x\2\2\u00c2\u00c3\7q\2\2\u00c3")
        buf.write("\u00c4\7k\2\2\u00c4\u00c5\7f\2\2\u00c5>\3\2\2\2\u00c6")
        buf.write("\u00c8\t\2\2\2\u00c7\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2")
        buf.write("\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca@\3\2\2")
        buf.write("\2\u00cb\u00cd\t\2\2\2\u00cc\u00cb\3\2\2\2\u00cd\u00ce")
        buf.write("\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00d2\t\3\2\2\u00d1\u00d3\t\2\2\2")
        buf.write("\u00d2\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d2\3")
        buf.write("\2\2\2\u00d4\u00d5\3\2\2\2\u00d5B\3\2\2\2\u00d6\u00da")
        buf.write("\t\4\2\2\u00d7\u00d9\n\4\2\2\u00d8\u00d7\3\2\2\2\u00d9")
        buf.write("\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2")
        buf.write("\u00db\u00dd\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00de\t")
        buf.write("\4\2\2\u00deD\3\2\2\2\u00df\u00e0\7V\2\2\u00e0\u00e1\7")
        buf.write("t\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e9\7g\2\2\u00e3\u00e4")
        buf.write("\7H\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7")
        buf.write("\7u\2\2\u00e7\u00e9\7g\2\2\u00e8\u00df\3\2\2\2\u00e8\u00e3")
        buf.write("\3\2\2\2\u00e9F\3\2\2\2\u00ea\u00ee\t\5\2\2\u00eb\u00ed")
        buf.write("\t\6\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee")
        buf.write("\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00efH\3\2\2\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f1\u00f3\t\7\2\2\u00f2\u00f1\3\2\2\2")
        buf.write("\u00f3\u00f4\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3")
        buf.write("\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\b%\2\2\u00f7J\3")
        buf.write("\2\2\2\u00f8\u00f9\7\61\2\2\u00f9\u00fa\7\61\2\2\u00fa")
        buf.write("\u00fe\3\2\2\2\u00fb\u00fd\13\2\2\2\u00fc\u00fb\3\2\2")
        buf.write("\2\u00fd\u0100\3\2\2\2\u00fe\u00ff\3\2\2\2\u00fe\u00fc")
        buf.write("\3\2\2\2\u00ff\u0101\3\2\2\2\u0100\u00fe\3\2\2\2\u0101")
        buf.write("\u0102\7\f\2\2\u0102\u0103\3\2\2\2\u0103\u0104\b&\2\2")
        buf.write("\u0104L\3\2\2\2\u0105\u0106\7\61\2\2\u0106\u0107\7,\2")
        buf.write("\2\u0107\u010b\3\2\2\2\u0108\u010a\13\2\2\2\u0109\u0108")
        buf.write("\3\2\2\2\u010a\u010d\3\2\2\2\u010b\u010c\3\2\2\2\u010b")
        buf.write("\u0109\3\2\2\2\u010c\u010e\3\2\2\2\u010d\u010b\3\2\2\2")
        buf.write("\u010e\u010f\7,\2\2\u010f\u0110\7\61\2\2\u0110\u0111\3")
        buf.write("\2\2\2\u0111\u0112\b\'\2\2\u0112N\3\2\2\2\r\2\u00bf\u00c9")
        buf.write("\u00ce\u00d4\u00da\u00e8\u00ee\u00f4\u00fe\u010b\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class simplifiedJavaGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    TYPE = 29
    VOID = 30
    INT = 31
    FLOAT = 32
    STRING = 33
    BOOLEAN = 34
    ID = 35
    WS = 36
    CommentInOneLine = 37
    CommentOnMultipleLines = 38

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "','", "')'", "':'", "'end'", "'main'", "'var'", "';'", 
            "'const'", "'='", "'while'", "'break;'", "'print'", "'scanf'", 
            "'return'", "'if'", "'else'", "'>='", "'<='", "'>'", "'<'", 
            "'=='", "'!='", "'+'", "'-'", "'*'", "'/'", "'!'", "'void'" ]

    symbolicNames = [ "<INVALID>",
            "TYPE", "VOID", "INT", "FLOAT", "STRING", "BOOLEAN", "ID", "WS", 
            "CommentInOneLine", "CommentOnMultipleLines" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "TYPE", "VOID", "INT", "FLOAT", "STRING", 
                  "BOOLEAN", "ID", "WS", "CommentInOneLine", "CommentOnMultipleLines" ]

    grammarFileName = "simplifiedJavaGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


