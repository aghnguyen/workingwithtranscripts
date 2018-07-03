####################################################
# Allison Nguyen, 2018
####################################################

import os
import io
import re
import csv


def split_interview(path):
    
    #cleaned = path + '\Clean_Transcripts'


    #here we have 'P' for participant and 'I' for interviewer - change this to what you labeled yours
    
    #for each file in the path
    for filename in os.listdir(path):
        #if it's a transcript + just in case some wrong files are in there

        #CHANGE _P and _I 
         if '_trans' in filename and '_P' not in filename and '_I' not in filename:
            file = filename.split(".")
            renameP = file[0] + '_P'
            renameI = file[0] + '_I'

            #create new folders for new files - can rename if want to
            participant = path + '\Participants'
            interviewer = path + '\Interviewer'
            
            if not os.path.exists(participant):
                os.makedirs(path + '\Participants')
                
            if not os.path.exists(interviewer): 
                os.makedirs(path + '\Interviewer')
                
            outputP = os.path.join(participant, renameP + '.txt')
            outputI = os.path.join(interviewer, renameI + '.txt')
            
            #remind the complier what the path is
            os.chdir(path)
            with open(filename) as f:
                lines = f.readlines()
                with open(outputP, 'w+') as pFile:
                    with open(outputI, 'w+') as iFile:
                        for line in lines:
                            splitstring = line.split()
                            #if the string is bigger than 1
                            if len(splitstring) > 1:
                            
                                #if the string is a participant string or an annotation
                                if splitstring[1] == 'P:' or splitstring[1] == '<' or splitstring[0] == '<P':
                                    pFile.write(line)
                                    pFile.write('\n')
                                
                                #if the string is an interviewer string or an annotation
                                elif splitstring[1] == 'I:' or splitstring[1] == '<' or splitstring[0] == '<I':
                                    iFile.write(line)
                                    iFile.write('\n')
                                
                                #otherwise write whatever it is to both files
                                else:
                                    pFile.write('\n')
                                    pFile.write(line)
                                    pFile.write('\n')
                                    iFile.write('\n')
                                    iFile.write(line)
                                    iFile.write('\n')
	

def main():
    #get user specificed path
    userPath = raw_input("Type path to file folder: ")
    split_interview(userPath)
	


main()
