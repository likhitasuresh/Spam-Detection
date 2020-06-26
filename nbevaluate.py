import sys
#dictionary for each path and correctness of label
precision = [0,0]
recall = [0,0]
f1 = [0,0]
correctly_classified = [0,0]
classified = [0,0]
belongs_in = [0,0]
listArgs = sys.argv
file = sys.argv[1]
ham = 0
spam = 1
#read the file line by line, adding into diictionary after checking how correct the labels are
with open(file, "r", encoding="latin1") as file_nboutput:
    for line in file_nboutput:        
            split_line = line.split()
            if ".ham.txt" in split_line[1]:
                belongs_in[ham] += 1
                if split_line[0] == "ham":
                    correctly_classified[ham] += 1                                    
            elif ".spam.txt" in split_line[1]:
                belongs_in[spam] += 1
                if split_line[0] == "spam":
                    correctly_classified[spam] += 1 
            if split_line[0] == "ham":
                classified[ham] += 1
            elif split_line[0] == "spam":
                classified[spam] += 1
precision[ham] = correctly_classified[ham]/classified[ham]
precision[spam] = correctly_classified[spam]/classified[spam]

recall[ham] = correctly_classified[ham]/belongs_in[ham]
recall[spam] = correctly_classified[spam]/belongs_in[spam]

f1[0] = 2*precision[ham]*recall[ham] / (precision[ham]+recall[ham])
f1[1] = 2*precision[spam]*recall[spam] / (precision[spam]+recall[spam])

print (precision)
print (recall)
print (f1)

    



