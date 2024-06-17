import os
import shutil

folder_path = './Audio_file'

filenames = os.listdir(folder_path)

index = 0

for filename in filenames:
    old = "{}.mp3".format(index)
    new = "{}.mp3".format(index+2000)
    os.rename(old,new)
    index += 1
    
