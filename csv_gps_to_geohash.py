#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import sys
import time
import geohash as geohash
import csv

def kill_self(*args):
    print(sys._getframe().f_code.co_name, sys._getframe(0).f_lineno)

class Data:
    def __init__(self):
        self.time = ""
        self.city = ""
        self.district = ""
        self.longitude = 0
        self.latitude = 0
        self.geohash = "" 
     
       
if __name__ == '__main__':

    signal.signal(signal.SIGINT, kill_self)
    
    list_data = list()

    path_csv = "./data/src/109_A1.csv"
    path_out = "./data/output/109_A1.csv"
    
    # import data
    # open CSV file
    with open( path_csv , newline='') as csvfile:

        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile, delimiter=',')

        # skip first row
        next(csvfile)
        
        # 以迴圈輸出每一列         
        for row in rows:
            
            # if have latitude
            if(row[5]):   
                
                data = Data()             
                data.time = row[0]          # time
                data.city = row[1][:3]      # city
                data.district = row[1][3:6] # district
                data.longitude = row[4]     # longitude
                data.latitude = row[5]      # latitude
                data.geohash = geohash.encode(float(row[5]), float(row[4]), precision=12)

                # pushback  
                list_data.append(data)

    # sort by city and district
    list_data = sorted( list_data, key=lambda data:(data.city,data.district), reverse=False )
        
    # 開啟輸出的 CSV 檔案並寫入
    with open( path_out , 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Time', 'City', 'District' , 'Longitude', 'Latitude', 'Geohash'])

        for i in range(len(list_data)):
            # print (str(list_data[i].time) + "," + str(list_data[i].city) + "," + str(list_data[i].district) +"," + str(list_data[i].longitude) + "," + str(list_data[i].latitude)+ "," + str(list_data[i].geohash))
            writer.writerow([list_data[i].time,list_data[i].city,list_data[i].district,list_data[i].longitude,list_data[i].latitude,list_data[i].geohash])
   
