#!/usr/bin/python

from pymongo import MongoClient
import os
import csv

path   = os.path.dirname("./data/")
client = MongoClient()
db     = client.bike_share

rebalancing = db.rebalancing
stations    = db.stations
trips       = db.trips
weather     = db.weather

collections = [rebalancing, stations, trips, weather]

# grab only our csv files for import
def get_data_files(path):
    file_list = os.listdir(path)
    csv_files = []
    for data_file in file_list:
        if data_file.endswith(".csv") is True:
            csv_files.append(data_file)
    return csv_files

# map the header rows, data rows, and collections, and add
# a document for each row in the file
def insert_data_mongo(filename, collection):
    file_path = os.path.join(path, filename)
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = reader.next()
        print "Filename: {fn} header: {hd}".format(fn=file_path, hd=header)
        for row in reader:
           document = dict(zip(header, row))
           collection.insert(document)
           # print document

# run all the things
def main():
    file_list = get_data_files(path)
    csv_file_map = dict(zip(file_list, collections))
    for csv, coll in csv_file_map.iteritems():
        insert_data_mongo(csv, coll)

if __name__ == '__main__':
    main()