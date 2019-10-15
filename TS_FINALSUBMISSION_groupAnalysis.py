#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scene-cat problem set for PSY 1210 - Fall 2018

@author: Michael Mack
"""

#%% import block 
import numpy as np
import scipy as sp
import scipy.stats
import os
import shutil

#%%
# copy files from testing room folders to raw data, rename files to include
# testing room letter in the filename


testingrooms = ['A','B','C']

for A in testingrooms:
    filepath = os.path.join('/Users/tianasimovic/Documents/GitHub/Tiana/ps2-tianas/testingroomA/','experiment_data.csv')
    newpath = os.path.join('/Users/tianasimovic/Documents/GitHub/Tiana/ps2-tianas/rawdata/','experiment_data_A.csv')
shutil.copyfile(filepath, newpath)

for B in testingrooms:
    filepath = os.path.join('/Users/tianasimovic/Documents/GitHub/Tiana/ps2-tianas/testingroomB/','experiment_data.csv')
    newpath = os.path.join('/Users/tianasimovic/Documents/GitHub/Tiana/ps2-tianas/rawdata/','experiment_data_B.csv')
shutil.copyfile(filepath, newpath)

for C in testingrooms:
    filepath = os.path.join('/Users/tianasimovic/Documents/GitHub/Tiana/ps2-tianas/testingroomC/','experiment_data.csv')
    newpath = os.path.join('/Users/tianasimovic/Documents/GitHub/Tiana/ps2-tianas/rawdata/','experiment_data_C.csv')
shutil.copyfile(filepath, newpath)

#%%
# read in all the data files in rawdata directory using a for loop
# columns: subject, stimulus, pairing, accuracy, median RT


data = np.empty((0,5))
for room in ['A','B','C']:
    filename = '/Users/tianasimovic/Documents/GitHub/Tiana/ps2-tianas/rawdata/experiment_data_'+room+'.csv'
    tmp = sp.loadtxt(filename,delimiter=',')
    data = np.vstack([data, tmp])
print(data)

#%%
# calculate overall average accuracy and average median RT


acc = data[:,3]
avg_acc = np.mean(acc)*100   
print("Overall average accuracy =", round(avg_acc, 2), "%")

mrt = data[:,4]
avg_mrt = np.mean(mrt)   
print("Overall average median RT =", round(avg_mrt, 1), "ms")

#%%
# calculate averages (accuracy & RT) split by stimulus using a for loop and an 
# if statement. (i.e., loop through the data to make a sum for each condition, 
# then divide by the number of data points going into the sum)


# Isolating stimulus, accuracy, and mRT elements from master data

stim = data[:,1]
acc = data[:,3]
mrt = data[:,4]

# Making a new list containing only stimulus, accuracy, and mRT elements

stim_data = [[s, a, rt] for s, a, rt in zip(stim, acc, mrt)]
print(stim_data)

# Breaking stim_data into two lists per stimulus using for loop

words = []
faces = []
for item in stim_data:
    if item[0] == 1.0:
        words.append(item)
    sumWords = np.sum(words, 0)
    if item[0] == 2.0:
        faces.append(item)
    sumFaces = np.sum(faces, 0)
    
# Calculating averages for words stimulus set
    
WordsAvgAcc = (sumWords[1]/len(words))*100
print("Average accuracy of words =", round(WordsAvgAcc, 1), "%")

WordsAvgmRT = (sumWords[2]/len(words))
print("Average median RT of words =", round(WordsAvgmRT, 1), "ms")

# Calculating averages for faces stimulus set

FacesAvgAcc = (sumFaces[1]/len(faces))*100
print("Average accuracy of faces =", round(FacesAvgAcc, 1), "%")

FacesAvgmRT = (sumFaces[2]/len(faces))
print("Average median RT of faces =", round(FacesAvgmRT, 1), "%")

#%%
# calculate averages (accuracy & RT) split by congruency using indexing, 
# slicing, and numpy's mean function 
# wp - white/pleasant, bp - black/pleasant
# (hint: only one line of code is needed per average)


# Isolating pairing, accuracy, and mRT elements from master data

pair = data[:,2]
acc = data[:,3]
mrt = data[:,4]

# Making a new list containing only pairing, accuracy, and mRT elements

pair_data = [[p, a, rt] for p, a, rt in zip(pair, acc, mrt)]
print(pair_data)

# Breaking pair_data into two lists per pairing using for loop

wp = []
bp = []
for item in pair_data:
    if item[0] == 1.0:
        wp.append(item)
        
    if item[0] == 2.0:
        bp.append(item)

wpAcc = np.array(wp)[:,1]
wpmRT = np.array(wp)[:,2]
bpAcc = np.array(bp)[:,1]
bpmRT = np.array(bp)[:,2]

# Calculating averages for white/pleasant pairing set

wpAvgAcc = (np.mean(wpAcc))*100
print("Average accuracy of white/pleasant =", round(wpAvgAcc, 1), "%")

wpAvgmRT = np.mean(wpmRT)
print("Average median RT of white/pleasant =", round(wpAvgmRT, 1), "ms")

# Calculating averages for black/pleasant pairing set

bpAvgAcc = (np.mean(bpAcc))*100
print("Average accuracy of black/pleasant =", round(bpAvgAcc, 1), "%")
  
bpAvgmRT = np.mean(bpmRT)
print("Average median RT of black/pleasant =", round(bpAvgmRT, 1), "ms")

#%% 
# calculate average median RT for each of the four conditions
# use for loops, indexing/slicing, or both!
# (hint: might be easier to slice data into separate words and faces datasets)


# Splitting up each condition into separate arrays using for loop

print(data)

cond1 = []
cond2 = []
cond3 = []
cond4 = []
for item in data:
    if item[1] == 1.0: 
        if item[2] == 1.0:
            cond1.append(item)
        if item[2] == 2.0:
            cond2.append(item)
    if item[1] == 2.0:
         if item[2] == 1.0:
            cond3.append(item)
         if item[2] == 2.0:
            cond4.append(item)

# Finding the average of the mRT element per condition array
            
cond1mRT = np.array(cond1)[:,4]
cond1AvgmRT = (np.mean(cond1mRT))
print("Average median RT of Condition 1 (words - white/pleasant) =", round(cond1AvgmRT, 1), "ms")

cond2mRT = np.array(cond2)[:,4]
cond2AvgmRT = (np.mean(cond2mRT))
print("Average median RT of Condition 2 (words - black/pleasant) =", round(cond2AvgmRT, 1), "ms")

cond3mRT = np.array(cond3)[:,4]
cond3AvgmRT = (np.mean(cond3mRT))
print("Average median RT of Condition 3 (faces - white/pleasant) =", round(cond3AvgmRT, 1), "ms")

cond4mRT = np.array(cond4)[:,4]
cond4AvgmRT = (np.mean(cond4mRT))
print("Average median RT of Condition 4 (faces - black/pleasant) =", round(cond4AvgmRT, 1), "ms")

#%%        
# compare pairing conditions' effect on RT within stimulus using scipy's 
# paired-sample t-test: scipy.stats.ttest_rel()


import scipy.stats

# Comparing within Word stimulus (Conditions 1 and 2)

tWords = scipy.stats.ttest_rel(cond1mRT, cond2mRT)

print("t-value within Word stimulus =", round(tWords[0], 2))
print("p-value within Word stimulus =", tWords[1])


# Comparing within Face stimulus (Conditions 3 and 4)

tFaces = scipy.stats.ttest_rel(cond3mRT, cond4mRT)

print("t-value within Face stimulus =", round(tFaces[0], 2))
print("p-value within Face stimulus =", tFaces[1])


#%%
# print out averages and t-test results
# (hint: use the ''.format() method to create formatted strings)


# apologies for already printing out the sentential answers in each step.
# I didn't read ahead to this step when I was calculating those!
# I left them in because it helped me get used to that format, and I would like
# to remember those steps when I review this later. I hope that is OK! :)


print('\nOVERALL AVERAGES: {:.2f}%, {:.1f}ms'.format(avg_acc,avg_mrt))

print('\nWORDS - AVERAGES: {:.1f}%, {:.1f}ms'.format(WordsAvgAcc,WordsAvgmRT))
print('\nFACES - AVERAGES: {:.1f}%, {:.1f}ms'.format(FacesAvgAcc,FacesAvgmRT))

print('\nWHITE/PLEASANT - AVERAGES: {:.1f}%, {:.1f}ms'.format(wpAvgAcc,wpAvgmRT))
print('\nBLACK/PLEASANT - AVERAGES: {:.1f}%, {:.1f}ms'.format(bpAvgAcc,bpAvgmRT))

print('\nCONDITION 1 - AVG MEDIAN RT: {:.1f}ms'.format(cond1AvgmRT))
print('\nCONDITION 2 - AVG MEDIAN RT: {:.1f}ms'.format(cond2AvgmRT))
print('\nCONDITION 3 - AVG MEDIAN RT: {:.1f}ms'.format(cond3AvgmRT))
print('\nCONDITION 4 - AVG MEDIAN RT: {:.1f}ms'.format(cond4AvgmRT))

print('\nt-VALUE - WITHIN WORD STIMULUS: {:.2f}'.format(tWords[0]))
print('\np-VALUE - WITHIN WORD STIMULUS:', (tWords[1]))

print('\nt-VALUE - WITHIN FACE STIMULUS: {:.2f}'.format(tFaces[0]))
print('\np-VALUE - WITHIN FACE STIMULUS:', (tFaces[1]))

