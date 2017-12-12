#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:00 2017

@author: cnglab
"""
#to run LINUX command (FSL), set up OS. in python environment
import glob
import os
import shutil
import pdb

#def prepo(basedir):
    #print('Hello data in the path '+basedir)
    
#def main():
    #load in all the global variables prepro needs
#basedir='/Users/cnglab/Desktop/data'
    #prepo(basedir) #call prepo to do things 


#main()

#input=glob.glob('/Users/cnglab/Desktop/data/sub-*/func/sub-*_task-bart_bold.nii.gz')
#print(input[0:10])

#x=input[0]
#print('my path is '+x)
#y=x.split('/')
#print (y)
#sub=y[5] #make sure to print this sub to double check that we are grabbing the
#right thing
#whatcomp=y[2]

#print sub

#sub=input[1].split('/')[5] #combing all the commands below into one clean line! 
#print(sub) 

#subtask=input[1].split('/')[7].split('.')[0]
#subtask=subtask.strip('.nii.gz')
#print(subtask)

#output=subtask+'_brain'
#print(output)

# os.system('bet' x output '-F') 
# the command above does not work because python wants what in ()to just a abstrong

#os.system('bet %s %s -F'%(x, output)) # %s is a placeholder for whatever in the %())
#this gives you the output files to where the script lives

#input=glob.glob('/Users/gracer/Desktop/data/sub-*/func/sub-*.nii.gz')
#basedir='/Users/cnglab/Desktop/data'
#path=os.path.join(basedir,'sub-*','func','sub-*.nii.gz')
#print(path)
#input=glob.glob(path)
#len(input[1:5])
#print(input[0:2])
#os.path.exists(basedir)'
def prepro(basedir):
    basedir='/Users/cnglab/Desktop/data'
    for item in glob.glob(os.path.join(basedir,'sub-*','func','sub-*_task-bart_bold.nii.gz')):
        input=item
        output_path=item.split('.')[0]
        output=output_path+('_brain')
        os.system("/usr/local/fsl/bin/bet %s %s -F"%(input, output)) #input path to fsl here
        #pdb.set_trace() #debug as you go - give you the result of first item in the loop. You can comment this out after checking the first item
def main():
    basedir='/Users/cnglab/Desktop/data'
    prepro(basedir)

main()