import time
import requests

from requests.exceptions import RequestException

def user_input():
	while True:
		url = input("\nPlease enter the url that you need to check: ")
		if url:
			return url
		else:
			print("\nMan, just give me a real url instead of nothing.")
def check_url(url):
	try:
		beginTime = time.time()
		gethttp = requests.get(url, timeout = 5)
		print("\nI guess this is what you have rn, bruh: ")
		print(f"\nYOUR URL: {url}")
		print(f"\nSTATUS CODE: {gethttp.status_code}")
		print(f"\nELAPSED TIME: {gethttp.elapsed.total_seconds()}")
	except RequestException as error:
		print("\nDamn dawg, idk what's going on rn, you better check your url!")
		print(f"\n{str(error)}")
def main():
	print("\n*****FAKEHTTPSTATUS*****")
	print("\n********STARTING********")
	print("\n*********RUNNING********")
	url = user_input()
	check_url(url)
	print("\nThis program works! Congrats!")

if __name__=="__main__":
	main()
