import os
import io
#dictionary is the current input list of words
import dictionary as input_list
#write a csv file using the csv library
import csv
#use the regular expressions library
import regex_main
#gives colors so that we can print text in color or bold
RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'

def coder(marker_list, path):
    

    for filename in os.listdir(path):
        file = filename.split(".")
    
        with open(filename) as f:
            
            outputP = os.path.join(filename + '.csv')

            with open(outputP, 'w') as csvfile:
                fieldnames = ['word', '1_count' , '2_count', '3_count', '4_count', '5_count', '6_count', '7_count', '8_count', 'total_count', 'sentences']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                print(filename)
                for item in marker_list:
                    word = item
                    output = regex_main.display(word, filename)
                    writer.writerow({fieldnames[0]: word, fieldnames[1]: output[0], fieldnames[2]: output[1], fieldnames[3]: output[2], fieldnames[4]: output[3], fieldnames[5]: output[4],fieldnames[6]: output[5], fieldnames[7]: output[6], fieldnames[8]: output[7], fieldnames[9]: output[8], fieldnames[10]: output[9]})



def main():
    #get user specificed path
    userPath = input("Type path to file folder: ")
    coder(input_list.markers, userPath)
	


main()