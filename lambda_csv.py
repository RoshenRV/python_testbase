import csv

#FUNCTIONS
#-----------------------------------------------------------------------------------

def csv_dict_reader(csvFile_obj):
	csv_dictReader_data = csv.DictReader(csvFile_obj)
	

def csv_reader(csvFile_obj): #This function is to hold the fieldname for writing it back to CSV file
	csv_reader_data = csv.reader(csvFile_obj)
	header = csv_reader_data.next() #Get the header of the CSV for fieldname
	return header

#MAIN
#-----------------------------------------------------------------------------------
with open('sampleData.csv', 'r') as csv_file: #this line opens up the file using a context manager 'r' denote read
	csv_dict_rader(csv_file)
	csv_reader(csv_file)
	
	csv_reader = csv.DictReader(csv_file)#This is a reader method usies ";" as a delimiter by default
	csv_reader2 =  csv.reader(csv_file)
	i = csv_reader2.next()
	#next(csv_reader)
	for line in csv_reader:
		sum =  int(line['Nonproductive time']) - 15
		print(sum)
		
		
		
#	with open('new_file.csv', 'w') as new_file:
#		fieldnames = i
#		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
	#
	#	for line in csv_reader:
	#		csv_writer.writerow(line[4])