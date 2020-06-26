import sys, os, math

listArgs = sys.argv
path = sys.argv[1]
nbmodel = {}
spam_prob= 0
ham_prob = 0
write_string = ""
path_list = []
counter = 0
ham = 0
spam = 1

#creating a new nboutput.txt file to store important data
f = open("nboutput.txt","w+",encoding="latin1")

#transferring all prob data from nbmodel.txt onto dictionary
with open("nbmodel.txt", "r", encoding="latin1") as file_nbmodel:
    for line in file_nbmodel:             
            split_line = line.split(" ")
            nbmodel[split_line[0]] = [split_line[1], split_line[2]]     
spam_word_count = int(nbmodel["!spam_word_count"][0])
ham_word_count =  int(nbmodel["!ham_word_count"][0])
total_tokens = int(nbmodel["!total_tokens"][0])
ham_denominator = math.log(1/(ham_word_count + total_tokens))
spam_denominator = math.log(1/(spam_word_count + total_tokens))

#traverse through directory and read each file
for paths, directories, files in os.walk(path):
    for file in files:
        file = paths + os.sep + file
        path_list.append(file)
for file in path_list:
    spam_prob = float(nbmodel["!files_details"][spam])
    ham_prob = float(nbmodel["!files_details"][ham]) 
    #print (counter+1)        
    if "txt" in file:
        #print (file)
        filez = open(file, "r", encoding="latin1")            
        mail_data = filez.read()
        filez.close()
        mail_tokens = mail_data.split()            
        #extract probabilities of each word for each class and cumulatively multiply
        for token in mail_tokens:
            token = token.lower()
            if token in nbmodel:                                    
                    spam_prob = spam_prob + float(nbmodel[token][spam])                
                    ham_prob = ham_prob + float(nbmodel[token][ham])                 
#after each file has P(file|spam) and P(file|ham) write it onto nboutput.txt
    
    if spam_prob > ham_prob:
        #print (file)
        write_string += "spam\t"+file+"\n"
        #f.write("SPAM "+file+"\n")
    else:
        write_string += "ham\t"+file+"\n"
        #f.write("HAM "+file+"\n")

f.write(write_string)
f.close()
#actual