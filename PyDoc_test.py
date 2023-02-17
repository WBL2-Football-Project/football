"""
    Modules;
    - Subprocess module to run bash within .py
    Syntax is as follows
    subprocess.run(["first_arg","second_arg","x_arg"]), for example subprocess.run(["python","-m","pydoc","-w","PyDoc_test"],text=True)

    - pathlib is a module that we are utilizing to move files, in this case the syntax pathlib.Path("filename.ext").replace("newDir/filename.ext") allows the replacement of a file so we can keep documentation updated.

    Extensions;
    - autoDocstring - Python Docstring Generator - Put 3 quote marks (") to open documentation, then press tab to move through documentation and add details.
"""
import subprocess
import pathlib
import tkinter


def pydoc_test():
    """
        Final function to output PyDoc generated documentation. If any modules have been added they will need to be manually added using the below syntax;
        pathlib.Path("moduleName.html").replace("documentation/moduleName.html")

        Please note, the modules name will also need to be added to the pydoc output.
    """
    if __name__ == "__main__":
        subprocess.run(["python","-m","pydoc","-w","PyDoc_test","subprocess","pathlib","tkinter"],text=True)
        pathlib.Path("PyDoc_test.html").replace("documentation/PyDoc_test.html")
        pathlib.Path("subprocess.html").replace("documentation/subprocess.html")
        pathlib.Path("pathlib.html").replace("documentation/pathlib.html")
        pathlib.Path("tkinter.html").replace("documentation/tkinter.html")

def test_func(num1,num2):
    """_summary_

    Args:
        num1 (_type_): _description_
        num2 (_type_): _description_
    """

pydoc_test()