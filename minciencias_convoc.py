#importing some modules
import requests
import html5lib
from bs4 import BeautifulSoup as bsp
from datetime import date, timedelta
import pandas as pd
from email.message import EmailMessage
import ssl # intern conectio secure - ass a layer of security
import smtplib
from email.mime.text import MIMEText
import lxml
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
import os

#other setting
disable_warnings(InsecureRequestWarning)


class mincienciasConvoc:

  def __init__(self, web, mainWeb, mailsList, frequency = None, nPages = None):
    
    self.__web = web
    self.__mainWeb = mainWeb
    self.mails = mailsList

    self.__n = nPages if nPages else 5 # the n_pages is optional and the default is 5
    self.__f = frequency if frequency else 7 # the periodicity to run the code


    self.newones = pd.DataFrame()



  def mostRecentTable(self):
   
    """This read all the df and identifies the most recent one """
    
    
    try:
      filesInFolder = sorted(os.listdir("dataFrames"))
    except:
      print("there are not files to compare")
    else:
      self.mostRecentTab = pd.read_pickle(f"dataFrames/{filesInFolder[-1]}")
      return self.mostRecentTab

  
  def __get_links(self, n=None):

    """it gives me the links of the n_pages"""
    
    resp = requests.get(self.__web, verify =False) # reading the web
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
  
  
  def get_allTable(self):

    """it reads all the tables in each webpage from all pages and concatenates them"""

    links = self.__get_links('all')
    self.allTable = pd.concat([pd.read_html(i)[0] for i in links]).reset_index(drop=True)
    return self.allTable
  

  def save(self):

    """it saves the table"""
    
    self.table.to_pickle(f"dataFrames/df_{date.today()}")

  
  def delete(self):

    """it delete the oldest tables"""
    
    try:
      filesInFolder = sorted(os.listdir("dataFrames"))
    except:
      print("there are not files to delete")
    else:
      if len(filesInFolder) > 4 :
        [os.remove(f"dataFrames/{i}") for i in sorted(filesInFolder)[:-4]]
      

 
  def comparing(self):
    
    """it creates a new table if there is other table to compare """
    
    other = pd.DataFrame()
    other = self.mostRecentTab

    if len(other) != 0 :
      merging = self.table.merge(other, how = 'outer', indicator=True)
      self.newones = merging.loc[merging['_merge']=='left_only'].reset_index(drop = True)
      self.newones.drop('_merge', inplace = True, axis = 1)
    #else:
    #  print("there is not table (mostRecentDF) to compare")



  
  def comparingOld(self):

    """it review if there is previous files-df to compare with the actual df.
    Then review if there are differences between them: when differences gives a df if not 0 """

    last = self.__f
    other = pd.DataFrame()

    try:
      other = pd.read_pickle(f"dataFrames/df_{date.today() - timedelta(days=last)}")
    except:
      try:
        other = pd.read_pickle(f"dataFrames/df_{date.today() - timedelta(days=last*2)}")
      except:
        print(f"there are not files for the last 2 runs")

    if len(other) != 0 :
      merging = self.table.merge(other, how = 'outer', indicator=True)
      self.newones = merging.loc[merging['_merge']=='left_only'].reset_index(drop = True)
      self.newones.drop('_merge', inplace = True, axis = 1)
     

  def emailing(self):

    """it sends an mail if there is new 'convocatorias' 
    This function is ONLY use if  newones != 0. Thats the reason why it is 
    private method"""

    email_sender = 'fisicaminciencias@gmail.com'
    email_password = 'nloaavzcczqaijyd' 
    email_receiver = self.mails
    
    html = f""" <html><head></head><body>
    <p>
    
    Estas son las nuevas convocatorias de MINCIENCIAS:<p>  
    
    {self.newones.to_html()}
    
    <p> Revisa 'https://minciencias.gov.co/convocatorias/todas' para información sobre las convocatorias <br>
        Revisa  https://github.com/LinaMRuizG/minciencias_convocatorias para información sobre este proyecto <p> 
    Good luck!<br>
    be happy!<p> 

    </body></html>"""
    body = MIMEText(html, 'html')
    subject = 'Nuevas convocatorias MINCIENCIAS'

    em=EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465, context = context) as smtp:
      smtp.login(email_sender,email_password)
      smtp.sendmail(email_sender, email_receiver, em.as_string())

  def run(self):
    
    """it runs the methods"""
    
    self.mostRecentTable()
    
    self.get_table()
    self.save()
    self.delete()
    
    self.comparing()
    print("No hay nuevas convocatorias") if self.newones.shape[0] == 0 else self.emailing()
    

    




  
  

