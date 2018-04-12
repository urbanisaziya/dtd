import csv

def OpenFile():
    filename = 'TestGameSessions.csv'
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        dataset=dict()
        for row in reader:
            max_time = 0
            if int(row['time']) > max_time:
                max_time = int(row['time'])
            delta_time = 1209600
            if row['udid'] not in dataset:
                dataset[row['udid']] = []
            dataset[row['udid']].append([row['time'], row['count'], row['avg_duration']])
        for row['udid'] in dataset:
            print(row['udid'], dataset[row['udid']])
        print(max_time)

        

            #print(row['udid'], row['time'], row['count'], row['avg_duration']) 

OpenFile()
