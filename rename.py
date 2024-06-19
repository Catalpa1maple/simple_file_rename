import os
import shutil

folder_path = input("folder's path?")

filenames = os.listdir(folder_path)

file_type = input("type of files?")

index = 0
i = input("Index?")
for filename in filenames:
    old = folder_path+"/{}.{}".format(index,file_type)
    new = folder_path+"/{}.{}".format((index+i),file_type)
    try:
        os.rename(old,new)
    except:
        pass
    # print(old)
    # print(new)
    index += 1
