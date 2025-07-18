import os
from display import *

#setOrientation(0)

def ls(path = "", tabs = 0):
    t.defineTextbox(1,1,237,30, BLACK,GREY,WHITE, arial10)
    for file in os.listdir(path):
        stats = os.stat(path+"/"+file)
        filesize = stats[6]
        isdir = stats[0] & 0x4000
        
        if filesize < 1000:
            sizestr = str(filesize) + "bytes"
        elif filesize < 1000000:
            sizestr = "%0.1f KB" % (filesize/1000)
        elif filesize < 1000000000:
            sizestr = "%0.1f MB" % (filesize/1000000)
        else:
            sizestr = "%0.1f GB" % (filesize/1000000000)
            
        prettyprintname = ""
        for i in range(tabs):
            prettyprintname += "   "
        prettyprintname += file
        if isdir:
            prettyprintname += "/"
            t.appendLine('{0:<40} Size: {1:>10}'.format(prettyprintname, sizestr))
        
        if isdir:
            ls(path+"/"+file, tabs+1)

def print_directory(path, tabs = 0):
    for file in os.listdir(path):
        stats = os.stat(path+"/"+file)
        filesize = stats[6]
        isdir = stats[0] & 0x4000
     
        if filesize < 1000:
            sizestr = str(filesize) + " by"
        elif filesize < 1000000:
            sizestr = "%0.1f KB" % (filesize/1000)
        else:
            sizestr = "%0.1f MB" % (filesize/1000000)
     
        prettyprintname = ""
        for i in range(tabs):
            prettyprintname += "   "
        prettyprintname += file
        if isdir:
            prettyprintname += "/"
            print('{0:<40} Size: {1:>10}'.format(prettyprintname, sizestr))
        
        # recursively print directory contents
        if isdir:
            print_directory(path+"/"+file, tabs+1)

g = Screen()
g.bgFill()
g.update()
print("Files on filesystem:")
print("====================")
print_directory("")
t = Textbox("Files on filesystem:")
t.appendLine("====================")
ls()