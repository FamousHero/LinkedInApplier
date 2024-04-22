#First python script in years so not comepletely compliant with standard
#hard-coding csrf value and other web form values until it breaks
from dotenv import load_dotenv
import os
import requests
x = requests.get('https://w3schools.com/python/demopage.htm')

class LinedInBot:
    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password
def main():
    load_dotenv('.env')
    login =  os.getenv('LOGIN')
    password = os.getenv('Password') 
    LinedInBot(login, password)
    print(x.text)
    print("hello world") 

if __name__ == "__main__":
    main()