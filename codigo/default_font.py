from tkinter.font import Font

class DefaultFont( Font ):
    #construtor
    def __init__( self, *args, **kwargs ):
        super( ).__init__( *args, **kwargs )

        #size
        self[ "size" ] = 12

        #weight
        self[ "weight" ] = "bold"