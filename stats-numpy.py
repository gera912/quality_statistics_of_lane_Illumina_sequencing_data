#!/usr/bin/env python
# coding: utf-8

# In[1]:


# imports a module
import matplotlib.pyplot as plt
import numpy as np

# The magic command that prints a plot in Jupyter notebook.
get_ipython().run_line_magic('matplotlib', 'inline')


# Stores a file path to a variable
file = "../lane1_NoIndex_L001_R1_003.fastq"

# Creates a list  
Number_base_pairs = np.zeros(101)


# Creates a variable
LN = 0


#file= "../test20190703.txt"

# Creates a method that takes an instance variable.
def convert_phred(letter):
    
    # Creates a variable that stores a difference 
    # of -33 of the unicode point from the instance variable. 
    x = ord(letter) - 33
    
    # returns a variable with the result.
    return x


    
    
    
# opens a text file to read and stores the text file as a variable.     
with open(file,"r") as fh:
    # A for loop that goes through each line in the text file.
    for line in fh:
        # updates the variable by an addition of one after each loop.
        LN = LN + 1
                
 
NumRec = int(16000000/4)
#NumRec = int(LN/4)

#print(NumRec)
                    
#print(np.zeros((NumRec, 101)))
mean_scores= np.zeros(101)

#median=np.zeros(101)

all_qscores=np.zeros((101, NumRec))
#all_qscores=np.zeros((NumRec, 101))



# opens a text file to read and stores the text file as a variable.        
with open(file,"r") as fh:
        LN=0
        row= 0
        # A for loop that goes through each line in the text file.
        #for LN, line in enumerate(fh):
        for line in fh:
            
          
            # updates the variable by an addition of one after each loop.
            LN = LN + 1
            
            # If statemnt to get the fourth line from each record in text file.
            if LN%4 == 0:
                row = 1+ row
                #print(line)
                
                # A for loop that goes through each character in the line.    
                for column in range(len(line)-1):
                    
                    # Stores a character from line to a variable
                    char = line[column]
                    
                    # calls the method with an instance ands stores the
                    # result into a variable.
                    value = convert_phred(char)
                    
                    # Stores a value in a list that is an index of another list
                    all_qscores[column][row-1]=value
                  
                 
                    

# Prints a statement in a specific format                    
print("# Base Pair\t","Mean Quality Score\t", "Variance\t", "Standard Deviation\t", "Median")                     
  

# A for loop that goes through each index in the length of the list.    
for index in range(len(all_qscores)):
    
    # Computes the mean of list in the index and store the result in a variable.
    mean = np.mean(all_qscores[index])
    #print(mean)
    
    # Computes the variance of list in the index and store the result in a variable.
    var = np.var(all_qscores[index])
   
    # Computes the standard deviation of the of list in the index and store the result in a variable.
    std = np.std(all_qscores[index])
    
    # Computes the median of the of list in the index and store the result in a variable.
    median = np.median(all_qscores[index])
    
     # Prints a statement in a specific format
    print("{0}\t{1}\t{2}\t{3}\t{4}".format(index, mean,var, std, median))
    
# Creates an empty dictionary
dict1={}
dict2={}

# opens a tsv file to write and stores the tsv file into a variable.
f1 = open("p6.tsv", "w")
f2 = open("p95.tsv", "w")

# A for loop that goes through the length of specific index that has a list. 
for i in range(len(all_qscores[6])):
    
    # If statement that checks if the value in the list is in the dictionary.
    if all_qscores[6][i] in dict1.keys():
        
        # If true then add a 1 to the value of the key. 
        dict1[all_qscores[6][i]]+=1
                  
                   
    else:
        
        # If false, then store 1 as a value for the key.
        dict1[all_qscores[6][i]]=1
   
       
    
# A for loop that goes through the length of specific index that has a list. 
for i in range(len(all_qscores[95])):
    
    # If statement that checks if the value in the list is in the dictionary.
    if all_qscores[95][i] in dict2.keys():
       
        # If true then add a 1 to the value of the key. 
        dict2[all_qscores[95][i]]+=1
                  
                   
    else:
        
        # If false, then store 1 as a value for the key.
        dict2[all_qscores[95][i]]=1
 
# A for loop that goes through the items in the dictionary.
for key, value in dict1.items():
    
    # writes the formatted output to the tsv file.
    f1.write("{0}\t{1}\n".format(key,value))
    
f1.close()
    
# writes the formatted output to the tsv file.    
for key, value in dict2.items():
    
    # writes the formatted output to the tsv file.
    f2.write("{0}\t{1}\n".format(key,value))
    
f2.close()





# In[2]:



# A for loop that goes through the items in the dictionary.
for key, value in dict1.items():
    
    # Plots the distribution of quality scores of a specific index position 
    # in the array.
    plt.bar(key,value)
    
# Labels a title
plt.title('p6')

# Labels X axis
plt.xlabel('Mean Quality Score')

# Labels Y axis
plt.ylabel('Number of occurrences')


# In[3]:


#Use this cell to generate your position 95 plot in Jupyter.
#Otherwise, issue a print statement so that the name of your plot file is printed.

# A for loop that goes through the items in the dictionary.
for key, value in dict2.items():
    
    # Plots the distribution of quality scores of a specific index position 
    # in the array.
    plt.bar(key,value)
    
# Labels a title
plt.title('p95')

# Labels X axis
plt.xlabel('Mean Quality Score')

# Labels Y axis
plt.ylabel('Number of occurrences')


# In[ ]:




