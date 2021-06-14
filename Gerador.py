import ArrayList
import NaluthaListener

class Gerador(NaluthaListener):
	Saida Saida
    List<Modelo> listaDeModelos

    def __init__(self, saida):
        self.saida = saida
        self.listaDeModelos = ArrayList<>()

    def visitMap(NaluthaParser.MapContext ctx):
        #colocar aqui o código que imprime os arquivos do tutorial

        #para imprimir usar a função self.saida.imprime("string que precisa ser escrita")
        self.saida.imprime("teste")
        #para acessar os "var" (modelo, entidade ou campo) criadas no código de entrada utilizar:
        #ctx.var().forEach(var -> visitVar(var))