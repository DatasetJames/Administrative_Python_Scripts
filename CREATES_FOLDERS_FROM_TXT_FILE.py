import os

with open('put location of .txt path here', 'rU') as x:
    for line in x:
        line = line.strip().split()
        filename = "_".join([i for i in line])
        os.chdir("put location of where you want the folders to be created at")
        os.mkdir(filename)
        
