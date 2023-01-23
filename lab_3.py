import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random

station_ls = []
station_ob_ls = []

class Stations():
    def __init__(self, name):
        self.name = name
        self.mtemp = []

with open('BigData2016 (1).csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        if row["STID"] not in station_ls:
            station_ls.append(row["STID"])
            station_ob_ls.append(Stations(row["STID"]))

    csvfile.seek(0)

    for row in reader:
        for station in station_ob_ls:
            if station.name == row["STID"]:
                if float(row["TMAX"]) > -996:
                    station.mtemp.append(float(row["TMAX"]))

    print(station_ls)
    print(station_ob_ls)

    for station in station_ob_ls:
        print(station.name)
        print(station.mtemp)

        plt.plot(station.mtemp)
        plt.ylabel("Temperature")
        plt.xlabel("Day")

    plt.legend(station_ls)
    plt.show()

