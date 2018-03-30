import csv

in_file = open("sampleData.csv", "rb")
csv_reader_data = csv.reader(in_file)
header = next(csv_reader_data ) #Get the header of the CSV for fieldname
out_file = open("new_file.csv", "wb")
writer = csv.writer(out_file)
#print header
headerIndex = []
for line in header:
    if 'time' in line:
        print line, 'Index - ', header.index(line)
        headerIndex = headerIndex + [header.index(line)]
        print headerIndex
    else: 
        print 'fail'
for line2 in csv_reader_data:
    hms = ''
    for i in headerIndex:
        print line2[i], 'Index - ', i
        if line2[i] == '':
            line2[i] = 0
        seconds = int(line2[i])
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        hms = "%d:%02d:%02d" % (h, m, s)
        line2[i] = hms
        print hms
    writer.writerow(line2)