#importing some modules
import requests
from bs4 import BeautifulSoup as bsp
from datetime import date, timedelta
import pandas as pd
from email.message import EmailMessage
import ssl # intern conectio secure - ass a layer of security
import smtplib
from email.mime.text import MIMEText

class mincienciasConvoc:

  def __init__(self, web, mainWeb, nPages = None):
    self.__web = web
    self.__mainWeb = mainWeb
    self.__n = nPages if nPages else 5 # the n_pages is optional and the default is 5
  
  def __get_links(self, n=None):

    """it gives me the links of the n_pages"""
    
    resp = requests.get(self.__web) # reading the web
    lastPage = bsp(resp.text, features="html.parser").find("li", "pager-last last")# looking in the soup the lastPage
    http = lastPage.findChild("a")['href']# looking more into lastPage
    splitedHttp = http.split('page=')

    nlast = int(splitedHttp[-1]) if n == 'all' else self.__n
    self.links = [self.__web] + [self.__mainWeb + splitedHttp[0]+ 'page=' + str(i) for i in range(1, nlast)]

    return self.links

  def get_table(self):

    """it reads all the tables in each webpage from 1 to nPages and concatenates them"""

    links = self.__get_links()
    self.table = pd.concat([pd.read_html(i)[0] for i in links]).reset_index(drop=True)
    return self.table
  
  

