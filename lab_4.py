import csv
import matplotlib as mpl
import matplotlib.pyplot as plt


class Stations():
    def __init__(self, name):
        self.name = name
        self.ls = []


running = True
while running:
    #first loop
    uName = input("name: ")

    with open('2016VizData.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        loopRun = True
        while loopRun:
            #second loop
            csvfile.seek(0)

            station_ls = []
            station_ob_ls = []

            for row in reader:
                if row["STID"] not in station_ls:
                    station_ls.append(row["STID"])
                    station_ob_ls.append(Stations(row["STID"]))

            category = None
            category = input(f"{uName}, would you like to look at - max temperature-TMAX, min temperature-TMIN, wind speed-WSMX/WSMN, humidity-HAVG, rain totals-RAIN: ")

            time = None
            time = input("would you like to look at a - month, year: ")

            if time == 'year':
                data_ls = []
                csvfile.seek(0)
                for row in reader:
                    for station in station_ob_ls:
                        if station.name == row["STID"]:
                            if float(row[category]) > -996:
                                station.ls.append(float(row[category]))
                
            else:
                month = None
                month = input("which month would you like to look at, 1-12: ")
                
                data_ls = []
                csvfile.seek(0)
                for row in reader:
                    for station in station_ob_ls:
                        if station.name == row["STID"]:
                            if row["MONTH"] == month:
                                if float(row[category]) > -996:
                                    station.ls.append(float(row[category]))
                print(f"list: {data_ls}")

            for station in station_ob_ls:
                plt.plot(station.ls)

            plt.ylabel(category)
            plt.xlabel("Day")
            plt.legend(station_ls)
            plt.show()