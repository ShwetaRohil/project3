import numpy as np
import pandas as pd
f1 = open("gmail_5.2.2.txt")
data_list = [] # create empty data list for parsing file data
list_loc_dict = {} # create dictionary to store key value pair of number of words/columns and its list location
pattern_dict = {}
error_messages={}
lines = f1.readlines()
for line in lines:
    words = line.lower().split() # convert line to lower case and split into words
    count = len(words)

    if count not in list_loc_dict.keys(): # if column/word count key not found in dictionary 
        list_loc_dict[count] = len(data_list) # add key value pair in dictionary
        data_list.append([]) # append empty list into the list to create list of list
    data_list[list_loc_dict[count]].append(words) # append list to list of list element with the help of dictionary for index of list

f1.close()

list_len = len(data_list) # length of base list
pattern_list = [ [] for _ in range(list_len)] # Empty lists of list for storing patterns of different sizes

for i in range(list_len): # loop for traversing base list for loading into numpy array
    np1=np.array(data_list[i]) # create array from list of list elements
    element_len = len(data_list[i][0])
    for j in range(element_len): # Loop for columner comparison
        first_row_cols = np1[0,j] # store value of first row and colmun index j
        if np.all(np1[:,j]==first_row_cols): # if all column values are same as first row and related col value
            pattern_list[i].append(first_row_cols) #  store the same to pattern
        else:
            pattern_list[i].append('*') # else store * to pattern
    pattern_string = ' '.join(pattern_list[i])
    pattern_string=pattern_string.replace("* *","*")
    pattern_dict[pattern_string] = element_len
    str_list=[]
    for k in data_list[i][0:1]:
        str_list.append(" ".join(k))
    error_messages[pattern_string] =str_list 

for i in error_messages.keys():
    print(i)