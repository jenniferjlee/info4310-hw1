# Simple post-processing script to create a clean subset of tree data
#     - JRz, for personal use and not indended for real world application

#  NOTE: This is eliminating valid, useful data in lieu of something easier to visualize
#        It's possible that this will mask trends, as it is often VERY likely that missing data are non-randomly distributed (e.g. more missing data pre-1955 in this dataset)


import csv

def passes_filter(row):
    # Filter criteria:
    #   Only listed trees that have full species name supplied
    if len(row['qSpecies']) < 1 or 'Tree(s) ::' in row['qSpecies']:
        return False
    #   Only trees that have a lat and lng provided
    elif len(row['Latitude']) < 1 or len(row['Longitude']) < 1:
        return False
    #   Only trees with valid SiteInfo
    elif len(row['qSiteInfo']) < 1 or row['qSiteInfo'] == ':':
        return False
    #   Only trees that have a DBH provided
    elif len(row['DBH']) < 1:
        return False
    else:
        return True

data = []
header = []
with open('Street_Tree_List-2020-08-20_RAW.csv','r') as f:
    reader = csv.DictReader(f)
    
    header = reader.fieldnames
    for row in reader:
        if passes_filter(row):
            data.append(row)

print(len(data))
           
with open('Street_Tree_List-2020-08-20_FILTERED.csv','w') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
