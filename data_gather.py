#!/usr/bin/python

import os
import csv

path = os.path.dirname("./data/")

def get_data_files(path):
    file_list = os.listdir(path)
    return file_list

files = get_data_files(path)
for data_file in files:
    # note: this code grabs the file extension so we can exclude the .txt readme file.
    # there is probably a much better way to do this, like regex, but this works.
    extension = data_file[(len(data_file)-3):len(data_file)]
    if extension != 'txt':
        print "File name: %s " % data_file
