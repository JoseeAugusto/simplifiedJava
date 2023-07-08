// Generated from c:\Users\jose1\Documents\UFPI\6º período\Compiladores\trabFinal\javaSimplificado\simplifiedJavaGrammar.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class simplifiedJavaGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, TYPE=30, INT=31, FLOAT=32, 
		STRING=33, BOOLEAN=34, ID=35, WS=36, CommentInOneLine=37, CommentOnMultipleLines=38;
	public static final int
		RULE_program = 0, RULE_functionDeclarationArea = 1, RULE_main = 2, RULE_variablesDeclarationArea = 3, 
		RULE_variablesDeclaration = 4, RULE_constantsDeclaration = 5, RULE_commands = 6, 
		RULE_callFunctionCommand = 7, RULE_ifCommand = 8, RULE_whileCommand = 9, 
		RULE_printCommand = 10, RULE_scanfCommand = 11, RULE_returnCommand = 12, 
		RULE_ifBlock = 13, RULE_elseBlock = 14, RULE_assigmentCommand = 15, RULE_expression = 16, 
		RULE_term = 17, RULE_term2 = 18, RULE_term3 = 19, RULE_term4 = 20, RULE_term5 = 21, 
		RULE_factor = 22;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "functionDeclarationArea", "main", "variablesDeclarationArea", 
			"variablesDeclaration", "constantsDeclaration", "commands", "callFunctionCommand", 
			"ifCommand", "whileCommand", "printCommand", "scanfCommand", "returnCommand", 
			"ifBlock", "elseBlock", "assigmentCommand", "expression", "term", "term2", 
			"term3", "term4", "term5", "factor"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "','", "')'", "':'", "'void'", "'end'", "'main'", "'var'", 
			"';'", "'const'", "'='", "'while'", "'break;'", "'print'", "'scanf'", 
			"'return'", "'if'", "'else'", "'>='", "'<='", "'>'", "'<'", "'=='", "'!='", 
			"'+'", "'-'", "'*'", "'/'", "'!'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "TYPE", "INT", "FLOAT", "STRING", 
			"BOOLEAN", "ID", "WS", "CommentInOneLine", "CommentOnMultipleLines"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "simplifiedJavaGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public simplifiedJavaGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public List<FunctionDeclarationAreaContext> functionDeclarationArea() {
			return getRuleContexts(FunctionDeclarationAreaContext.class);
		}
		public FunctionDeclarationAreaContext functionDeclarationArea(int i) {
			return getRuleContext(FunctionDeclarationAreaContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(46);
				functionDeclarationArea();
				}
				}
				setState(51);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(52);
			main();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionDeclarationAreaContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(simplifiedJavaGrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(simplifiedJavaGrammarParser.ID, i);
		}
		public List<TerminalNode> TYPE() { return getTokens(simplifiedJavaGrammarParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(simplifiedJavaGrammarParser.TYPE, i);
		}
		public List<VariablesDeclarationAreaContext> variablesDeclarationArea() {
			return getRuleContexts(VariablesDeclarationAreaContext.class);
		}
		public VariablesDeclarationAreaContext variablesDeclarationArea(int i) {
			return getRuleContext(VariablesDeclarationAreaContext.class,i);
		}
		public List<CommandsContext> commands() {
			return getRuleContexts(CommandsContext.class);
		}
		public CommandsContext commands(int i) {
			return getRuleContext(CommandsContext.class,i);
		}
		public FunctionDeclarationAreaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDeclarationArea; }
	}

	public final FunctionDeclarationAreaContext functionDeclarationArea() throws RecognitionException {
		FunctionDeclarationAreaContext _localctx = new FunctionDeclarationAreaContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_functionDeclarationArea);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(ID);
			setState(55);
			match(T__0);
			setState(66);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TYPE) {
				{
				setState(56);
				match(TYPE);
				setState(57);
				match(ID);
				setState(63);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(58);
					match(T__1);
					setState(59);
					match(TYPE);
					setState(60);
					match(ID);
					}
					}
					setState(65);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(68);
			match(T__2);
			setState(69);
			match(T__3);
			setState(70);
			_la = _input.LA(1);
			if ( !(_la==T__4 || _la==TYPE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__7) {
				{
				{
				setState(71);
				variablesDeclarationArea();
				}
				}
				setState(76);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(80);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__11) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << ID))) != 0)) {
				{
				{
				setState(77);
				commands();
				}
				}
				setState(82);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(83);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MainContext extends ParserRuleContext {
		public List<VariablesDeclarationAreaContext> variablesDeclarationArea() {
			return getRuleContexts(VariablesDeclarationAreaContext.class);
		}
		public VariablesDeclarationAreaContext variablesDeclarationArea(int i) {
			return getRuleContext(VariablesDeclarationAreaContext.class,i);
		}
		public List<CommandsContext> commands() {
			return getRuleContexts(CommandsContext.class);
		}
		public CommandsContext commands(int i) {
			return getRuleContext(CommandsContext.class,i);
		}
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_main);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(T__6);
			setState(86);
			match(T__3);
			setState(90);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__7) {
				{
				{
				setState(87);
				variablesDeclarationArea();
				}
				}
				setState(92);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(96);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__11) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << ID))) != 0)) {
				{
				{
				setState(93);
				commands();
				}
				}
				setState(98);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(99);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariablesDeclarationAreaContext extends ParserRuleContext {
		public List<VariablesDeclarationContext> variablesDeclaration() {
			return getRuleContexts(VariablesDeclarationContext.class);
		}
		public VariablesDeclarationContext variablesDeclaration(int i) {
			return getRuleContext(VariablesDeclarationContext.class,i);
		}
		public List<ConstantsDeclarationContext> constantsDeclaration() {
			return getRuleContexts(ConstantsDeclarationContext.class);
		}
		public ConstantsDeclarationContext constantsDeclaration(int i) {
			return getRuleContext(ConstantsDeclarationContext.class,i);
		}
		public VariablesDeclarationAreaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variablesDeclarationArea; }
	}

	public final VariablesDeclarationAreaContext variablesDeclarationArea() throws RecognitionException {
		VariablesDeclarationAreaContext _localctx = new VariablesDeclarationAreaContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_variablesDeclarationArea);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			match(T__7);
			setState(102);
			match(T__3);
			setState(105); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(105);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case ID:
						{
						setState(103);
						variablesDeclaration();
						}
						break;
					case T__9:
						{
						setState(104);
						constantsDeclaration();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(107); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariablesDeclarationContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(simplifiedJavaGrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(simplifiedJavaGrammarParser.ID, i);
		}
		public TerminalNode TYPE() { return getToken(simplifiedJavaGrammarParser.TYPE, 0); }
		public VariablesDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variablesDeclaration; }
	}

	public final VariablesDeclarationContext variablesDeclaration() throws RecognitionException {
		VariablesDeclarationContext _localctx = new VariablesDeclarationContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_variablesDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			match(ID);
			setState(114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(110);
				match(T__1);
				setState(111);
				match(ID);
				}
				}
				setState(116);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(117);
			match(T__3);
			setState(118);
			match(TYPE);
			setState(119);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstantsDeclarationContext extends ParserRuleContext {
		public Token terminal;
		public List<TerminalNode> ID() { return getTokens(simplifiedJavaGrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(simplifiedJavaGrammarParser.ID, i);
		}
		public List<TerminalNode> STRING() { return getTokens(simplifiedJavaGrammarParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(simplifiedJavaGrammarParser.STRING, i);
		}
		public List<TerminalNode> INT() { return getTokens(simplifiedJavaGrammarParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(simplifiedJavaGrammarParser.INT, i);
		}
		public List<TerminalNode> BOOLEAN() { return getTokens(simplifiedJavaGrammarParser.BOOLEAN); }
		public TerminalNode BOOLEAN(int i) {
			return getToken(simplifiedJavaGrammarParser.BOOLEAN, i);
		}
		public List<TerminalNode> FLOAT() { return getTokens(simplifiedJavaGrammarParser.FLOAT); }
		public TerminalNode FLOAT(int i) {
			return getToken(simplifiedJavaGrammarParser.FLOAT, i);
		}
		public ConstantsDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constantsDeclaration; }
	}

	public final ConstantsDeclarationContext constantsDeclaration() throws RecognitionException {
		ConstantsDeclarationContext _localctx = new ConstantsDeclarationContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_constantsDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			match(T__9);
			setState(122);
			match(ID);
			setState(123);
			match(T__10);
			setState(124);
			((ConstantsDeclarationContext)_localctx).terminal = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << FLOAT) | (1L << STRING) | (1L << BOOLEAN))) != 0)) ) {
				((ConstantsDeclarationContext)_localctx).terminal = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(131);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(125);
				match(T__1);
				setState(126);
				match(ID);
				setState(127);
				match(T__10);
				setState(128);
				((ConstantsDeclarationContext)_localctx).terminal = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << FLOAT) | (1L << STRING) | (1L << BOOLEAN))) != 0)) ) {
					((ConstantsDeclarationContext)_localctx).terminal = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(133);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(134);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CommandsContext extends ParserRuleContext {
		public IfCommandContext ifCommand() {
			return getRuleContext(IfCommandContext.class,0);
		}
		public WhileCommandContext whileCommand() {
			return getRuleContext(WhileCommandContext.class,0);
		}
		public AssigmentCommandContext assigmentCommand() {
			return getRuleContext(AssigmentCommandContext.class,0);
		}
		public CallFunctionCommandContext callFunctionCommand() {
			return getRuleContext(CallFunctionCommandContext.class,0);
		}
		public PrintCommandContext printCommand() {
			return getRuleContext(PrintCommandContext.class,0);
		}
		public ScanfCommandContext scanfCommand() {
			return getRuleContext(ScanfCommandContext.class,0);
		}
		public ReturnCommandContext returnCommand() {
			return getRuleContext(ReturnCommandContext.class,0);
		}
		public CommandsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_commands; }
	}

	public final CommandsContext commands() throws RecognitionException {
		CommandsContext _localctx = new CommandsContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_commands);
		try {
			setState(145);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(136);
				ifCommand();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(137);
				whileCommand();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(138);
				assigmentCommand();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(139);
				callFunctionCommand();
				setState(140);
				match(T__8);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(142);
				printCommand();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(143);
				scanfCommand();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(144);
				returnCommand();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CallFunctionCommandContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(simplifiedJavaGrammarParser.ID, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public CallFunctionCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_callFunctionCommand; }
	}

	public final CallFunctionCommandContext callFunctionCommand() throws RecognitionException {
		CallFunctionCommandContext _localctx = new CallFunctionCommandContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_callFunctionCommand);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			match(ID);
			setState(148);
			match(T__0);
			setState(157);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__25) | (1L << T__28) | (1L << INT) | (1L << FLOAT) | (1L << STRING) | (1L << BOOLEAN) | (1L << ID))) != 0)) {
				{
				setState(149);
				expression(0);
				setState(154);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(150);
					match(T__1);
					setState(151);
					expression(0);
					}
					}
					setState(156);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(159);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfCommandContext extends ParserRuleContext {
		public IfBlockContext ifBlock() {
			return getRuleContext(IfBlockContext.class,0);
		}
		public ElseBlockContext elseBlock() {
			return getRuleContext(ElseBlockContext.class,0);
		}
		public IfCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifCommand; }
	}

	public final IfCommandContext ifCommand() throws RecognitionException {
		IfCommandContext _localctx = new IfCommandContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_ifCommand);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			ifBlock();
			setState(163);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__17) {
				{
				setState(162);
				elseBlock();
				}
			}

			setState(165);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhileCommandContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<CommandsContext> commands() {
			return getRuleContexts(CommandsContext.class);
		}
		public CommandsContext commands(int i) {
			return getRuleContext(CommandsContext.class,i);
		}
		public WhileCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileCommand; }
	}

	public final WhileCommandContext whileCommand() throws RecognitionException {
		WhileCommandContext _localctx = new WhileCommandContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_whileCommand);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(T__11);
			setState(168);
			match(T__0);
			setState(169);
			expression(0);
			setState(170);
			match(T__2);
			setState(171);
			match(T__3);
			setState(175);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__11) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << ID))) != 0)) {
				{
				{
				setState(172);
				commands();
				}
				}
				setState(177);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(179);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(178);
				match(T__12);
				}
			}

			setState(181);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrintCommandContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public PrintCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printCommand; }
	}

	public final PrintCommandContext printCommand() throws RecognitionException {
		PrintCommandContext _localctx = new PrintCommandContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_printCommand);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(183);
			match(T__13);
			setState(184);
			match(T__0);
			setState(185);
			expression(0);
			setState(190);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(186);
				match(T__1);
				setState(187);
				expression(0);
				}
				}
				setState(192);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(193);
			match(T__2);
			setState(194);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ScanfCommandContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(simplifiedJavaGrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(simplifiedJavaGrammarParser.ID, i);
		}
		public ScanfCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scanfCommand; }
	}

	public final ScanfCommandContext scanfCommand() throws RecognitionException {
		ScanfCommandContext _localctx = new ScanfCommandContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_scanfCommand);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			match(T__14);
			setState(197);
			match(T__0);
			setState(198);
			match(ID);
			setState(203);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(199);
				match(T__1);
				setState(200);
				match(ID);
				}
				}
				setState(205);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(206);
			match(T__2);
			setState(207);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReturnCommandContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ReturnCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnCommand; }
	}

	public final ReturnCommandContext returnCommand() throws RecognitionException {
		ReturnCommandContext _localctx = new ReturnCommandContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_returnCommand);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			match(T__15);
			setState(210);
			expression(0);
			setState(211);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfBlockContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<CommandsContext> commands() {
			return getRuleContexts(CommandsContext.class);
		}
		public CommandsContext commands(int i) {
			return getRuleContext(CommandsContext.class,i);
		}
		public IfBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifBlock; }
	}

	public final IfBlockContext ifBlock() throws RecognitionException {
		IfBlockContext _localctx = new IfBlockContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_ifBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			match(T__16);
			setState(214);
			match(T__0);
			setState(215);
			expression(0);
			setState(216);
			match(T__2);
			setState(217);
			match(T__3);
			setState(221);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__11) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << ID))) != 0)) {
				{
				{
				setState(218);
				commands();
				}
				}
				setState(223);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElseBlockContext extends ParserRuleContext {
		public List<CommandsContext> commands() {
			return getRuleContexts(CommandsContext.class);
		}
		public CommandsContext commands(int i) {
			return getRuleContext(CommandsContext.class,i);
		}
		public ElseBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elseBlock; }
	}

	public final ElseBlockContext elseBlock() throws RecognitionException {
		ElseBlockContext _localctx = new ElseBlockContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_elseBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			match(T__17);
			setState(225);
			match(T__3);
			setState(229);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__11) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << ID))) != 0)) {
				{
				{
				setState(226);
				commands();
				}
				}
				setState(231);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssigmentCommandContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(simplifiedJavaGrammarParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssigmentCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assigmentCommand; }
	}

	public final AssigmentCommandContext assigmentCommand() throws RecognitionException {
		AssigmentCommandContext _localctx = new AssigmentCommandContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_assigmentCommand);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(ID);
			setState(233);
			match(T__10);
			setState(234);
			expression(0);
			setState(235);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public  type;
		public  inhType;
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
			this.type = ctx.type;
			this.inhType = ctx.inhType;
		}
	}
	public static class GoTermContext extends ExpressionContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public GoTermContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ComparativeOperationContext extends ExpressionContext {
		public Token op;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public ComparativeOperationContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 32;
		enterRecursionRule(_localctx, 32, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new GoTermContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(238);
			term(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(245);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ComparativeOperationContext(new ExpressionContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_expression);
					setState(240);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(241);
					((ComparativeOperationContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21))) != 0)) ) {
						((ComparativeOperationContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(242);
					term(0);
					}
					} 
				}
				setState(247);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public  type;
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	 
		public TermContext() { }
		public void copyFrom(TermContext ctx) {
			super.copyFrom(ctx);
			this.type = ctx.type;
		}
	}
	public static class GotTerm2Context extends TermContext {
		public Term2Context term2() {
			return getRuleContext(Term2Context.class,0);
		}
		public GotTerm2Context(TermContext ctx) { copyFrom(ctx); }
	}
	public static class EqualDiffOperationContext extends TermContext {
		public Token op;
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Term2Context term2() {
			return getRuleContext(Term2Context.class,0);
		}
		public EqualDiffOperationContext(TermContext ctx) { copyFrom(ctx); }
	}

	public final TermContext term() throws RecognitionException {
		return term(0);
	}

	private TermContext term(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TermContext _localctx = new TermContext(_ctx, _parentState);
		TermContext _prevctx = _localctx;
		int _startState = 34;
		enterRecursionRule(_localctx, 34, RULE_term, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new GotTerm2Context(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(249);
			term2(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(256);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new EqualDiffOperationContext(new TermContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_term);
					setState(251);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(252);
					((EqualDiffOperationContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==T__22 || _la==T__23) ) {
						((EqualDiffOperationContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(253);
					term2(0);
					}
					} 
				}
				setState(258);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Term2Context extends ParserRuleContext {
		public  type;
		public Term2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term2; }
	 
		public Term2Context() { }
		public void copyFrom(Term2Context ctx) {
			super.copyFrom(ctx);
			this.type = ctx.type;
		}
	}
	public static class PlusMinusOperationContext extends Term2Context {
		public Token op;
		public Term2Context term2() {
			return getRuleContext(Term2Context.class,0);
		}
		public Term3Context term3() {
			return getRuleContext(Term3Context.class,0);
		}
		public PlusMinusOperationContext(Term2Context ctx) { copyFrom(ctx); }
	}
	public static class GoTerm3Context extends Term2Context {
		public Term3Context term3() {
			return getRuleContext(Term3Context.class,0);
		}
		public GoTerm3Context(Term2Context ctx) { copyFrom(ctx); }
	}

	public final Term2Context term2() throws RecognitionException {
		return term2(0);
	}

	private Term2Context term2(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Term2Context _localctx = new Term2Context(_ctx, _parentState);
		Term2Context _prevctx = _localctx;
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_term2, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new GoTerm3Context(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(260);
			term3(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(267);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new PlusMinusOperationContext(new Term2Context(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_term2);
					setState(262);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(263);
					((PlusMinusOperationContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==T__24 || _la==T__25) ) {
						((PlusMinusOperationContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(264);
					term3(0);
					}
					} 
				}
				setState(269);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Term3Context extends ParserRuleContext {
		public  type;
		public Term3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term3; }
	 
		public Term3Context() { }
		public void copyFrom(Term3Context ctx) {
			super.copyFrom(ctx);
			this.type = ctx.type;
		}
	}
	public static class MultDivOperationContext extends Term3Context {
		public Token op;
		public Term3Context term3() {
			return getRuleContext(Term3Context.class,0);
		}
		public Term4Context term4() {
			return getRuleContext(Term4Context.class,0);
		}
		public MultDivOperationContext(Term3Context ctx) { copyFrom(ctx); }
	}
	public static class GoTerm4Context extends Term3Context {
		public Term4Context term4() {
			return getRuleContext(Term4Context.class,0);
		}
		public GoTerm4Context(Term3Context ctx) { copyFrom(ctx); }
	}

	public final Term3Context term3() throws RecognitionException {
		return term3(0);
	}

	private Term3Context term3(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Term3Context _localctx = new Term3Context(_ctx, _parentState);
		Term3Context _prevctx = _localctx;
		int _startState = 38;
		enterRecursionRule(_localctx, 38, RULE_term3, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new GoTerm4Context(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(271);
			term4();
			}
			_ctx.stop = _input.LT(-1);
			setState(278);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new MultDivOperationContext(new Term3Context(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_term3);
					setState(273);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(274);
					((MultDivOperationContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==T__26 || _la==T__27) ) {
						((MultDivOperationContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(275);
					term4();
					}
					} 
				}
				setState(280);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Term4Context extends ParserRuleContext {
		public  type;
		public Term4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term4; }
	 
		public Term4Context() { }
		public void copyFrom(Term4Context ctx) {
			super.copyFrom(ctx);
			this.type = ctx.type;
		}
	}
	public static class GoTerm5Context extends Term4Context {
		public Term5Context term5() {
			return getRuleContext(Term5Context.class,0);
		}
		public GoTerm5Context(Term4Context ctx) { copyFrom(ctx); }
	}
	public static class UnaryMinusOperationContext extends Term4Context {
		public Term4Context term4() {
			return getRuleContext(Term4Context.class,0);
		}
		public UnaryMinusOperationContext(Term4Context ctx) { copyFrom(ctx); }
	}

	public final Term4Context term4() throws RecognitionException {
		Term4Context _localctx = new Term4Context(_ctx, getState());
		enterRule(_localctx, 40, RULE_term4);
		try {
			setState(284);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__25:
				_localctx = new UnaryMinusOperationContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(281);
				match(T__25);
				setState(282);
				term4();
				}
				break;
			case T__0:
			case T__28:
			case INT:
			case FLOAT:
			case STRING:
			case BOOLEAN:
			case ID:
				_localctx = new GoTerm5Context(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(283);
				term5();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Term5Context extends ParserRuleContext {
		public  type;
		public Term5Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term5; }
	 
		public Term5Context() { }
		public void copyFrom(Term5Context ctx) {
			super.copyFrom(ctx);
			this.type = ctx.type;
		}
	}
	public static class GoFactorContext extends Term5Context {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public GoFactorContext(Term5Context ctx) { copyFrom(ctx); }
	}
	public static class NotOperationContext extends Term5Context {
		public Term5Context term5() {
			return getRuleContext(Term5Context.class,0);
		}
		public NotOperationContext(Term5Context ctx) { copyFrom(ctx); }
	}

	public final Term5Context term5() throws RecognitionException {
		Term5Context _localctx = new Term5Context(_ctx, getState());
		enterRule(_localctx, 42, RULE_term5);
		try {
			setState(289);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__28:
				_localctx = new NotOperationContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(286);
				match(T__28);
				setState(287);
				term5();
				}
				break;
			case T__0:
			case INT:
			case FLOAT:
			case STRING:
			case BOOLEAN:
			case ID:
				_localctx = new GoFactorContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(288);
				factor();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FactorContext extends ParserRuleContext {
		public  type;
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	 
		public FactorContext() { }
		public void copyFrom(FactorContext ctx) {
			super.copyFrom(ctx);
			this.type = ctx.type;
		}
	}
	public static class BoolTerminalContext extends FactorContext {
		public TerminalNode BOOLEAN() { return getToken(simplifiedJavaGrammarParser.BOOLEAN, 0); }
		public BoolTerminalContext(FactorContext ctx) { copyFrom(ctx); }
	}
	public static class CallFunctionTerminalContext extends FactorContext {
		public CallFunctionCommandContext callFunctionCommand() {
			return getRuleContext(CallFunctionCommandContext.class,0);
		}
		public CallFunctionTerminalContext(FactorContext ctx) { copyFrom(ctx); }
	}
	public static class OpenCloseParantesisTerminalContext extends FactorContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public OpenCloseParantesisTerminalContext(FactorContext ctx) { copyFrom(ctx); }
	}
	public static class IdTerminalContext extends FactorContext {
		public TerminalNode ID() { return getToken(simplifiedJavaGrammarParser.ID, 0); }
		public IdTerminalContext(FactorContext ctx) { copyFrom(ctx); }
	}
	public static class IntTerminalContext extends FactorContext {
		public TerminalNode INT() { return getToken(simplifiedJavaGrammarParser.INT, 0); }
		public IntTerminalContext(FactorContext ctx) { copyFrom(ctx); }
	}
	public static class FloatTerminalContext extends FactorContext {
		public TerminalNode FLOAT() { return getToken(simplifiedJavaGrammarParser.FLOAT, 0); }
		public FloatTerminalContext(FactorContext ctx) { copyFrom(ctx); }
	}
	public static class StringTerminalContext extends FactorContext {
		public TerminalNode STRING() { return getToken(simplifiedJavaGrammarParser.STRING, 0); }
		public StringTerminalContext(FactorContext ctx) { copyFrom(ctx); }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_factor);
		try {
			setState(301);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				_localctx = new OpenCloseParantesisTerminalContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(291);
				match(T__0);
				setState(292);
				expression(0);
				setState(293);
				match(T__2);
				}
				break;
			case 2:
				_localctx = new IdTerminalContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(295);
				match(ID);
				}
				break;
			case 3:
				_localctx = new IntTerminalContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(296);
				match(INT);
				}
				break;
			case 4:
				_localctx = new FloatTerminalContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(297);
				match(FLOAT);
				}
				break;
			case 5:
				_localctx = new StringTerminalContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(298);
				match(STRING);
				}
				break;
			case 6:
				_localctx = new BoolTerminalContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(299);
				match(BOOLEAN);
				}
				break;
			case 7:
				_localctx = new CallFunctionTerminalContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(300);
				callFunctionCommand();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 16:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		case 17:
			return term_sempred((TermContext)_localctx, predIndex);
		case 18:
			return term2_sempred((Term2Context)_localctx, predIndex);
		case 19:
			return term3_sempred((Term3Context)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean term_sempred(TermContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean term2_sempred(Term2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean term3_sempred(Term3Context _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(\u0132\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2\7\2\62"+
		"\n\2\f\2\16\2\65\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3@\n\3\f\3"+
		"\16\3C\13\3\5\3E\n\3\3\3\3\3\3\3\3\3\7\3K\n\3\f\3\16\3N\13\3\3\3\7\3Q"+
		"\n\3\f\3\16\3T\13\3\3\3\3\3\3\4\3\4\3\4\7\4[\n\4\f\4\16\4^\13\4\3\4\7"+
		"\4a\n\4\f\4\16\4d\13\4\3\4\3\4\3\5\3\5\3\5\3\5\6\5l\n\5\r\5\16\5m\3\6"+
		"\3\6\3\6\7\6s\n\6\f\6\16\6v\13\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\7\7\u0084\n\7\f\7\16\7\u0087\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\3\b\5\b\u0094\n\b\3\t\3\t\3\t\3\t\3\t\7\t\u009b\n\t\f\t"+
		"\16\t\u009e\13\t\5\t\u00a0\n\t\3\t\3\t\3\n\3\n\5\n\u00a6\n\n\3\n\3\n\3"+
		"\13\3\13\3\13\3\13\3\13\3\13\7\13\u00b0\n\13\f\13\16\13\u00b3\13\13\3"+
		"\13\5\13\u00b6\n\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\7\f\u00bf\n\f\f\f\16"+
		"\f\u00c2\13\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\7\r\u00cc\n\r\f\r\16\r\u00cf"+
		"\13\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\7"+
		"\17\u00de\n\17\f\17\16\17\u00e1\13\17\3\20\3\20\3\20\7\20\u00e6\n\20\f"+
		"\20\16\20\u00e9\13\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22"+
		"\3\22\7\22\u00f6\n\22\f\22\16\22\u00f9\13\22\3\23\3\23\3\23\3\23\3\23"+
		"\3\23\7\23\u0101\n\23\f\23\16\23\u0104\13\23\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\7\24\u010c\n\24\f\24\16\24\u010f\13\24\3\25\3\25\3\25\3\25\3\25"+
		"\3\25\7\25\u0117\n\25\f\25\16\25\u011a\13\25\3\26\3\26\3\26\5\26\u011f"+
		"\n\26\3\27\3\27\3\27\5\27\u0124\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30"+
		"\3\30\3\30\3\30\5\30\u0130\n\30\3\30\2\6\"$&(\31\2\4\6\b\n\f\16\20\22"+
		"\24\26\30\32\34\36 \"$&(*,.\2\b\4\2\7\7  \3\2!$\3\2\25\30\3\2\31\32\3"+
		"\2\33\34\3\2\35\36\2\u0140\2\63\3\2\2\2\48\3\2\2\2\6W\3\2\2\2\bg\3\2\2"+
		"\2\no\3\2\2\2\f{\3\2\2\2\16\u0093\3\2\2\2\20\u0095\3\2\2\2\22\u00a3\3"+
		"\2\2\2\24\u00a9\3\2\2\2\26\u00b9\3\2\2\2\30\u00c6\3\2\2\2\32\u00d3\3\2"+
		"\2\2\34\u00d7\3\2\2\2\36\u00e2\3\2\2\2 \u00ea\3\2\2\2\"\u00ef\3\2\2\2"+
		"$\u00fa\3\2\2\2&\u0105\3\2\2\2(\u0110\3\2\2\2*\u011e\3\2\2\2,\u0123\3"+
		"\2\2\2.\u012f\3\2\2\2\60\62\5\4\3\2\61\60\3\2\2\2\62\65\3\2\2\2\63\61"+
		"\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65\63\3\2\2\2\66\67\5\6\4\2\67\3"+
		"\3\2\2\289\7%\2\29D\7\3\2\2:;\7 \2\2;A\7%\2\2<=\7\4\2\2=>\7 \2\2>@\7%"+
		"\2\2?<\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2BE\3\2\2\2CA\3\2\2\2D:\3\2"+
		"\2\2DE\3\2\2\2EF\3\2\2\2FG\7\5\2\2GH\7\6\2\2HL\t\2\2\2IK\5\b\5\2JI\3\2"+
		"\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MR\3\2\2\2NL\3\2\2\2OQ\5\16\b\2PO\3"+
		"\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3\2\2\2UV\7\b\2\2V\5"+
		"\3\2\2\2WX\7\t\2\2X\\\7\6\2\2Y[\5\b\5\2ZY\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2"+
		"\\]\3\2\2\2]b\3\2\2\2^\\\3\2\2\2_a\5\16\b\2`_\3\2\2\2ad\3\2\2\2b`\3\2"+
		"\2\2bc\3\2\2\2ce\3\2\2\2db\3\2\2\2ef\7\b\2\2f\7\3\2\2\2gh\7\n\2\2hk\7"+
		"\6\2\2il\5\n\6\2jl\5\f\7\2ki\3\2\2\2kj\3\2\2\2lm\3\2\2\2mk\3\2\2\2mn\3"+
		"\2\2\2n\t\3\2\2\2ot\7%\2\2pq\7\4\2\2qs\7%\2\2rp\3\2\2\2sv\3\2\2\2tr\3"+
		"\2\2\2tu\3\2\2\2uw\3\2\2\2vt\3\2\2\2wx\7\6\2\2xy\7 \2\2yz\7\13\2\2z\13"+
		"\3\2\2\2{|\7\f\2\2|}\7%\2\2}~\7\r\2\2~\u0085\t\3\2\2\177\u0080\7\4\2\2"+
		"\u0080\u0081\7%\2\2\u0081\u0082\7\r\2\2\u0082\u0084\t\3\2\2\u0083\177"+
		"\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086"+
		"\u0088\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u0089\7\13\2\2\u0089\r\3\2\2"+
		"\2\u008a\u0094\5\22\n\2\u008b\u0094\5\24\13\2\u008c\u0094\5 \21\2\u008d"+
		"\u008e\5\20\t\2\u008e\u008f\7\13\2\2\u008f\u0094\3\2\2\2\u0090\u0094\5"+
		"\26\f\2\u0091\u0094\5\30\r\2\u0092\u0094\5\32\16\2\u0093\u008a\3\2\2\2"+
		"\u0093\u008b\3\2\2\2\u0093\u008c\3\2\2\2\u0093\u008d\3\2\2\2\u0093\u0090"+
		"\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0092\3\2\2\2\u0094\17\3\2\2\2\u0095"+
		"\u0096\7%\2\2\u0096\u009f\7\3\2\2\u0097\u009c\5\"\22\2\u0098\u0099\7\4"+
		"\2\2\u0099\u009b\5\"\22\2\u009a\u0098\3\2\2\2\u009b\u009e\3\2\2\2\u009c"+
		"\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2"+
		"\2\2\u009f\u0097\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1"+
		"\u00a2\7\5\2\2\u00a2\21\3\2\2\2\u00a3\u00a5\5\34\17\2\u00a4\u00a6\5\36"+
		"\20\2\u00a5\u00a4\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7"+
		"\u00a8\7\b\2\2\u00a8\23\3\2\2\2\u00a9\u00aa\7\16\2\2\u00aa\u00ab\7\3\2"+
		"\2\u00ab\u00ac\5\"\22\2\u00ac\u00ad\7\5\2\2\u00ad\u00b1\7\6\2\2\u00ae"+
		"\u00b0\5\16\b\2\u00af\u00ae\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3"+
		"\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4"+
		"\u00b6\7\17\2\2\u00b5\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\3"+
		"\2\2\2\u00b7\u00b8\7\b\2\2\u00b8\25\3\2\2\2\u00b9\u00ba\7\20\2\2\u00ba"+
		"\u00bb\7\3\2\2\u00bb\u00c0\5\"\22\2\u00bc\u00bd\7\4\2\2\u00bd\u00bf\5"+
		"\"\22\2\u00be\u00bc\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0"+
		"\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4\7\5"+
		"\2\2\u00c4\u00c5\7\13\2\2\u00c5\27\3\2\2\2\u00c6\u00c7\7\21\2\2\u00c7"+
		"\u00c8\7\3\2\2\u00c8\u00cd\7%\2\2\u00c9\u00ca\7\4\2\2\u00ca\u00cc\7%\2"+
		"\2\u00cb\u00c9\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce"+
		"\3\2\2\2\u00ce\u00d0\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\7\5\2\2\u00d1"+
		"\u00d2\7\13\2\2\u00d2\31\3\2\2\2\u00d3\u00d4\7\22\2\2\u00d4\u00d5\5\""+
		"\22\2\u00d5\u00d6\7\13\2\2\u00d6\33\3\2\2\2\u00d7\u00d8\7\23\2\2\u00d8"+
		"\u00d9\7\3\2\2\u00d9\u00da\5\"\22\2\u00da\u00db\7\5\2\2\u00db\u00df\7"+
		"\6\2\2\u00dc\u00de\5\16\b\2\u00dd\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df"+
		"\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\35\3\2\2\2\u00e1\u00df\3\2\2"+
		"\2\u00e2\u00e3\7\24\2\2\u00e3\u00e7\7\6\2\2\u00e4\u00e6\5\16\b\2\u00e5"+
		"\u00e4\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2"+
		"\2\2\u00e8\37\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb\7%\2\2\u00eb\u00ec"+
		"\7\r\2\2\u00ec\u00ed\5\"\22\2\u00ed\u00ee\7\13\2\2\u00ee!\3\2\2\2\u00ef"+
		"\u00f0\b\22\1\2\u00f0\u00f1\5$\23\2\u00f1\u00f7\3\2\2\2\u00f2\u00f3\f"+
		"\4\2\2\u00f3\u00f4\t\4\2\2\u00f4\u00f6\5$\23\2\u00f5\u00f2\3\2\2\2\u00f6"+
		"\u00f9\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8#\3\2\2\2"+
		"\u00f9\u00f7\3\2\2\2\u00fa\u00fb\b\23\1\2\u00fb\u00fc\5&\24\2\u00fc\u0102"+
		"\3\2\2\2\u00fd\u00fe\f\4\2\2\u00fe\u00ff\t\5\2\2\u00ff\u0101\5&\24\2\u0100"+
		"\u00fd\3\2\2\2\u0101\u0104\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2"+
		"\2\2\u0103%\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u0106\b\24\1\2\u0106\u0107"+
		"\5(\25\2\u0107\u010d\3\2\2\2\u0108\u0109\f\4\2\2\u0109\u010a\t\6\2\2\u010a"+
		"\u010c\5(\25\2\u010b\u0108\3\2\2\2\u010c\u010f\3\2\2\2\u010d\u010b\3\2"+
		"\2\2\u010d\u010e\3\2\2\2\u010e\'\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0111"+
		"\b\25\1\2\u0111\u0112\5*\26\2\u0112\u0118\3\2\2\2\u0113\u0114\f\4\2\2"+
		"\u0114\u0115\t\7\2\2\u0115\u0117\5*\26\2\u0116\u0113\3\2\2\2\u0117\u011a"+
		"\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119)\3\2\2\2\u011a"+
		"\u0118\3\2\2\2\u011b\u011c\7\34\2\2\u011c\u011f\5*\26\2\u011d\u011f\5"+
		",\27\2\u011e\u011b\3\2\2\2\u011e\u011d\3\2\2\2\u011f+\3\2\2\2\u0120\u0121"+
		"\7\37\2\2\u0121\u0124\5,\27\2\u0122\u0124\5.\30\2\u0123\u0120\3\2\2\2"+
		"\u0123\u0122\3\2\2\2\u0124-\3\2\2\2\u0125\u0126\7\3\2\2\u0126\u0127\5"+
		"\"\22\2\u0127\u0128\7\5\2\2\u0128\u0130\3\2\2\2\u0129\u0130\7%\2\2\u012a"+
		"\u0130\7!\2\2\u012b\u0130\7\"\2\2\u012c\u0130\7#\2\2\u012d\u0130\7$\2"+
		"\2\u012e\u0130\5\20\t\2\u012f\u0125\3\2\2\2\u012f\u0129\3\2\2\2\u012f"+
		"\u012a\3\2\2\2\u012f\u012b\3\2\2\2\u012f\u012c\3\2\2\2\u012f\u012d\3\2"+
		"\2\2\u012f\u012e\3\2\2\2\u0130/\3\2\2\2\36\63ADLR\\bkmt\u0085\u0093\u009c"+
		"\u009f\u00a5\u00b1\u00b5\u00c0\u00cd\u00df\u00e7\u00f7\u0102\u010d\u0118"+
		"\u011e\u0123\u012f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}