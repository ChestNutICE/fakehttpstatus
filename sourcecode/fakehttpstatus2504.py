#!/usr/bin/env python3
import time
import http.client
import ssl
from http.client import HTTPException

#This method read and return users input
def user_input():
	while True:
		url = input("\nPlease enter the url that you need to check: ")
		if url:
            #if it is not empty: return it
			return url
		else:
            #if it is empty: man what can i say
			print("\nMan, just give me a real url instead of nothing.")

  
def main():
    print("\n*****FAKEHTTPSTATUS*****\n")
    print("\n********STARTING********\n")
    print("\n********RUNNING*********\n")
    try:
        context = ssl.create_default_context()
        url = user_input()
        print("\n*******CONNECTING*******\n")
        #customize connection according to user input
        conn = http.client.HTTPSConnection(str(url),443,context= context)
        #get start time
        start = time.time()
        #send request to inputted url and get response
        conn.request("GET","/")
        response = conn.getresponse()
        #get end time
        end = time.time()
        
        #Print results
        print("\nI guess this is what you have rn, bruh: ")
        print(f"\nYOUR URL: {url}")
        print(f"\nSTATUS CODE: {response.status}")
        print(f"\nELAPSED TIME: {end-start} seconds")
    #If connection is not made correctly:
    except Exception as error:
        print("\nDamn dawg, idk what's going on rn, you better check your url!")
        #print err message
        print(f"\n{str(error)}")
    
    finally:
        print("\n*****DISCONNECTING******\n")
        #close connection
        conn.close()
    print("\nThis program works! Congrats!")

if __name__=="__main__":
	main()
