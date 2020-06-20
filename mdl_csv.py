    #without csv
# with open('dt.txt','r') as dt1:
# 	data1 = dt1.readlines()
# 	lines = [line for line in data] #list comprehension
# 	print(lines)
# 	print(lines[0].strip().split(',')) #strip=remove white space and even newlines,split=devid the string into smzller peices
# 	data_set = [line.strip().split(',') for line in lines]
# 	print(data_set[0])
# 	print(data_set[0][0])

#_____________________________________________________________________

                    #with csv
# import csv
# from datetime import datetime 	

 	#write a csv

# # print(dir(csv))
# with open('dt.txt','r',newline='') as dt2: #newline=replace '\n' with ''
# 	#read a csv
# 	reader = csv.reader(dt2) #read a file as a csv file
# 	header = next(reader) #next()=to remove the first line and consider it as a header
# 	# data = [row for row in reader] 
# 	# print(header)
# 	# print(data)
# 	data = []
# 	for row in reader:
# 		date = datetime.strptime(row[0], '%Y-%m-%d') #strptime=string_parsr_time
# 		open_price = float(row[1])
# 		high_p = float(row[2])
# 		low_p = float(row[3])
# 		close_p = float(row[4])
# 		volume = float(row[5])
# 		adj_close = float(row[6])
# 		data.append([date,open_price,high_p,low_p,close_p,volume,adj_close])
 	 #write a csv

# 	with open('tslareturnes.txt','w',newline='') as tsl:
# 		writer = csv.writer(tsl) #read a file as a csv
# 		writer.writerow(['date','returns']) #writerow = write 1 line writerows = write multiple lines
# 		for i in range(len(data)-1):
# 		    todays_row = data[i]
# 		    todays_date = todays_row[0]
# 		    todays_price = todays_row[-1]
# 		    yesterday_row = data[i+1]
# 		    yesterday_price = yesterday_row[-1]
# 		    daily_return = (todays_price-yesterday_price)/yesterday_price
# 		    formated_date = todays_date.strftime('%m-%d-%Y')
# 		    writer.writerow([formated_date,daily_return])

#_____________________________________________________________________
import csv

    # read text as csv file

# with open('dt.txt','r') as csvfile:
# 	csv_reader = csv.reader(csvfile) #csv.reader(csvfile) ==csv.reader(csvfile,delimiter=',') 
# 	print(csv_reader) #its going to say that csv_reader is just an object in memory
# 	header = next(csv_reader)
# 	for line in csv_reader:
# 		print(line)

   # write text as csv file

# with open('dt.txt','r') as csvfiler:
# 	csv_reader = csv.reader(csvfiler,delimiter=',')
# 	with open('newcsvfile.csv','w',newline='') as csvfilew:
# 		csv_writer = csv.writer(csvfilew,delimiter=',') #or delimiter='\t'
# 		for line in csv_reader:
# 			csv_writer.writerow(line)
 
   # read csv file as dict

# with open('dt.txt','r') as csvfilerd:
# 	csv_dreader = csv.DictReader(csvfilerd,delimiter=',') #
# 	for line in csv_dreader:
# 		print(line)
# 		print(line['Date'])


  # write csv file as dict

# with open('dt.txt','r') as csvfilerd:
# 	csv_dreader = csv.DictReader(csvfilerd,delimiter=',')
# 	with open('dictcsv.csv','w') as csvfilewd:
# 		field_names = ['Date','Open','High','Low','Close','Adjusted_close','Volume']
# 		csv_dwriter = csv.DictWriter(csvfilewd,fieldnames=field_names,delimiter=',') #DictWriter(file,fieldnames)
# 		csv_dwriter.writeheader() #to write the field names as headers 
# 		for line in csv_dreader:
# 			csv_dwriter.writerow(line)
			#or you can delete a field
			# del line['Volume'] #you need to delete 'Volume' also from field_names ;del=for delting in python
			# csv_dwriter.writerow(line)