import os
import shutil

typedelete = input("enter name of file to delete")
foldername = input("enter the folder name")

foldername = foldername+"/"

os.remove(foldername+typedelete)