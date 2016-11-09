import requests
import re

urls = ['http://www.mosigra.ru/']
mails =[]
startUrl = 'http://www.mosigra.ru/'

def  pars (pageUrl):      
    global urls
    global mails
   
    response = requests.get(pageUrl)
    if response.status_code == 200: 
        result = re.findall('href=^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$',response.text)
        result2 = re.findall (r"[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",response.text)
        urlsNew = list(set(result))
        mailsNew = list(set(result2))
        for mail in mailsNew:
            mails.append(mail)
        
        
print('Начало работы')
print('')
pars (startUrl)
mails= set(mails)
for u in mails:
    print (u)
print('')
print('Окончание работы')    


