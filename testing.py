#importing some modules
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import pandas as pd
from email.message import EmailMessage
import ssl # intern conectio secure - ass a layer of security
import smtplib
from email.mime.text import MIMEText

#setting the dataframes display
pd.set_option("display.max_colwidth", None)
pd.set_option('display.width', 30)
pd.set_option('display.max_rows', None)
pd.set_option("display.max_column", None)

#defining my class
class minciencias_convoc:
    
    def __init__(self, webpage, main_web,n_pages = None):
         """An instance of this class is a DataFrame"""
         self.__webpage = webpage
         self.__n = n_pages if n_pages else 10 # the n_pages is optional and the default is 10
         self.__main_web = main_web

    def get_links(self,n=None):
        
        """it gives the links of the n pages"""
        resp = requests.get(self.__webpage) #reading the web
        part_with_lastPage = BeautifulSoup(resp.text).find("li","pager-last last")#getting a key part with the last page
        http_str = part_with_lastPage.findChild("a")['href']# getting part of the http as str
        splited_str = http_str.split('page=') 
        
        last = int(splited_str[-1]) if n == 'all' else self.__n
        
        self.links = [self.__webpage] + [self.__main_web + splited_str[0] + 'page=' + str(i) for i in range(1, last)]
        return self.links
    
web = 'https://minciencias.gov.co/convocatorias/todas'
main_web ='https://minciencias.gov.co'
convocat = minciencias_convoc(web,main_web,3)
convocat.get_links()