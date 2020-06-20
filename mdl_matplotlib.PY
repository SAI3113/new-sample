import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates
# import csv
#1 x = [1,2,3]
#1y = [5,7,4]
#1 x2 = [1,2,3]
#1 y2 = [6,4,7]
#1 plt.plot(x,y,label='first line')
#1 plt.plot(x2,y2,label='second line')
#2 x =[2,4,6,8,10]
#2 y =[6,7,8,4,2]
#2 x2 =[1,2,4,5,7]
#2 y2 =[5,4,6,6,7]
#2 plt.bar(x,y,label='bar1')
#2 plt.bar(x2,y2,label='bar2')
#3&4 age_population=[14,55,20,14,8,6,44,58,23,47,58,62,11,24,88,98,44,42,66,87,33]
#3 x=age_population list length
#3 plt.bar(ids,age_population,label='population') #the ids means nothing(shows the oldest)
#4 bins=[0,10,20,30,40,50,60,70,80,90] #evry number contains an interval:[0,10],[10,20]...
#4 plt.hist(age_population,bins,label='hist',histtype='bar',rwidth=0.8) #bins=an interval
#5 x =[2,4,6,8,10,11,1]
#5 y =[6,7,8,4,2,5,3]
#5 plt.scatter(x,y,label='scatter',color='r',marker='*',s=500) #marker=shape (o,*,s,+,...)  , s=size
#6 days = [1,2,3,4,5]

#6 sleeping = [7,5,8,11,6]
#6 eating = [2,3,2,1,3]
#6 playing =[4,5,6,4,3]
#6 working =[4,8,9,7,4]

#6 plt.stackplot(days,eating,sleeping,playing,working,colors=['red','blue','m','green'],labels=['eating','sleeping','playing','working'],linewidth=1) #line=the seperating
'''
if you cant make legends in a type of graphe just creat a fake one,for the previous example:
plt.plot([],[],color='red',label='eating,linewidth=2') 
plt.plot([],[],color='blue',label='sleeping') 
plt.plot([],[],color='m',label='playing,linewidth=5') 
plt.plot([],[],color='green',label='working') 
'''
#7 slices = [3,8,6,4]
#7 activities = ['eating','sleeping','playing','working']
#7 cols= ['red','blue','m','green']
#7 plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow= True,explode=(1,0,0,0),autopct='%1.1f%%') #you may want to discard x & y labels & the legends
'''
startangle=starting angle
shadow=3D aspect (add shadow)
explode= grabe a slice
autopct=add percentage to the pie
'%1.1f%%'=just a code to add percentage
'''

#8 x = []
#8 y = []
#8 with open('w.txt','r') as csvfile:   #w.txt=2 values in one line
#8 	plots = csv.reader(csvfile,delimiter=',')
#8 	for line in plots:
#8 		x.append(int(line[0]))
#8 		y.append(int(line[1]))
#8 plt.plot(x,y,label='w')

#8 x,y = np.loadtxt('w.txt',delimiter=',',unpack=True) #unpack means unpack the values seperated with ',' into X & Y
#8 plt.plot(x,y,label='w')
     

                             #the date handling
#9-1 def bytespdate2num(fmt,encoding='utf-8'):  #convert_bytes_date_to_number(formate,type of code 'utf-8')
#9-1	strconverter = mdates.strpdate2num(fmt) #string_parse_date(ex:Y%-m%-d%)_to_number(formate) = the formate part 
#9-1 	#the web handling
#9-1  	def bytesconverter(b):  #decode the utf-8 = the encoding part    b='bytes'
#9-1  		s = b.decode(encoding) #decode(utf-8)  to  s='string'
#9-1  		return strconverter(s) #convert bytes to string(formate decoded) return the formate decoded
#9-1  	return bytesconverter #return the date data in a decoded formate = a string  

#9-1 def graph_data(stock): #the graph
#9-1  	stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement' #the stock API
#9-1  	source_code = urllib.request.urlopen(stock_price_url).read().decode() #urllib.request.urlopen(the stock API).read(the site).decode(utf-8) 	stock_data =[] #site data
#9-1  	split_source = source_code().split('\n') #split_source = all the data splited with a new line
#9-1  	for line in split_source: #check evry each line 
#9-1  		split_source = line.split(',') #check the lines splited with ','
#9-1  		if len(split_source) == 7: #if the lines splited have 7 items do
#9-1  			if 'date' not in split_source: #if the lines splited does not include 'date' do
#9-1 				stock_data().append(split_source) #add the lines splited to data
#9-1  	Date,Openp,Highp,Lowp,Close,Adjusted_closep,Volume = np.loadtxt(stock_data,delimiter=',',unpack=True,converters={0: bytespdate2num('%Y-%m-%d')}) #assigne the 7 data to variables

#9-1  	plt.plot_date(date,closep,label='price') #creat the plot	
#9-1  	plt.xlabel('date')
#9-1      plt.ylabel('price')
#9-1      plt.title('stock')
#9-1      plt.legend()
#9-1      plt.show()
#9-1  graph_data('TSLA')

#10 fig = plt.figure()    #to add subplots
#9 ax1 = plt.subplot2grid((1,1),(0,0))  #ax1= subplot(shape,location)
#9 x,y= np.loadtxt('w.txt',delimiter=',',unpack=True)  
#9 ax1.plot(x,y,label='data',color='red',linewidth=0.8,marker='p',linestyle='solid')  #linestyle= "solid", "dotted", "dashed" or "dashdot"and More;marker= ",", ".", "s" or "p". More

#9 for label in ax1.xaxis.get_ticklabels(): #subplot.in_the_x_axis.the_ticklabels() 
#9 	label.set_rotation(45)  #rotation_degree(45°)
#9 ax1.grid(True,linewidth=0.5,linestyle='dashed',color='black')  #add_a_grid(=True,line_width,linestyle,color)




plt.xlabel('x')
plt.ylabel('y')
plt.title('graph')
#plt.subplots_adjust(bottom=0.16,left=0.16,right=0.9,top=1,wspace=0.2,hspace=0)  #figure paramataire
plt.legend()
plt.show()