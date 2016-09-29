"""
Embedded_Images.py

Contains encoded GIF images AToM3 depends upon in its user-interface.
Advantage: image file never gets 'lost' or 'misplaced' :D

Sample usage:
1) from Embedded_Images import Embedded_Images
2) self.image = Embedded_Images().getImageMethod()

Note: the complexity of the structure may seem like overkill, but because of the
way Python import statements & Tkinter work, it really is necessary :p

Done with imageEmbedder 1.0 utility img2pytk.py from
http://www.3dartist.com/WP/python/pycode.htm#img2pytk

Created August 10, 2004
"""

import Tkinter

class Embedded_Images:
  
  isInitilized = False
  
  def __init__( self ):
    
    # No point doing this twice :D
    if( self.isInitilized ): 
      return
    else:                    
      self.isInitilized = True
      self.__loadPhotoImages()
      
  def getMainLogo(self):
    return self.Main_Logo_Photoimage
  
  def getPopupLogo(self):
    return self.Popup_Logo_Photoimage   
  
  def getLHS(self):
    return self.LHS_Photoimage 
  
  def getRHS(self):
    return self.RHS_Photoimage 
    
  def __loadPhotoImages( self ):
    """ Converts data to Photoimage """
        
    self.Main_Logo_Photoimage = Tkinter.PhotoImage(format='gif',data=
             'R0lGODdhnQBBAPcAAAAAACEAQikAQikASikAUikAWikIWjEAQjEASjEAUjEA'
            +'WjEAYzEIQjEISjEIUjEIWjEIYzkASjkAUjkAWjkAYzkAazkISjkIUjkIWjkI'
            +'YzkIazkQUjkQWjkQY0IAWkIAY0IAa0IAc0IIUkIIWkIIY0IIa0IIc0IIe0IQ'
            +'UkIQWkIQY0IQa0IQc0IYUkIYY0IYa0oAhEoIY0oIa0oIc0oIe0oIhEoQY0oQ'
            +'a0oQc0oQe0oYY0oYa0oYc0oYe0ohY1IAc1IIa1IIc1IIhFIQa1IQc1IQe1IQ'
            +'hFIYa1IYc1IYe1JzAFJ7AFoAc1oAe1oAhFoQe1oQhFoQjFoYhFoYjFohjFp7'
            +'AFqEAGMAhGMAjGMYjGOEAGOMAGOUAGsAjGsAlGuMAGuUAGucAHMAlHMAnHMA'
            +'pXOcAHOlAHsApXsArXulAHutAIQArYQAtYStAIS1AJTOAJzOAMaUAMbOAMb/'
            +'Wsb/Y86UAM7OAM7/Y///Wv//Y///////////////////////////////////'
            +'////////////////////////////////////////////////////////////'
            +'////////////////////////////////////////////////////////////'
            +'////////////////////////////////////////////////////////////'
            +'////////////////////////////////////////////////////////////'
            +'////////////////////////////////////////////////////////////'
            +'////////////////////////////////////////////////////////////'
            +'////////////////////////////////////////////////////////////'
            +'////////////////////////////////////////////////////////////'
            +'/////////////////////ywAAAAAnQBBAEAI/gD/CRxIsKDBgwgTKlzIsKHD'
            +'hxAjSpxI8MqVJhYtDghgoEGDDiMWeMhAYkWSJCHQUPyXMePKlzBjyvyXYQSE'
            +'EWjQrNGJho1BAECDCh0KIEMKEx4SeDjDdM3OnRNFoOBgI8WIMWJy+kz4BYwW'
            +'K2DKeLWypYxZNW7UtIHYRQyWLm3fxhUDV26XiEAFrsChAicbnmsKEh0ctCAO'
            +'JCU6/IU6MO/BFSAzqEghcMSIDTv/JmzbZQzWMWSqbAkLpo0VLV3TlEnjEAcQ'
            +'EzfWjHGKBkgOI1KiGLkRZG5duG4BvHkj3M1wAAQTKBXK+B/yg4Mbj+EggoEA'
            +'oQQByLGzvTv3792R/nswUaIn5w8SRkQWmAFIEBmBB275smVLFS2k07phLZGE'
            +'Cw4qrHEGGgosQMABDqh0kAodOHfcG8ZBSJxghTWm0FCCZVehQNrJ4Z2H3XnI'
            +'3XMJKecBDmPMRFEG5MlgwhmyCRgfQySqqGKNC42QgAAieGDjj0A2BEAeeQBF'
            +'ZJFEDplkkEw26eSTUEYZZUstYXTRlVZidIZmUnbp5UIkjGDCQQY4oAIHO/XE'
            +'00RUtiQGaGMwxVRMnpHRmWdiOHSaFktUoQRZZr0UF1x3qeiACAT4BRiHRN0x'
            +'xx10OEpHpHMMtkIQNxAR26IP1RSmBB58UAILOTVnkFhlHJSfWmo8FEQJ/pgm'
            +'gQQOIwQRww2+dSGXW3TpSmiGBlU1gguZcWrhQgB00VIDGKRQk2w0jkBSqCMQ'
            +'ZEIBCxQrEHCc1VTBm2RghSppYqmWRhtotfqQCSQAiAaMMM62Bg1C0GBEEVA8'
            +'YUQJJsgQl3DESTjccc5lsAKGHDKKHbIJL4xchyCCJ7EcAIzkgQQk2GDDQUh0'
            +'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'
            +'MpWDHohSRJiESriETMgkAQEAADs=')


    self.Popup_Logo_Photoimage = Tkinter.PhotoImage(format='gif',data=
             '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'
            +'yUyQg4G8QwpD+0TQ7LEMiHArfAEBADs=')
            
            
    self.LHS_Photoimage = Tkinter.PhotoImage(format='gif',data=
             'R0lGODlhPAAoAPf/AP///wBKMQAxIQBSOVrnvTHerQjWnABzUgCMYwClcwCt'
            +'ewDGjADOlEretULetSnerSHWpRjWpQAhGAA5KQBaQgB7WgCUawCccwC1hAC9'
            +'jADWnFLevTnetSnWrRDWpQjWpQBCMQBjSgCEYwCMawClewCthADGlADOnEre'
            +'vSHWrQBKOQBzWinOrQApIQBSQgB7YwClhFrexjnOtRDGpQi9nABaSgiljAit'
            +'lAi1nAiEcxi1pRCtnBC1pQiUhAicjAillABKQlLGvQhzawiEe1rOxkK9tTm9'
            +'tSmtpSm1rSGtpRi1rQiMhAiUjFK9vUq9vTmtrQhaWghjYwhrawh7ewAhITmt'
            +'tRCMlCmcpQhjawhKUghSWghaYymUpSGUpRiElAhCSggxORBjcxBrewg5QgAp'
            +'MSmctRiEnDGUrSmMpRh7lEKctTGMpQg5SkqlxkKcvTGMrRBSa0KUtRhrjBBK'
            +'YwgxQkqcxjmMtSFznDmMvSlznCFrlBhSczFznBhKa0KMxjmEvQgpQiFajCFj'
            +'nBA5Wtbn97XG1jF7va29zr3W7zl7vSlrrSFalBhKezFjnDFrrSFanKXG75y9'
            +'52OErSFSjJSlvbXO75StznuUtXOMrWuEpWN7nDFrvSFKhJytxpy975S154yt'
            +'3oSl1muMvVJzpTFjrSlapRg5a87e96291qW1zq3G74ylzlpznDlrvSlSlDlz'
            +'zjFjtSFKjClarb3G1qW954ScxmN7pYSl3jlrxiFCeylSnDFjvSFKlBg5c8bW'
            +'973O75ytzpSlxoycvYSUtaW975y154yl1oScznuUxnOMvWN7rVpzpVJrnDFa'
            +'rTlrziFChClSpTFjxhg5e5St54yl3lJrpTljvTljxilKlDFatSFCjJSlznOE'
            +'rWt7pWNznISc1ilKnHuMvVprnCE5e9be97W91q21zmt7rWNzpVJjnCE5hJyl'
            +'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'
            +'9xzdde5zNREQADs=')
    
    
    self.RHS_Photoimage = Tkinter.PhotoImage(format='gif',data=
             'R0lGODlhPAAoAPf/AP///ykpKYR7e2NaWox7e4Rzc3trazkxMXNjYzEpKWNS'
            +'UoxzcykhIUIxMYRrY2tSSqWUjEo5MSkYEFpKQlJCOWtSQqWMe5yEc4RrWsal'
            +'jMace3NSOZRrStaca5xrQrV7SnNKKUI5MXNaQlI5ISkYCK2Ue8alhFpKOdat'
            +'hFJCMcacc72Ua7WMY4RjQsaUY96la5xzSr2MWntaObWEUoxjOb2ESrV7QjEh'
            +'EGM5EJxaGDkhCCkhGO+9hPe9e8aUWt6lY/e1a86UUvetWr2EQqVzOe+lUs6M'
            +'QrV7Od6UQoxaIfecOd6MMYRSGOeMKb1zIZRaGKVjGNa1jNala/e9c72MUrWE'
            +'SpRrOXtSIfelQr17Kc6EKfecMbVzIVo5EO+UKcZ7IdaEIWtCEK1rGHtKEFIx'
            +'CP/Ge96lWr2MSve1WvetSpxrKeecOZRjIeeUKb17IYxaGM6EIZxjGN6MIXNK'
            +'EEIpCGNSOWNCEKVrGFpKMUoxCN7v99bn987W3q29zr3W7yEpMaXG75y954y1'
            +'55SlvbXO75y11pStzoScvXuUtYSt5zFrvZytxpS154Sl1ilapc7e96W1zq3G'
            +'72uErTFKczlzzjFjtTFrxiFKjClard7n973G1qW954ScxoSl3kJrtTFSjCE5'
            +'YzljrSlKhDlrxilSnCFKlBg5c8bO3sbW973O75SlxoycvYSUtXuMrXOEpaW9'
            +'75y155St3oyl1oSczoSl5zlKa0JajDlShDlanEJrvTFarTlrziFChBg5e87W'
            +'55St54yl3lpzrUpjnDlSjDlapSlCezljvSlKlDFatSFCjL3O962956W13pyt'
            +'1pSlzoycxnuMtXOErWt7pUJSe1pztTFCayk5YzFKjCE5cylKnN7n/73G3jlC'
            +'WlJjlDlKeyE5e7W91q21zqWtxlJac2t7rTlKhJylxlpjhJScvYyUtXN7nEpS'
            +'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'
            +'vproQzjSK45FLMIcAQEAOw==')

    