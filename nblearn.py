import os, sys, math

#data directory for training dataset
listArgs = sys.argv;
path = sys.argv[1];
ham_word_count = 0;
spam_word_count = 0;
word_count = 0;
write_string = ""    
spam_files = 0
ham_files = 0 
total_tokens = 0      
ham = 0
spam = 1      
common_words = {"a", "an", "the", "aboard","about","above","across","after","against","along","amid","among","anti","around","as","at","before","behind","below","beneath","beside","besides","between","beyond","by","concerning","considering","despite","down","during","except","excepting","excluding","following","for","from","in","inside","into","like","minus","near","of","off","on","onto","opposite","outside","over","past","per","plus","regarding","round","save","since","than","through","to","toward","towards","under","underneath","unlike","until","up","upon","versus","via","with","within","without"}                                             
#creating a new nbmodel.txt file to start storing information
f = open("nbmodel.txt","w+",encoding="latin1");
path_list = []

#creating a dictionary to store all values from every individual file
token_dictionary = {}
for paths, directories, files in os.walk(path):
    for file in files:      
        if file.endswith("txt"):                        
            file = paths + os.sep + file
            path_list.append(file)  
            
#training             
for file in path_list:
    if "train" in file:                    
        if ".spam." in file:
            spam_files += 1
        elif ".ham." in file:
            ham_files += 1
        filez = open(file, "r", encoding="latin1")
        mail_data = filez.read()
        filez.close() 
        mail_tokens = mail_data.split()                
        for token in mail_tokens:              
                token = token.lower()
                #if len(token)>2:                
                if (token[0].isdigit() or token[0].isalpha()): #checking if it's a valid token                                        
                    if token not in token_dictionary:  
                        total_tokens += 1                                                 
                        token_dictionary[token]=[0,0]      #incrementing frequency                                                                      
                    if ".spam." in file:
                        spam_word_count = spam_word_count+1                     
                        token_dictionary[token][spam] += 1                                  
                    elif ".ham." in file:
                        ham_word_count = ham_word_count+1
                        token_dictionary[token][ham] += 1
                        #updating after incrementing     
                        
#calculating conditional probability for each token and storing in table
token_probability = {}
for token in token_dictionary:    
    spam_count = (token_dictionary[token][spam]+1)/(spam_word_count+total_tokens)
    ham_count = (token_dictionary[token][ham]+1)/(ham_word_count+total_tokens)
    spam_count = math.log(spam_count)
    ham_count = math.log(ham_count)
    token_probability[token] = [ham_count, spam_count]    

write_string += "!ham_word_count " + str(ham_word_count) +" 0\n"
write_string += "!spam_word_count " + str(spam_word_count) + " 0\n"
write_string += "!total_tokens " + str(total_tokens) + " 0\n"
#storing P(spam) and P(ham) in nbmodel   
p_spam = spam_files/(spam_files+ham_files)
p_ham = ham_files/(ham_files+spam_files)  
p_spam = math.log(p_spam)
p_ham = math.log(p_ham) 
write_string += "!files_details"+" "+str(p_ham)+" "+str(p_spam)+"\n"    

#writing conditional probability for each token into nbmodel.txt
for token in token_probability:
    write_string += token+" "+str(token_probability[token][ham])+" "+str(token_probability[token][spam])+"\n"
f.write(write_string)
f.close();
#actual



