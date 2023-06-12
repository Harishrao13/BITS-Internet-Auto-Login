from requests import post
from sys import exit

# User Credentials
def credentials():
    with open("creds.txt", 'r') as file:

        USERNAME = file.readline().strip(" ")
        if USERNAME == "f20xxxxxx":
            print('Please enter your Sophos Login credentials in creds.txt')
            file.close()
            exit()
        else:
            return USERNAME
        file.close()


USERNAME = credentials()

headers = {
    'Origin': 'http://172.16.0.30:8090',
    'Connection': 'keep-alive',
    'Referer': 'http://172.16.0.30:8090/',
}

data = {
    'mode': '193',
    'username': USERNAME,
    'producttype': '0',
}

response = post('http://172.16.0.30:8090/login.xml', headers=headers, data=data)
if response.status_code == 200:
    print("Logged Out Successfully!")
else:
    print("LAN is down, Please try again later!")
