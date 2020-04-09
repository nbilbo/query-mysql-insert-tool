from tkinter import Tk, Text, Scrollbar, Frame
#from os import system
from default_font import DefaultFont

class LocalTexto( Frame ):
    #construtor
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )

        #localTexto e scrollTexto
        self.localTexto = Text( self, font = DefaultFont( ) )
        self.scrollTexto = Scrollbar( self, command = self.localTexto.yview )
        
        self.localTexto.configure( yscrollcommand = self.scrollTexto.set )

        self.scrollTexto.pack( side = "left", fill = "y" )
        self.localTexto.pack( side = "left", fill = "both", expand = True )
        
    #métodos
    def adicionarTexto( self, texto ):
        self.localTexto.insert( "end", texto )


def main( ):
    root = Tk( )
    texto = LocalTexto( root )
    texto.pack( fill = "both", expand = True, padx = 5, pady = 5 )
    texto.pack_propagate( False )
    root.geometry( "400x400+0+0" )
    root.mainloop( )
    #system( "cls" )

if __name__ == "__main__":
    main()
