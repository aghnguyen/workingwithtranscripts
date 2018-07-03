####################################################
# Allison Nguyen, 2018
# this asks you for a file location
# (C:\User\Your File Path\Folder with Transcripts)
# then removes unwanted characters from txt files
# and prints the result to a new file
####################################################


import os
import io
import re
import csv


def clean_trans(path):
    
    #make a new folder to hold the new files
    cleanTrans = path + '\Clean_Transcripts'
    
    #if that doesn't exist make one
    if not os.path.exists(cleanTrans):
        os.makedirs(path + '\Clean_Transcripts')

    #loop through the file    
    for filename in os.listdir(path):

        #if it's a transcript (files saved in ###_trans.txt): CAN BE CHANGED TO MATCH YOUR FORMAT
        #and if it's not already cleaned
        if '_trans' in filename and '_clean' not in filename:
            file = filename.split(".")
            renameF = file[0] + '_clean'
            #make a clean output file
            output = os.path.join(cleanTrans , renameF +".txt")
            #update with current dir
            os.chdir(path)
            with open(filename) as f:
                lines = f.readlines()
                with open(output, 'w+') as outFile:
                    for line in lines:

                        #here's where you'd change your special characters
                        
                        if '[' in line:
                            line = line.replace('[', '=')
                        if '/' in line and '</' not in line:
                            line = line.replace('/', '[INAUD]')
                        
                        if '((' in line and '))' in line:
                            line = line.replace('[', '')
                            line = line.replace('(//', '[[')
                            line = line.replace('((', '[[')
                            #line = line.replace('(', '[')
                            line = line.replace('/', '')
                            line = line.replace('))', ']]')
                        if '<' in line or '</' in line:
                            if '1>' not in line and '2>' not in line:
                                line = line.replace('<', '[[')
                                line = line.replace('/', '')
                                line = line.replace('>', ']]')
                        if '(' in line:
                            line = line.replace('(', '[')
                            line = line.replace(')', ']')
                            
                        outFile.write(line)
                        outFile.write('\n')



def main():
    #get user specificed path
    userPath = raw_input("Type path to file folder: ")
    clean_trans(userPath)

main()   
                                
