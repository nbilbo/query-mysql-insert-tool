from tkinter import Tk, Scrollbar, Canvas, Frame
from os import system

class FrameScroll( Frame ):
    #construtor
    def __init__( self, *args, **kwargs ):
        super( ).__init__( *args, **kwargs )

        #canvas e scrollCanvas
        backgroundCanvas = "black"
        self.canvas = Canvas( self, bg = backgroundCanvas, highlightthickness=0, relief='ridge' )
        
        self.scrollCanvas = Scrollbar( self, command = self.canvas.yview )

        self.canvas.configure( yscrollcommand = self.scrollCanvas.set )

        self.scrollCanvas.pack( side = "left", fill = "y" )
        self.canvas.pack( side = "left", fill = "both", expand = True )

        #scrollableFrame
        scrollableFrameBackground = "black"
        self.scrollableFrame = Frame( self.canvas, bg = scrollableFrameBackground )

        #canvasFrame
        self.canvasFrame = self.canvas.create_window( ( 0, 0 ), window = self.scrollableFrame, anchor = "nw" )

        #bind
        self.canvas.bind( "<Configure>", self.frameWidth )
        self.scrollableFrame.bind( "<Configure>", self.onFrameConfigure )

    #métodos
    #resposavel por atualizar os atributos irmaProximo e irmaAnterior de cada width 'filha' de scrollableFrame
    def atualizarIrma( self ):
        if len( self.scrollableFrame.winfo_children( ) ) > 0:
            
            #atualizar atributo irmaProximo
            for indice in range( len( self.scrollableFrame.winfo_children( ) ) - 1 ):
                coluna = self.scrollableFrame.winfo_children( )[ indice ]
                coluna.irmaProximo = self.scrollableFrame.winfo_children( )[ indice + 1 ]
            self.scrollableFrame.winfo_children( )[ -1 ].irmaProximo = self.scrollableFrame.winfo_children( )[ 0 ]

            #atualizar o atributo irmaAnterior
            listaFilha = self.scrollableFrame.winfo_children( )
            listaFilha = listaFilha[ ::-1 ]
            for indice in range( len( listaFilha ) - 1 ):
                coluna = listaFilha[ indice ]
                coluna.irmaAnterior = listaFilha[ indice + 1 ]
            listaFilha[ -1 ].irmaAnterior = listaFilha[ 0 ]
           
    def frameWidth( self, event ):
        canvasWidth = event.width
        self.canvas.itemconfig( self.canvasFrame, width = canvasWidth )

    def onFrameConfigure( self, event ):
        self.canvas.configure( scrollregion = self.canvas.bbox( "all" ) )

def main():
    root = Tk( )
    frame = FrameScroll( root, bg = "blue" )
    frame.pack( fill = "both", expand = True, padx = 5, pady = 5 )
    for a in range( 11 ):
        novoFrame = Frame( frame.scrollableFrame, height = 100, bg = "red" )
        novoFrame.pack(side = "top", fill ="x", padx = 5, pady = 5)
    root.geometry( "400x400+0+0" )
    root.mainloop( )
    system( "cls" )

if __name__ == "__main__":
    main()
