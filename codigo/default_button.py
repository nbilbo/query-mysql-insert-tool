from tkinter import Tk, Button, Frame
#from os import system
from default_font import DefaultFont

class DefaultButton( Frame ):
    #construtor
    def __init__( self, *args, textoButton = "Button", **kwargs ):
        super().__init__( *args, **kwargs )

        #background
        #self["background"] = "black"

        #button
        self.button = Button( self, font = DefaultFont( ) )
        self.setTextoButton( textoButton )
        self.button.pack( padx = 5, pady = 5 )

    #métodos
    #retornar o texto de self.button
    def getTextoButton( self ):
        return self.button[ "text" ]

    #defirnir texto de self.button
    def setTextoButton(self, value):
        self.button.configure( text = value )
    

def main():
    root = Tk( )
    frameButton = DefaultButton( root, bg = "red" )
    frameButton.pack( fill = "x", padx = 5, pady = 5 )
    root.geometry( "400x400+0+0" )
    root.mainloop( )
    #system( "cls" )


if __name__ == "__main__":
    main()
