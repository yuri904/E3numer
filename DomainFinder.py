import requests
import json
import re
import sys 
from pythonping import ping
import subprocess

def Sectrails(Domain):
    url = "https://api.securitytrails.com/v1/domain/"+Domain+"/subdomains?children_only=false&include_inactive=true"

    headers = {
        "accept": "application/json",
        "APIKEY": "I8ei5ZxqUZbY9EmR7YBQCw6NT7PDwwJX"
    }
    response = requests.get(url, headers=headers)
    jsondata=json.loads(response.text)
    data = jsondata["subdomains"]
    print("Printing all subdomains")
    for domain in data:
        print(f"{domain}.{sys.argv[1]}")
    print("\n")
    print("Printing the alive subdomains:\n")
    for domain in data:
        subdomain = domain + "." + sys.argv[1]
        #print(subdomain)
        try:
            if(ping(subdomain, count=1)):
                print(f"{subdomain}")
                f=open("alive.txt" , "a")
                f.write(subdomain)
                f.write("\n")
            else:
                pass
        except:
            pass
    f.close()
    print("\n")
    
    print("Running Neucli Scanner on the alive ports.")
    subprocess.call(["/usr/bin/nuclei"] , input="alive.txt")
    
   # print("Printing the dead subdomains:\n")
   # print("they might be alive can later...miracles are real :)\n")
   # for domain in data:
   #     subdomain = domain + "." + sys.argv[1]
   #     #print(subdomain)
   #     try:
   #         if(ping(subdomain, count=1)):
   #             pass
   #         else:
   #             print(f"{subdomain}")
   #     except:
   #         pass        
Sectrails(sys.argv[1])

