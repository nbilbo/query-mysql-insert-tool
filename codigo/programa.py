from tkinter import Tk, Frame, Button
from default_entry import DefaultEntry
from local_coluna import LocalColuna
from local_texto import LocalTexto

class Programa( Tk ):
    #construtor
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )

        #background
        self[ "background" ] = "black"

        #definirTabela
        self.definirTabela = DefaultEntry( self, textoLabel = "Tabela" )
        self.definirTabela.pack( fill = "x", padx = 5, pady = 5 )
        
        #frameBottom
        frameBottomBackground = "gray"
        self.frameBottom = Frame( self, bg = frameBottomBackground )
        self.frameBottom.pack( fill = "both", expand = True, padx = 5, pady = 5 )

        #localColuna
        self.localColuna = LocalColuna( self.frameBottom, bg = "blue" )
        self.localColuna.pack( side = "left", fill = "both", expand = True )

        #button
        self.button = Button( self.frameBottom, width = 5, text = ">>" )
        self.button.pack( side = "left", padx = 5, pady = 5 )
        self.button[ "command" ] = self.buttonClick

        #localTexto
        self.localTexto = LocalTexto( self.frameBottom )
        self.localTexto.pack( side = "left", fill = "both", expand = True )
    
    #métodos
    def buttonClick( self, *args ):
        nomeTabela = self.definirTabela.getTextoEntry( )
        query = self.localColuna.getQueryInsert( nomeTabela )
        self.localTexto.adicionarTexto( query )

def main():
    root = Programa( )
    root.geometry( "800x400+0+0" )
    root.mainloop( )

if __name__ == "__main__":
    main()
