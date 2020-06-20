from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import requests
import csv

r = requests.get('https://pythonprogramming.net/yahoo_finance_replacement')
with open('dt.txt','w',newline='') as dfile:
	data = dfile.writelines(r.text)
with open('dt.txt','r') as csvfile:
	csv_reader = csv.reader(csvfile)
	header = next(csv_reader)
	data = []
	for line in csv_reader:
		Date = datetime.strptime(line[0],'%Y-%m-%d')
		Open = float(line[1])
		High = float(line[2])
		Low = float(line[3])
		Close = float(line[4])
		Adj_close = float(line[5])
		Volume =  float(line[6])
		data.append([Date,Open,High,Low,Close,Adj_close,Volume])
	date = [row[0] for row in data]
	open_p = [row[1] for row in data]
	high_p = [row[2] for row in data]
	low_p = [row[3] for row in data]
	close_p = [row[4] for row in data]
	adj_close = [row[5] for row in data]
	volume = [row[6] for row in data]

	plt.plot_date(date,high_p,color='blue',linewidth=1,linestyle='-',marker='.',markersize=1,markeredgecolor='r',label='high price')

	plt.xlabel('time')
	plt.ylabel('price(bilion $)')
	plt.title('TSLA stock \n daily high price in 18 years')
	plt.legend()
	plt.show()