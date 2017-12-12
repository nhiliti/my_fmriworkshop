#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:00 2017

@author: cnglab
"""
import glob
import os
import shutil

def prepo(basedir):
    print('Hello data in the path '+basedir)
    
def main():
    #load in all the global variables prepro needs
    basedir='/Users/cnglab/Desktop/data'
    prepo(basedir) #call prepo to do things 
    
main()