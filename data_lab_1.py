import csv

with open('Norman2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    def max_temp():
        ls = []
        for row in reader:
            ls.append((row['TMAX']))
        nls = []
        for e in ls:
            if e not in ('-996.00'):
                nls.append(e)
        return(max(ls))

    def min_temp():
        ls = []
        for row in reader:
            ls.append((row['TMIN']))
        nls = []
        for e in ls:
            if e not in ('-996.00'):
                nls.append(e)
        for i in range(len(nls)):
            nls[i] = float(nls[i])

        return(float(nls[nls.index(min(nls))]))

    def av_max_temp():
        sum = 0
        ls = []
        for row in reader:
            ls.append((row['TMAX']))
        nls = []
        for e in ls:
            if e not in ('-996.00'):
                nls.append(e)
        for i in range(len(nls)):
            sum += float(nls[i])
        return(round(sum/len(nls), 2))

    def av_min_temp():
        sum = 0
        ls = []
        for row in reader:
            ls.append((row['TMIN']))
        nls = []
        for e in ls:
            if e not in ('-996.00'):
                nls.append(e)
        for i in range(len(nls)):
            sum += float(nls[i])
        return(round(sum/len(nls), 2))

    print(av_min_temp())

