import shutil
import os

src="SOURCE OF DIRECTORY WHERE YOU WANT TO SEARCH"              #example: D:\demo
dest="DESTINATION DIRECTORY WHERE YOU WANT TO COPY THAT FILE"   #example: D:\DemoCopy
toSearch="FILE TO BE SEARCHED"                                  #example: "Dataset.csv"
folder=file=0

try:
    os.makedirs(dest)
except:
    print("ALREADY EXISTERD")
def checkFile(src,searchFile):                                  #Recursive Fuction to Check the file in each Folder
    global folder,file
    src_file = os.listdir(src)                                  #listDir returns all files and folder within the src in src_file
    for file_name in src_file:
        full_file_name = os.path.join(src, file_name)           #this create a path by joining src and file_name
        if os.path.isdir(full_file_name):                       #check weather it is a directory or a file
            folder += 1
            checkFile(full_file_name,toSearch)                  #Again call the function recursively until it reach the last folder
        else:
            if file_name == toSearch:
                shutil.copy(full_file_name, dest)               #Copy the file to the destination folder
            file += 1

checkFile(src,toSearch)
print("FOLDER",folder)                                            #COUNT OF TOTAL FOLDERS
print("FILE",file)                                                #COUNT OF TOTAL FILES


