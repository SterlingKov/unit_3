import csv
station_ls = []

#MAX
def stat_ls_max(station_name):
    csvfile.seek(0)
    nlist = []
    for row in reader:
        if row["STID"] == station_name:
            nlist.append(float(row["TMAX"]))
    return max(nlist)


def get_station_names():
    if row["STID"] not in station_ls:
        station_ls.append(row["STID"])

#MIN
def stat_ls_min(station_name):
    csvfile.seek(0)
    nlist = []
    for row in reader:
        if row["STID"] == station_name and float(row["TMIN"]) > -996.0:
            nlist.append(float(row["TMIN"]))
    return min(nlist)

#loop
with open('BigData2016 (1).csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        get_station_names()

    for station in station_ls:
        print(stat_ls_min(station))

    print(' ')

    for station in station_ls:
        print(stat_ls_max(station))


