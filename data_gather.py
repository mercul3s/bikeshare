#!/usr/bin/python

import os
import csv

path = os.path.dirname("./data/")

def get_data_files(path):
    file_list = os.listdir(path)
    return file_list

def loop_files(files):
    for data_file in files:
        if data_file.endswith(".csv"):
            file_path = os.path.join(path, data_file)
            print "File path: %s " % file_path
            with open(file_path, 'r') as csvfile:
                counter = 0
                # fileDialect = csv.Sniffer().sniff(csvfile.read(1024), delimiters=",")
                # csvfile.seek(0)
                reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                print dir(reader)
                # for row in reader: 
                    # print ', '.join(row)

def main():
    file_list = get_data_files(path)
    loop_files(file_list)
if __name__ == '__main__':
    main()