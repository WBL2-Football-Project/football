from ui.GUI import GUI
from api.SystemController import SystemController
from api.api import API

if __name__ == "__main__":
    SystemController(GUI(), API())
