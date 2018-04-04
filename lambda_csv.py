import boto3
import csv

s3 = boto3.resource('s3')

def csv_converter(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    original_temp_filepath = '/tmp/' + key
    modified_temp_filepath = '/tmp/modified-'+ key
    modified_filename = 'modified-'+key
    
    s3.meta.client.download_file(bucket, key, original_temp_filepath)
    
    original_file = open(original_temp_filepath, "rb")
    csv_reader_data = csv.reader(original_file)
    
    header = next(csv_reader_data)
    
    modified_file = open(modified_temp_filepath, "wb")
    csv_writer_data = csv.writer(modified_file)
    
    headerIndex = []
    
    for line in header:
        if 'time' in line:
            headerIndex = headerIndex + [header.index(line)]
    csv_writer_data.writerow(header)
    
    for line2 in csv_reader_data:
        hms = ''
        for x in headerIndex:
            if line2[x] == '':
                line2[x] = 0
            seconds = int(line2[x])
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            hms = "%d:%02d:%02d" % (h, m, s)
            line2[x] = hms
        csv_writer_data.writerow(line2)
        modified_file.flush()
        #print(line2)
    
    temp_file = open(modified_temp_filepath, "rb")
    csv_reader_data2 = csv.reader(temp_file)
    
    for line3 in csv_reader_data2:
        print(line3)
        
    #s3.meta.client.upload_file(modified_temp_filepath, bucket, modified_filename)