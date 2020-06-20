# f = open('hjfill.txt','r') #r-r+-w-a
# print(f.name) #the name
# print(f.mode) #the mode
# f.close() #you must close when you open a file
# with open('hjfill.txt','r') as f:   #it close automaticly
# 	pass
# print(f.closed)
# with open('hjfill.txt','r') as f:
	# f_readall=f.read()
	# print(f_readall)
	# f_isreadable=f.readable()
	# print(f_isreadable)
	# f_contents=f.readlines()
	# print(f_contents)
	# f_content=f.readline()
	# print(f_content,end='')  #end='' to remove the new line'\n' charactaire
	# f_content=f.readline()
	# print(f_content)
	# for line in f:
	# 	print(line,end='')
	# print(f.read(12))  #12 = size
	# print(f.read(100))
	# print(len(f.read()))  #count all the files charactaire
	# r_location = f.read(7)
	# print(f.tell()) #reading location
	# print(f.read(10))
	# f.seek(0) #set position
	# print(f.read(10))
# with open('hjfill.txt','r') as f:
# 	print(f.writable())
# with open('hjfill2.txt','w') as f:  #hjfill2 to creat a new file
#     f.write('test')
#     f.seek(0)
#     f.write('r')
# # to copy a file
# with open('hjfill2.txt','r') as rf:
# 	with open('hjfill_copy.txt','w') as wf:
# 		for line in rf:
#			wf.write(line)


#to work with image,ypu need to work with bytes no text
# with open('test.jpg','rb') as rf:   #rb = read bytes
# 	with open('test_copy.jpg','wb') as wf:  #wb = read bytes
# 		# to copy
# 		for line in rf:
# 			wf.write(line)
		# to also copy 
        # size_img = 4054
		# rf_size = rf.read(size_img)
		# while len(rf_size)>0:
		# 	wf.write(rf_size)
		# 	rf_size = rf.read(size_img)
# with open('hjfill2.txt','a') as ff:
# 	ff.write('h')
# from random import randint as ran
# with open('w.txt','w') as nef:
# 	i = 0
# 	for k in range(51):
# 		nef.writelines([str(i),',',str(ran(0,20)),'\n'])
# 		i+=1

