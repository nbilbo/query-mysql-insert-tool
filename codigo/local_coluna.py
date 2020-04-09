from tkinter import Tk, Frame
from default_button import DefaultButton
from definir_coluna import DefinirColuna
from frame_scroll import FrameScroll
from os import system

class LocalColuna( Frame ):
    #construtor
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )

        #frameScroll
        self.frameScroll = FrameScroll( self )
        self.frameScroll.pack( fill = "both", expand = True )

        #frameButton
        self.frameButton = DefaultButton( self, textoButton = "Adicionar coluna", bg = "black")
        self.frameButton.pack( fill = "x", padx = 5, pady = 5 )
        self.button = self.frameButton.button
        self.button[ "command" ] = self.buttonClick

    #métodos
    #retornar uma query mysql de insert
    def getQueryInsert( self, nomeTabela ):
        #lista
        nomeColuna = list()
        valorColuna = list()
        #referenciar scrollableFrame
        scrollableFrame =  self.winfo_children()[0].scrollableFrame 

        #percorrer todas as widget filhas
        for children in scrollableFrame.winfo_children( ):
            nomeColuna.append( children.frameEntry.getTextoLabel( ) )
            valorColuna.append( children.getTextoEntry() )

        #formatar lista
        nomeColuna = ", ".join( nomeColuna )
        valorColuna = ", ".join( valorColuna )

        #query
        query = f'INSERT INTO {nomeTabela} \n({nomeColuna}) \nVALUES \n({valorColuna});\n\n'
        return query
        

    #self.button clicado
    def buttonClick( self, *args ):
        #instanciar DefinirColuna
        container = self.frameScroll.scrollableFrame
        DefinirColuna( containerDaColuna = container )
   

def main( ):
    root = Tk( )
    localColuna = LocalColuna( root, bg = "blue" )
    localColuna.pack( side = "top", fill = "both", expand = True, padx = 5, pady = 5 )
    root.geometry( "400x400+0+0" )
    root.mainloop( )
    #system( "cls" )

if __name__ == "__main__":
    main()
