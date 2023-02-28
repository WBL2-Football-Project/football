from UIAbstractInterface import UIAbstractInterface
from UIHelperInterface import *

class UITkinterGUI(UIAbstractInterface):
    def __init__(self,helper:UIHelperInterface):
        self.helper = helper
        UIAbstractInterface.__init__(self,self)
