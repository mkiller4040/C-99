import time, os, shutil

path = "C:/Users/monit/delete"

if(os.path.exists(path)) :
    for rootFolder, folders, files in os.walk(path) :
        for folder in folders :
            folderPath = os.path.join(rootFolder, folder)
            os.remove(folderPath)
        for file in files : 
            filePath = os.path.join(rootFolder, file)
            os.remove(filePath)
else :
    print("Path not found")


    
