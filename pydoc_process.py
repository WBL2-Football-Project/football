import subprocess
import os
import shutil

def pydoc_output():
    if __name__ == "__main__":
        for root, dirs, files in os.walk(".", topdown=False):
            for file in files:
                if file.endswith('.py'):
                    if os.getcwd() != root:
                        print("WORKING")
                        print(os.path.relpath(root))
                        os.chdir(os.path.relpath(root))
                    print("")
                    cwd = os.getcwd()
                    print("CWD: - ",cwd,"\n","Root: ",root,sep="")
                    # curr_file = file.strip(".py")
                    # print(os.path.join(root, file))
                    # subprocess.run(["python","-m","pydoc","-w","{0}".format(curr_file)],text=True)

def pydoc_move():
    destinationpath = 'documentation/'  
    for root, dirs, files in os.walk(".", topdown=False):
        for file in files:
            if file.endswith('.html'):
                shutil.move(os.path.join(root,file), os.path.join(destinationpath,file))
    text = " END "
    print(f"\n{text:-^20}\n")

pydoc_output()
#pydoc_move()