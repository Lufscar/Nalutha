// Generated from Nalutha.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class NaluthaParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, Id=6, WS=7;
	public static final int
		RULE_model_lex = 0, RULE_entity_lex = 1, RULE_dois_pontos = 2, RULE_abre_chave = 3, 
		RULE_fecha_chave = 4, RULE_program = 5, RULE_model = 6, RULE_entity = 7, 
		RULE_field = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"model_lex", "entity_lex", "dois_pontos", "abre_chave", "fecha_chave", 
			"program", "model", "entity", "field"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Model'", "'Entity'", "':'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, "Id", "WS"
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
	public String getGrammarFileName() { return "Nalutha.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public NaluthaParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class Model_lexContext extends ParserRuleContext {
		public Model_lexContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_model_lex; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).enterModel_lex(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).exitModel_lex(this);
		}
	}

	public final Model_lexContext model_lex() throws RecognitionException {
		Model_lexContext _localctx = new Model_lexContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_model_lex);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			match(T__0);
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

	public static class Entity_lexContext extends ParserRuleContext {
		public Entity_lexContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity_lex; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).enterEntity_lex(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).exitEntity_lex(this);
		}
	}

	public final Entity_lexContext entity_lex() throws RecognitionException {
		Entity_lexContext _localctx = new Entity_lexContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_entity_lex);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			match(T__1);
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

	public static class Dois_pontosContext extends ParserRuleContext {
		public Dois_pontosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dois_pontos; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).enterDois_pontos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).exitDois_pontos(this);
		}
	}

	public final Dois_pontosContext dois_pontos() throws RecognitionException {
		Dois_pontosContext _localctx = new Dois_pontosContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_dois_pontos);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
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

	public static class Abre_chaveContext extends ParserRuleContext {
		public Abre_chaveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_abre_chave; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).enterAbre_chave(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).exitAbre_chave(this);
		}
	}

	public final Abre_chaveContext abre_chave() throws RecognitionException {
		Abre_chaveContext _localctx = new Abre_chaveContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_abre_chave);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			match(T__3);
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

	public static class Fecha_chaveContext extends ParserRuleContext {
		public Fecha_chaveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fecha_chave; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).enterFecha_chave(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).exitFecha_chave(this);
		}
	}

	public final Fecha_chaveContext fecha_chave() throws RecognitionException {
		Fecha_chaveContext _localctx = new Fecha_chaveContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_fecha_chave);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			match(T__4);
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

	public static class ProgramContext extends ParserRuleContext {
		public ModelContext model() {
			return getRuleContext(ModelContext.class,0);
		}
		public TerminalNode EOF() { return getToken(NaluthaParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			model();
			setState(29);
			match(EOF);
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

	public static class ModelContext extends ParserRuleContext {
		public List<EntityContext> entity() {
			return getRuleContexts(EntityContext.class);
		}
		public EntityContext entity(int i) {
			return getRuleContext(EntityContext.class,i);
		}
		public ModelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_model; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).enterModel(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).exitModel(this);
		}
	}

	public final ModelContext model() throws RecognitionException {
		ModelContext _localctx = new ModelContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_model);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			match(T__0);
			setState(32);
			match(T__3);
			setState(36);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(33);
				entity();
				}
				}
				setState(38);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(39);
			match(T__4);
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

	public static class EntityContext extends ParserRuleContext {
		public TerminalNode Id() { return getToken(NaluthaParser.Id, 0); }
		public List<FieldContext> field() {
			return getRuleContexts(FieldContext.class);
		}
		public FieldContext field(int i) {
			return getRuleContext(FieldContext.class,i);
		}
		public EntityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).enterEntity(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).exitEntity(this);
		}
	}

	public final EntityContext entity() throws RecognitionException {
		EntityContext _localctx = new EntityContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_entity);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			match(T__1);
			setState(42);
			match(Id);
			setState(43);
			match(T__3);
			setState(45); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(44);
				field();
				}
				}
				setState(47); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==Id );
			setState(49);
			match(T__4);
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

	public static class FieldContext extends ParserRuleContext {
		public Token fieldName;
		public Token fieldType;
		public List<TerminalNode> Id() { return getTokens(NaluthaParser.Id); }
		public TerminalNode Id(int i) {
			return getToken(NaluthaParser.Id, i);
		}
		public FieldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).enterField(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof NaluthaListener ) ((NaluthaListener)listener).exitField(this);
		}
	}

	public final FieldContext field() throws RecognitionException {
		FieldContext _localctx = new FieldContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_field);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			((FieldContext)_localctx).fieldName = match(Id);
			setState(52);
			match(T__2);
			setState(53);
			((FieldContext)_localctx).fieldType = match(Id);
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t:\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3"+
		"\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\7\b%\n\b\f\b\16\b"+
		"(\13\b\3\b\3\b\3\t\3\t\3\t\3\t\6\t\60\n\t\r\t\16\t\61\3\t\3\t\3\n\3\n"+
		"\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\2\2\62\2\24\3\2\2\2\4\26\3"+
		"\2\2\2\6\30\3\2\2\2\b\32\3\2\2\2\n\34\3\2\2\2\f\36\3\2\2\2\16!\3\2\2\2"+
		"\20+\3\2\2\2\22\65\3\2\2\2\24\25\7\3\2\2\25\3\3\2\2\2\26\27\7\4\2\2\27"+
		"\5\3\2\2\2\30\31\7\5\2\2\31\7\3\2\2\2\32\33\7\6\2\2\33\t\3\2\2\2\34\35"+
		"\7\7\2\2\35\13\3\2\2\2\36\37\5\16\b\2\37 \7\2\2\3 \r\3\2\2\2!\"\7\3\2"+
		"\2\"&\7\6\2\2#%\5\20\t\2$#\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\')\3"+
		"\2\2\2(&\3\2\2\2)*\7\7\2\2*\17\3\2\2\2+,\7\4\2\2,-\7\b\2\2-/\7\6\2\2."+
		"\60\5\22\n\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\63\3"+
		"\2\2\2\63\64\7\7\2\2\64\21\3\2\2\2\65\66\7\b\2\2\66\67\7\5\2\2\678\7\b"+
		"\2\28\23\3\2\2\2\4&\61";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}