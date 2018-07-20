####################################################
# Allison Nguyen, 2018
# 
####################################################

import os
import io
import re
import csv



def clean_trans(path):
    #for each file in the path
    cleanTrans = path + '\Clean_Transcripts'
    if not os.path.exists(cleanTrans):
        os.makedirs(path + '\Clean_Transcripts')
    for filename in os.listdir(path):   
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
                                
                                
    

def split_interview(path):
    
    cleaned = path + '\Clean_Transcripts'

    #for each file in the path
    for filename in os.listdir(cleaned):
        #if it's a transcript + just in case some wrong files are in there
         if '_trans' in filename and '_P' not in filename and '_I' not in filename:
            file = filename.split(".")
            renameP = file[0] + '_P'
            renameI = file[0] + '_I'
            
            participant = path + '\Clean_Transcripts\Participants'
            interviewer = path + '\Clean_Transcripts\Interviewer'
            
            if not os.path.exists(participant):
                os.makedirs(path + '\Clean_Transcripts\Participants')
                
            if not os.path.exists(interviewer): 
                os.makedirs(path + '\Clean_Transcripts\Interviewer')
                
            outputP = os.path.join(participant, renameP + '.txt')
            outputI = os.path.join(interviewer, renameI + '.txt')
            
            #remind the complier what the path is
            os.chdir(cleaned)
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
	

def user_defined_regex(fill):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    userRegex = ''
    
    for letter in fill:
       userRegex = userRegex + letter + ('\:*')

    #userRegex = userRegex + '\b'
    
    #print(userRegex)

    return userRegex

            
    
def filler_counter(path, fill):

    #print(fill)

    newReg = user_defined_regex(fill)
    

    filler = "\\" + fill

    nameV = '_' + fill

    
    
    cleaned_1 = path + '\Clean_Transcripts'
    newP = path + '\Clean_Transcripts' + filler


    #define your regex here
    #tested using regex101.com

    #filler speech
    umRegex = re.compile(r'\bu(\:)?m(\-)*(\:)?(\,)*\b', re.I) # um
    uhRegex = re.compile(r'\bu(\:)?h(\-)*(\:)?(\,)*\b',re.I) # uh
    mhmRegex = re.compile(r'\bm*(\:*)h(\-*)(\:*)m*(\:*)?(\,*)\b', re.I) # mhm
    likeRegex = re.compile(r'\bl*i(\:*)*k*e(\:*)\b', re.I) # like
    youKnowRegex = re.compile(r'yo(\:*)u(\:*)(\s*)kno(\:*)w', re.I) # you know
    gotItRegex = re.compile(r'go(\:*)t(\s*)i(\:*)t', re.I) # got it
	

    #backchannels
    okRegex = re.compile(r'\bo(\:*)k(a*(\:*))(y*(\:*))\b', re.I) #ok - works
    mmRegex = re.compile(r'\bm(\:*)m(a*(\:*))(y*(\:*))\b', re.I) #ok - works
    wowRegex = re.compile(r'\bw(\-*)o(\:*)(\-*)w\b', re.I) #wow 
    yeahRegex = re.compile(r'y(\-*)e(\:*)(\-*)(\s*)a(\:*)h', re.I) #yeah
    greatRegex = re.compile(r'\bgre(\:*)a(\:*)t\b', re.I) #great
    userRegex = re.compile(r'%s' %(newReg), re.I)
    rightRegex = re.compile(r'\b(a*(\:*))(l*(\:*))r(\:*)i(\:*)g(\:*)h(\:*)t(\:*)\b', re.I) #right + alright
    
    

    for filename in os.listdir(cleaned_1):
        
        file = filename.split(".")

        #CHANGE FOR FILLER YOU WANT
        rename = file[0] + nameV
        
        os.chdir(cleaned_1)

        with open(filename) as f:
            
            
            if not os.path.exists(newP):
               os.makedirs(path + '\Clean_Transcripts' + filler)

            outputP = os.path.join(newP, rename + '.txt')

            lines = f.readlines()
            with open(outputP, 'w') as outFile:
                #search using regex
                writer = csv.writer(outFile)
                for line in lines:
                    if fill == 'um':
                        x = umRegex.search(line)
                    elif fill == 'mm':
                        x = mmRegex.search(line)
                    elif fill == 'got it':
                        x = gotItRegex.search(line)
                    elif fill == 'uh':
                        x = uhRegex.search(line)
                        #counter = counter + 1
                    elif fill == 'mhm':
                        a = 0
                        x = mhmRegex.search(line)
                        #counter = counter + 1
                    elif fill == 'like':
                        x = likeRegex.search(line)
                        #counter = counter + 1
                    elif fill == 'you know':
                        a = 1
                        x = youKnowRegex.search(line)
                        #counter = counter + 1
                    elif fill == 'ok':
                        a = 0
                        x = okRegex.search(line)
                    elif fill == 'wow':
                        a = 1
                        x = wowRegex.search(line)
                        #counter = counter + 1
                    elif fill == 'right':
                        a = 1
                        x = rightRegex.search(line)
                        #counter = counter + 1
                    elif fill == 'yeah':
                        a = 1
                        x = yeahRegex.search(line)
                        #counter = counter + 1
                    elif fill == 'great':
                        a = 1
                        x = greatRegex.search(line)
                        #counter = counter + 1
                    else:
                        a = 1
                        x = userRegex.search(line)
                        #counter = counter + 1
                        

                    if x != None:
                        outFile.write(line)
                        outFile.write('\n')



def main():
    #get user specificed path
    userPath = input("Type path to file folder: ")
    fill = input("What filler are you searching for? (lowercase only)")
    #get path to clean_transcripts
    clean_trans(userPath)
    #newReg = user_defined_regex(fill)
    filler_counter(userPath, fill)
    split_interview(userPath)
	


main()

