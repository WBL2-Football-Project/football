from UIAbstractInterface import UIAbstractInterface
from UIHelperInterface import UIHelperInterface

class UIConsole(UIAbstractInterface):
    def __init__(self,helper:UIHelperInterface):
        self.helper = helper
        UIAbstractInterface.__init__(self,self)
