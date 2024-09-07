import requests
from random import randint
from time import sleep

url = 'http://127.0.0.1:8000/upload'
while True:
	file = {'file': open("./test images/test"+str(randint(0,3))+".png", 'rb')}
	sleep(randint(1, 2))
	resp = requests.post(url=url, files=file) 
	print(resp.json())