#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import geohash as geohash
import csv

class Data:
    def __init__(self):
        self.time = ""
        self.city = ""
        self.district = ""
        self.longitude = 0
        self.latitude = 0
        self.geohash = ""

class CvsToGeohash:

    def __init__(self):
        # init precision = 12
        self._precision = 12

    def csvfile_to_geohush(self,file_in,file_out,precision):
        
        if(precision!=None):
            self._precision = precision

        list_data = list()

        #open CSV file
        with open( file_in , newline='') as csvfile:

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
                    data.geohash = geohash.encode(float(row[5]), float(row[4]), self._precision)

                    # pushback
                    list_data.append(data)


        # sort by city and district
        list_data = sorted( list_data, key=lambda data:(data.city,data.district), reverse=False )

        print("total data:" + str(len(list_data)))

        # 開啟輸出的 CSV 檔案並寫入
        with open( file_out , 'w+', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['Longitude', 'Latitude', 'Geohash','Time', 'City', 'District'])

            for i in range(len(list_data)):
            # print (str(list_data[i].time) + "," + str(list_data[i].city) + "," + str(list_data[i].district) +"," + str(list_data[i].longitude) + "," + str(list_data[i].latitude)+ "," + str(list_data[i].geohash))
                writer.writerow([list_data[i].longitude,list_data[i].latitude,list_data[i].geohash,list_data[i].time,list_data[i].city,list_data[i].district])


    def csvdir_to_geohush(self,dir_in,file_out,precision):
       
        files = os.listdir(dir_in)

        if(precision!=None):
            self._precision = precision

        list_data = list()

        for i in range(len(files)):
            
            file_in = dir_in + "/" +files[i]
            print(file_in)
            
            #open CSV file
            with open( file_in , newline='') as csvfile:
            
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
                        data.geohash = geohash.encode(float(row[5]), float(row[4]), self._precision)

                        # pushback
                        list_data.append(data)

        # sort by city and district
        list_data = sorted( list_data, key=lambda data:(data.city,data.district), reverse=False )

        print("total data:" + str(len(list_data)))
       
        # 開啟輸出的 CSV 檔案並寫入
        with open( file_out , 'w+', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['Longitude', 'Latitude', 'Geohash','Time', 'City', 'District'])

            for i in range(len(list_data)):
            # print (str(list_data[i].time) + "," + str(list_data[i].city) + "," + str(list_data[i].district) +"," + str(list_data[i].longitude) + "," + str(list_data[i].latitude)+ "," + str(list_data[i].geohash))
                writer.writerow([list_data[i].longitude,list_data[i].latitude,list_data[i].geohash,list_data[i].time,list_data[i].city,list_data[i].district])

    