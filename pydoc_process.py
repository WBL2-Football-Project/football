import subprocess
import os
import shutil

def pydoc_output():
    if __name__ == "__main__":
        sourcepath=os.chdir("src")
        sourcefiles = os.listdir(sourcepath)
        for file in sourcefiles:
            if file.endswith('.py'):
                curr_file = file.strip(".py")
                subprocess.run(["python3","-m","pydoc","-w","{0}".format(curr_file)],text=True)

def pydoc_move():
    sourcepath=os.getcwd()
    sourcefiles = os.listdir(sourcepath)
    destinationpath = '../documentation/'  
    for file in sourcefiles:
        if file.endswith('.html'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))

pydoc_output()
pydoc_move()