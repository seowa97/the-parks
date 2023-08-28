import csv
from app import app
from traffic_spot import Traffic

# git test 

park_list = {}  # park list = [traffic spot: traffic object]
NP_list = {}    # NP_list = [national park: list of traffic spots]

'''
0: ParkName
1: UnitCode (x)
2: ParkType (x)
3: Region (x)
4: TrafficCounter
5: Year
6: Month
7: TrafficCount
8: ParkNameTotal (x)
9: UnitCodeTotal (x)
10: ParkTypeTotal (x)
11: RegionType (x)
12: TrafficCountTotalLabel (x)
13: YearTotal (x)
14: TrafficCountTotal
'''

# with open("Query Builder for Traffic Counts (1985 - Last Calendar Year).csv", "r") as data_file:
with open("csv_files/test.csv", "r") as data_file:
    
    reader = csv.reader(data_file)
    headers = next(reader)

    # for determining index of csv items, listed above
    # for n,i in enumerate(headers):
    #     print(f"{n}: {i}")

    for line in reader:
        if not line:
            break

        try:            
            line[4] = line[4][17:]
            if line[4][0] == "t":
                line[4] = "ALL VEHICLES"
        except:
            break

        # creates traffic spot object and adds to map; park list = [traffic spot: traffic object]
        # if traffic spot is already in map, add month and count to object varable

        line[6] = int(line[6])
        line[7] = int(line[7].replace(",",""))
        line[14] = int(line[14].replace(",",""))

        if line[4] not in park_list:
            park_traf = Traffic(line[0], line[4], line[14])
            park_traf.add_to_map(line[6], line[7])
            park_list[line[4]] = park_traf
        else:
            park_list[line[4]].add_to_map(line[6], line[7])


        if line[0] not in NP_list:
            NP_list[line[0]] = []

        if line[4] not in NP_list[line[0]]:
            NP_list[line[0]].append(line[4])


    park_list['SAND BEACH'].plot_data()
    # park_list['SAND BEACH'].interpolate()




    # for i in park_list:
    #     print(f"{i} in {park_list[i].park}.")
    #     park_list[i].print_counter()




