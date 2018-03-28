import csv

with open('sampleData.csv', 'r') as csv_file: #this line opens up the file using a context manager 'r' denote read
	csv_reader = csv.reader(csv_file) #This is a reader method usies ";" as a delimiter by default

	for line in csv_reader:
		print(line)