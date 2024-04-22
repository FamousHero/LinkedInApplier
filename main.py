#First python script in years so not comepletely compliant with standard
#hard-coding csrf value and other web form values until it breaks
from dotenv import load_dotenv
from bs4 import _soup
import os
import requests


class LinedInBot:
    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password
        self.client = requests.Session()
        #scoped to static var so i not global at least
        self._homepageURL = 'https://www.linkedin.com'
        self._loginURL = 'https://www.linkedin.com/uas/login=submit'

    def LoadSoup(self, url):
        """
        Helper function to feed html response to soup parser
        """
        html = self.client.get(url)
        soup = _soup(html.text, "html.parser")
        return soup

    #
    def Homepage(self):
        """
        Load the homepage and returned a parsed html version 
        """
        soup = self.LoadSoup(self._homepageURL)
        return soup

    def Run(self):
        """Base method IYKYK"""
        print(self.password)
        print(self.login)
        self.Homepage()

def main():
    load_dotenv('.env')
    login: str =  os.getenv('LOGIN')
    password: str = os.getenv('Password') 
    friend = LinedInBot(login, password)
    friend.Run()

if __name__ == "__main__":
    main()