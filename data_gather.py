#!/usr/bin/python

from pymongo import MongoClient
import os
import csv

path = os.path.dirname("./data/")
client = MongoClient()
db = client.bike_share

rebalancing = db.rebalancing
stations    = db.stations
trips       = db.trips
weather     = db.weather

collections = [rebalancing, stations, trips, weather]

def get_data_files(path):
    file_list = os.listdir(path)
    csv_files = []
    for data_file in file_list:
        if data_file.endswith(".csv") is True:
            csv_files.append(data_file)
    return csv_files

def loop_files(filename, collection):
    file_path = os.path.join(path, filename)
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = reader.next()
        print "Filename: {fn} header: {hd}".format(fn=file_path, hd=header)
        for row in reader:
           document = dict(zip(header, row))
           collection.insert(document)
           # print document

def main():
    file_list = get_data_files(path)
    # print file_list

    csv_file_map = dict(zip(file_list, collections))
    # print csv_file_map

    for csv, coll in csv_file_map.iteritems():
        loop_files(csv, coll)

if __name__ == '__main__':
    main()