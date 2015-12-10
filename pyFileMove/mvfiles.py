'''
Created on Nov 22, 2015
@author: Nancy Schorr
'''
##  You need to create a file called "fileslist.py" in the the same directory as this file
##  inside fileslist.py you need a line that contains the file types to move 
##  Put one line in the file the defines the list dirTypes like this:
##  dirTypes = ["pdf", "cat", "car", "aaa", "ring", "avery", "avalon",  "jpg", "doc" ]

import re
import os
import shutil
import sys
PYTHONDONTWRITEBYTECODE = True   #prevents bytecode .pyc files from being created

## you can put the fileslist.py file here: 
sys.path.append(os.path.abspath("E:\\Workspace\\PrivateFiles\\")) 

if __name__ == '__main__':   pass

from fileslist import dirNames

impfiles=sys.modules.keys()  ## print out the python modules we're using
for i in impfiles :
    if re.search("fileslist", str(i)):  # make sure fileslist.py can be found
        print "yes its here: " + str(i)

print "sys.path is: " + str(sys.path)  ## just for fun

inDirToSort= 'C:\\Users\\user\\Desktop\\MYDOCS'  ## where your files to be sorted are
outDir='C:\\Users\\user\\Desktop\\moved'    ## where you are sorting to
 
def mywalk(inputDir):
    for rootDir, subDirs, eachFile in os.walk(inputDir):
        fullFilePathName=[rootDir,subDirs,eachFile]      
        print "-------------  working on " + str(fullFilePathName)
       
        for efile in eachFile:
            print "!!-----------------------------starting over --newval equals: " +  efile
            for dirNameItem in dirNames:
                print "dirNameItem is: " + dirNameItem
             
                if re.search(dirNameItem, efile, re.IGNORECASE ):
                    print "FOUND MATCH. efile is: " + str(efile)
                   
                    oldpath =  os.path.join(rootDir, efile)
                    newdir =  "c:/Users/user/Desktop/moved/" + dirNameItem
                    
                    print "rootDir is: " + rootDir +" oldpath is: " + oldpath
                    print "newdir is: " + newdir
                    print(  os.path.isfile(oldpath) )    ## make sure they're there              
                    print(  os.path.isdir(newdir) ) 
                    
                    if dirNameItem == 'test' :     ## an exception to the rule
                        print "found test"                
                        shutil.move(oldpath, "C:\\Users\\user\\Desktop\\moved\\exceptions")
                    else :
                        shutil.move(oldpath, newdir)
                        
                    print "-------done with a loop"
                    break  ## breaking because there is no sense in continuing with this item
                
                        
mywalk(inDirToSort)

print "end of program"


