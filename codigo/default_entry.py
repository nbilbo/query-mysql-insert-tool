from tkinter import Tk, Frame, Entry, Label, StringVar
from os import system

class DefaultEntry( Frame ):
    #construtor
    def __init__( self, *args, textoLabel = "Label", larguraLabel = 15, **kwargs ):
        super().__init__( *args, **kwargs )

        #background
        #self[ "background" ] = "black"

        #label
        self.stringLabel = StringVar()
        self.label = Label( self, width = larguraLabel, textvariable = self.stringLabel )
        self.setTextoLabel( textoLabel )
        self.label.pack( side = "left", padx = 5, pady = 5 )

        #Entry
        self.entry = Entry( self )
        self.entry.pack( side = "left", fill = "x", expand = True, padx = 5, pady = 5 )
    
    #métodos
    #retornar o texto de self.entry
    def getTextoEntry( self ):
        return self.entry.get()
    
    #definir o texto de self.entry
    def setTextoEntry( self, value ):
        self.entry.insert( 0, value )
    
    #retornar o texto de self.label
    def getTextoLabel( self ):
        return self.stringLabel.get()
    
    #definir o texto de self.label
    def setTextoLabel( self, value ):
        self.stringLabel.set( value )


def main( ):
    root = Tk( )
    DefaultEntry( root, textoLabel = "Label", bg = "red" ).pack( fill = "x", padx = 5, pady = 5 )
    root.geometry( "400x400+0+0" )
    root.mainloop( )
    system( "cls" )


if __name__ == "__main__":
    main()
