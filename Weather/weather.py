import requests
from pprint import pprint
def main():
	city="India"
	response=request.get("openweathermap.org link with id") #get it from openweathermap.org
	weather=response.json()
	# pprint weather # see it
	print "weather for "weather['name']
	print weather['main']['temp'] #geting temperature
	print weather['weather'][0]['description']
if '__name__'=='__main__':
	main() 