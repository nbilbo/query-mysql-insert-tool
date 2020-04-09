from tkinter import Tk, Frame, Button, Toplevel, IntVar, Checkbutton
from functools import partial
#from os import system
from default_button import DefaultButton
from default_entry import DefaultEntry


class DefinirColuna( Toplevel ):
    #construtor
    def __init__( self, *args, containerDaColuna = None, textoButton = "Adicionar", **kwargs ):
        super().__init__( *args, **kwargs )

        #background
        self[ "background" ] = "black"
        #geometry
        self.geometry( "450x110+500+0" )

        #containerDaColuna
        self.containerDaColuna = containerDaColuna

        #frameTop
        frameTopBackground = "black"
        self.frameTop = Frame( self, bg = frameTopBackground )
        self.frameTop.pack( fill = "x", padx = 5, pady = 5 )

        #frameEntry
        self.frameEntry = DefaultEntry( self.frameTop, textoLabel = "Coluna", bg = "blue" )
        self.frameEntry.pack( side = "left", fill = "x", expand = True, padx = 5, pady = 5 )
        self.entry = self.frameEntry.entry
        self.entry.bind( "<Return>", self.buttonClick )
        self.entry.focus( )

        #checkbutton
        self.intCheckbutton = IntVar()
        self.checkbutton = Checkbutton( self.frameTop, text = "String", variable = self.intCheckbutton )
        self.checkbutton.pack( side = "left", padx = 5, pady = 5 )
        self.setCheckbuttonValue( 1 )

        #frameBottom
        frameBottomBackground = "black"
        self.frameBottom = Frame( self, bg = frameBottomBackground )
        self.frameBottom.pack(  padx = 5, pady = 5 )

        #frameButton
        self.frameButton = DefaultButton( self.frameBottom, textoButton = textoButton, bg = "blue" )
        self.frameButton.pack( padx = 5, pady = 5 )
        self.button = self.frameButton.button
        self.button[ "command" ] = self.buttonClick

    #métodos
    #button clicado
    def buttonClick( self, *args ):
        nomeColuna = self.frameEntry.getTextoEntry( )
        stringValue = self.getCheckbuttonValue( )
        #condição para que seja adicionada uma nova coluna
        if nomeColuna.strip():
            #instanciando uma NovaColuna
            novaColuna = NovaColuna( self.containerDaColuna, string = stringValue )
            #atualizando seus valores
            novaColuna.frameEntry.setTextoLabel( nomeColuna )
            #finalizando
            novaColuna.pack( fill = "x", padx = 5, pady = 5 )
            self.destroy( )
            #atualizar os atributos de cada width 'filha' de scrollableFrame
            scrollableFrame = self.containerDaColuna.master.master
            scrollableFrame.atualizarIrma( )

    #retornar o valor de intCheckbutton
    def getCheckbuttonValue( self ):
        return self.intCheckbutton.get()

    #definir o valor de intCheckbutton
    def setCheckbuttonValue( self, value ):
        self.intCheckbutton.set( value )
    
    #getter setter containerDaColuna
    @property
    def containerDaColuna( self ):
        return self._containerDaColuna

    @containerDaColuna.setter
    def containerDaColuna( self, containerDaColuna ):
        self._containerDaColuna = containerDaColuna


class NovaColuna( Frame ):
    #contrutor
    def __init__( self, *args, string = True, **kwargs ):
        super( ).__init__( *args, **kwargs  )

        #background
        self[ "background" ] = "blue"

        #string
        self.string = string

        #irmaProximo
        self.irmaProximo = None

        #irmaAnterior
        self.irmaAnterior = None

        #buttonDestroy
        self.buttonDestroy = Button( self, text = "X" )
        self.buttonDestroy.pack( side = "left", padx = 5, pady = 5 )
        self.buttonDestroy[ "command" ] = self.buttonDestroyClick

        #frameEntry
        self.frameEntry = DefaultEntry( self )
        self.frameEntry.pack( side = "left", fill = "x", expand = True, padx = 5, pady= 5 )
        self.entry = self.frameEntry.entry
        
        #caso o usuario clique 2x em cima do label, abrir uma nova janela com um campo de texto.
        self.frameEntry.label.bind("<Double-Button-1>", self.frameBind)

        #focar irmaProximo
        self.entry.bind( "<Return>", self.focarIrmaProximo )
        self.entry.bind( "<Down>", self.focarIrmaProximo )

        #focar irmaAnterior
        self.entry.bind( "<Up>", self.focarIrmaAnterior )

    #métodos
    #atualizar o nome da coluna
    def frameBind( self, *args ):
        RedefinirColuna( coluna = self, textoButton = "Atualizar" )
    
    def focarIrmaProximo( self, *args ):
        self.irmaProximo.entry.focus( )
    
    def focarIrmaAnterior( self, *args ):
        self.irmaAnterior.entry.focus( )
    
    #verificar o atributo self.string e retornar o valor de entry 
    def getTextoEntry( self ):
        texto = self.frameEntry.getTextoEntry()
        if self.string:
            return f"'{texto}'"
        
        return texto

    #buttonDestroy clicado
    def buttonDestroyClick( self, *args ):
        #referenciar o container 
        frameScroll = self.master.master.master
        #destruir-se
        self.destroy( )
        #chamar o método do container
        frameScroll.atualizarIrma( )

    #getter setter string
    @property
    def string( self ):
        return self._string
    
    @string.setter
    def string( self, string ):
        self._string = string

    #getter setter irmaProximo
    @property
    def irmaProximo( self ):
        return self._irmaProximo
    
    @irmaProximo.setter
    def irmaProximo( self, irmaProximo ):
        self._irmaProximo = irmaProximo

    #getter setter irmaAnterior
    @property
    def irmaAnterior( self ):
        return self._irmaAnterior
    
    @irmaAnterior.setter
    def irmaAnterior( self, irmaAnterior ):
        self._irmaAnterior = irmaAnterior


class RedefinirColuna( DefinirColuna ):
    #construtor
    def __init__( self, *args, coluna, **kwargs ):
        super( ).__init__( *args, **kwargs )
        
        #coluna
        self._coluna = coluna

        #destruir o label
        self.frameEntry.label.destroy()
        #atualizando o texto de label
        #self.frameEntry.setTextoLabel( coluna.frameEntry.getTextoLabel( ) )
        #atualizando o texto de entry
        self.frameEntry.setTextoEntry( coluna.frameEntry.getTextoLabel( ) )
        #atualizando o checkbutton
        self.setCheckbuttonValue( coluna.string )
        
       

    #métodos
    #button clicado
    def buttonClick( self, *args ):
 
        nomeColuna = self.frameEntry.getTextoEntry( )
        stringValue = self.getCheckbuttonValue( )
        #condição para atualizar a coluna
        if nomeColuna.strip( ):
            #atualizando os valores da coluna
            self.coluna.frameEntry.setTextoLabel( nomeColuna )
            self.coluna.string = stringValue
            self.destroy()
    
    #getter coluna
    @property
    def coluna( self ):
        return self._coluna


def main():
    root = Tk( )
    #DefinirColuna( containerDaColuna = root )
    nova = NovaColuna( root )
    nova.pack( fill = "x" )
    root.geometry( "400x400+0+0" )
    root.mainloop( )
    #system( "cls" )

if __name__ == "__main__":
    main()
