import subprocess
import os
import shutil

mainpath = os.getcwd()

def pydoc_output():
    if __name__ == "__main__":
        text = " START "
        paths = []
        print(f"{text:-^20}\n")
        print("Finding files...")
        for root, dirs, files in os.walk(".", topdown=False):
            for file in files:
                if file.endswith('.py'):
                    print("File found:",file)
                    paths.append(root)
        print("\nIn directories;")
        paths = list(dict.fromkeys(paths))
        print(paths)
        print("\nOutputting files...")
        for directory in paths:
            os.chdir(mainpath)
            dirname = os.path.relpath(directory)
            os.chdir(dirname)
            print("\nCWD: ",dirname,sep="")
            subprocess.run(["python3","-m","pydoc","-w",".\\"])

def pydoc_move():
    destinationpath = 'documentation/'  
    os.chdir(mainpath)
    print("Moving files...")
    for root, dirs, files in os.walk(".", topdown=False):
        for file in files:
            if file.endswith('.html'):
                try:
                    print("File moved:",file)
                    shutil.move(os.path.join(root,file), os.path.join(destinationpath,file))
                except:
                    print("Something went wrong with the",file,"file.")

pydoc_output()
pydoc_move()
text = " END "
print(f"\n{text:-^20}")