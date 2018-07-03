####################################################
# Allison Nguyen, 2018
# this code can find any word in your transcript
# can only find single words right now except for 'you know'
# some fillers and backchannels are built in 
####################################################

import os
import io
import re
import csv


#this function creates a regex from your input!

def user_defined_regex(fill):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    userRegex = ''
    
    for letter in fill:
       userRegex = userRegex + letter + ('\:*')
            
    #print(userRegex)

    return userRegex

            
    
def filler_counter(path, fill):

    newReg = user_defined_regex(fill)
    

    filler = "\\" + fill

    nameV = '_' + fill


    
    #cleaned_1 = path + '\Clean_Transcripts'

    newP = path + filler


    #define your regex here
    #tested using regex101.com

    #some generic regexs you can enter

    #filler speech
    umRegex = re.compile(r'\bu(\:)?m(\-)*(\:)?(\,)*\b', re.I) # um
    uhRegex = re.compile(r'\bu(\:)?h(\-)*(\:)?(\,)*\b',re.I) # uh
    mhmRegex = re.compile(r'\bm*(\:*)h(\-*)(\:*)m*(\:*)?(\,*)\b', re.I) # mhm
    likeRegex = re.compile(r'\bl*i(\:*)*k*e(\:*)\b', re.I) # like
    youKnowRegex = re.compile(r'yo(\:*)u(\:*)(\s*)kno(\:*)w', re.I) # you know

    #backchannels
    okRegex = re.compile(r'\bo(\:*)k(a*(\:*))(y*(\:*))\b', re.I) #ok - works
    wowRegex = re.compile(r'\bw(\-*)o(\:*)(\-*)w\b', re.I) #wow - THERE ARE NO WOWS IN THIS I THINK
    yeahRegex = re.compile(r'y(\-*)e(\:*)(\-*)(\s*)a(\:*)h', re.I) #yeah
    greatRegex = re.compile(r'\bgre(\:*)a(\:*)t\b', re.I) #great
    userRegex = re.compile(r'%s' %(newReg), re.I)
    rightRegex = re.compile(r'\b(a*(\:*))(l*(\:*))r(\:*)i(\:*)g(\:*)h(\:*)t(\:*)\b', re.I) #right + alright
    
    

    for filename in os.listdir(path):

        file = filename.split(".")

        
        rename = file[0] + nameV
        
        os.chdir(path)

        with open(filename) as f:
            
            
            if not os.path.exists(newP):
               os.makedirs(path + filler)

            outputP = os.path.join(newP, rename + '.txt')

            lines = f.readlines()
            with open(outputP, 'w') as outFile:
                #search using regex
                writer = csv.writer(outFile)
                for line in lines:

                    if 'um' in fill:
                        x = umRegex.search(line)
                    elif fill == 'uh':
                        x = uhRegex.search(line)
                    elif fill == 'mhm':
                        x = mhmRegex.search(line)
                    elif fill == 'like':
                        x = likeRegex.search(line)
                    elif fill == 'you know':
                        x = youKnowRegex.search(line)
                    elif fill == 'ok':
                        x = okRegex.search(line)
                    elif fill == 'wow':
                        x = wowRegex.search(line)
                    elif fill == 'right':
                        x = rightRegex.search(line)
                    elif fill == 'yeah':
                        x = yeahRegex.search(line)
                    elif fill == 'great':
                        x = greatRegex.search(line)
                    else:
                        x = userRegex.search(line)
                    if x != None:
                        outFile.write(line)
                        outFile.write('\n')


def main():
    #get user specificed path
    userPath = raw_input("Type path to file folder: ")
    fill = raw_input("What filler are you searching for? (lowercase only)")
    filler_counter(userPath, fill)
   
	


main()

