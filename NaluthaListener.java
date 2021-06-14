// Generated from Nalutha.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link NaluthaParser}.
 */
public interface NaluthaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link NaluthaParser#model_lex}.
	 * @param ctx the parse tree
	 */
	void enterModel_lex(NaluthaParser.Model_lexContext ctx);
	/**
	 * Exit a parse tree produced by {@link NaluthaParser#model_lex}.
	 * @param ctx the parse tree
	 */
	void exitModel_lex(NaluthaParser.Model_lexContext ctx);
	/**
	 * Enter a parse tree produced by {@link NaluthaParser#entity_lex}.
	 * @param ctx the parse tree
	 */
	void enterEntity_lex(NaluthaParser.Entity_lexContext ctx);
	/**
	 * Exit a parse tree produced by {@link NaluthaParser#entity_lex}.
	 * @param ctx the parse tree
	 */
	void exitEntity_lex(NaluthaParser.Entity_lexContext ctx);
	/**
	 * Enter a parse tree produced by {@link NaluthaParser#dois_pontos}.
	 * @param ctx the parse tree
	 */
	void enterDois_pontos(NaluthaParser.Dois_pontosContext ctx);
	/**
	 * Exit a parse tree produced by {@link NaluthaParser#dois_pontos}.
	 * @param ctx the parse tree
	 */
	void exitDois_pontos(NaluthaParser.Dois_pontosContext ctx);
	/**
	 * Enter a parse tree produced by {@link NaluthaParser#abre_chave}.
	 * @param ctx the parse tree
	 */
	void enterAbre_chave(NaluthaParser.Abre_chaveContext ctx);
	/**
	 * Exit a parse tree produced by {@link NaluthaParser#abre_chave}.
	 * @param ctx the parse tree
	 */
	void exitAbre_chave(NaluthaParser.Abre_chaveContext ctx);
	/**
	 * Enter a parse tree produced by {@link NaluthaParser#fecha_chave}.
	 * @param ctx the parse tree
	 */
	void enterFecha_chave(NaluthaParser.Fecha_chaveContext ctx);
	/**
	 * Exit a parse tree produced by {@link NaluthaParser#fecha_chave}.
	 * @param ctx the parse tree
	 */
	void exitFecha_chave(NaluthaParser.Fecha_chaveContext ctx);
	/**
	 * Enter a parse tree produced by {@link NaluthaParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(NaluthaParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link NaluthaParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(NaluthaParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link NaluthaParser#model}.
	 * @param ctx the parse tree
	 */
	void enterModel(NaluthaParser.ModelContext ctx);
	/**
	 * Exit a parse tree produced by {@link NaluthaParser#model}.
	 * @param ctx the parse tree
	 */
	void exitModel(NaluthaParser.ModelContext ctx);
	/**
	 * Enter a parse tree produced by {@link NaluthaParser#entity}.
	 * @param ctx the parse tree
	 */
	void enterEntity(NaluthaParser.EntityContext ctx);
	/**
	 * Exit a parse tree produced by {@link NaluthaParser#entity}.
	 * @param ctx the parse tree
	 */
	void exitEntity(NaluthaParser.EntityContext ctx);
	/**
	 * Enter a parse tree produced by {@link NaluthaParser#field}.
	 * @param ctx the parse tree
	 */
	void enterField(NaluthaParser.FieldContext ctx);
	/**
	 * Exit a parse tree produced by {@link NaluthaParser#field}.
	 * @param ctx the parse tree
	 */
	void exitField(NaluthaParser.FieldContext ctx);
}