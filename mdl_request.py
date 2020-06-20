import requests
r = requests.get('https://pythonprogramming.net/yahoo_finance_replacement')

print(r) #response code
# print(dir(r)) #attributes and methods
# print(help(r)) #more detailes
#images are in bytes and text is in unicode(utf-8)
# print(r.text) #site text(string) or r.content.decode('UTF-8') 
# print(type(r.text))
# print(r.encoding)  #type of encoding(ex='utf-8')
# print(r.content) #site content in bytes
# print(r.status_code)  #int(response code)
# print(r.ok) #if the reponse code is less than 400 print True
# print(r.headers) #site information

# payload_1 = {'page': 2, 'count': 25} #in get request,these are parameteres
# req = requests.get('https://httpbin.org/get',params=payload_1) #or (https://httpbin.org/get?page=2&count=25) #to get a site request
# print(req.text) #in json form
# print(req.json()) #in dictionary form
# print(req.url) #print the URL

# payload_2 = {'username':'SAI311','password':'azerty'} #in post request,these are data
# rq = requests.post('https://httpbin.org/post',data=payload_2) #to post the data to the site
# print(rq.text) 
# rq_dict = rq.json()
# print(rq_dict)
# print(rq_dict['form']) #print element in dictionary

# at = requests.get('http://httpbin.org/basic-auth/islam/sai', auth=('islam','sai')) #get(http://httpbin.org/basic-auth/{user}/{password}) auth=(put_username,put_password)
# print(at.text) #if auth={user}/{password} print text
# print(at) #response code
# print(at.status_code) #int(response code)
# at = requests.get('http://httpbin.org/basic-auth/islam/sai', auth=('abc','efg'))
# print(at.text) #if auth!={user}/{password} dont print text
# print(at) #response code
# print(at.status_code) ##int(response code)
# at = requests.get('http://httpbin.org/delay/3') #('http://httpbin.org/delay/3')=delay 3 seconds before excute
# at = requests.get('https://httpbin.org/get',timeout=2) #('https://httpbin.org/get',timeout=2)=if it dosnt excute,timeout
# at = requests.get('http://httpbin.org/delay/5',timeout=4)




'''
response code:

informational responses (100–199)
Successful responses (200–299)
Redirects (300–399)
Client errors (400–499)
Server errors (500–599)



more information about requests:('http://httpbin.org')
'''








