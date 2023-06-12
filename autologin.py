from requests import post

# User Credentials
with open("creds.txt", 'r') as file:
    USERNAME = file.readline().strip()
    PASSWORD = file.readline().strip()
    file.close()

# HEADERS
headers = {
    'Origin': 'http://172.16.0.30:8090',
    'Connection': 'keep-alive',
    'Referer': 'http://172.16.0.30:8090/',
}
data = {
    'mode': '191',
    'username': USERNAME,
    'password': PASSWORD,
}
response = post('http://172.16.0.30:8090/login.xml', headers=headers, data=data)
if response.status_code == 200:
    print("Logged In Successfully!")
else:
    print("LAN is down, Please try again later!")

