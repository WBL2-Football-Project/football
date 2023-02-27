import subprocess
import os
import shutil
import dominate
from dominate.tags import *

mainpath = os.getcwd()
count = 0

def pydoc_output():
    global count
    try:
        os.chdir('documentation')
        for old_files in os.listdir("."):
            if old_files.endswith(".html"):
                os.remove(old_files)
    except:
        print("No documentation folder found, please run this file from the root folder.")
        exit(-1)
    paths = []
    os.chdir("..")
    
    for root, dirs, files in os.walk(".", topdown=False):
        for file in files:
            if file.endswith('.py'):
                count+=1
                #print("File found:",file)
                paths.append(root)
    #print("\nIn directories;")
    paths = list(dict.fromkeys(paths))
    #print(paths)
    for directory in paths:
        os.chdir(mainpath)
        dirname = os.path.relpath(directory)
        os.chdir(dirname)
        #print("\nCWD: ",dirname,sep="")
        subprocess.run(["python3","-m","pydoc","-w",".\\"])

def pydoc_move():
    destinationpath = 'documentation/'  
    os.chdir(mainpath)
    for root, dirs, files in os.walk(".", topdown=False):
        for file in files:
            if file.endswith('.html'):
                try:
                    #print("File moved:",file)
                    shutil.move(os.path.join(root,file), os.path.join(destinationpath,file))
                except:
                    print("Something went wrong with the",file,"file.")
                    exit(-1)
    print("\nFiles documented - ",count,sep="")

def pydoc_test():
    file_list = {}
    
    os.chdir('documentation')
    for html_file in os.listdir("."):
        if html_file.endswith(".html"):
            html_file_new = "https://htmlpreview.github.io/?https://raw.githubusercontent.com/WBL2-Football-Project/football/main/documentation/"+html_file
            file_list.update({html_file: html_file_new})

    html_code = dominate.document(title='WBL2-Football-Project/football documentation')  

    with html_code:
        with div(id='Title'):
            h1("WBL2-Football-Project/football documentation")

        with div(id='Documentation'):
            html_file_list = ul()
            for file_name, file_path in file_list.items():
                html_file_list+= li(a(file_name,href=file_path))

    try:
        index_file = open('index.html','w')
        index_file.write(str(html_code))
        index_file.close()
    except:
        print("Something went wrong with the index.html file.")

if __name__ == "__main__":
    pydoc_output()
    pydoc_move()
    pydoc_test()