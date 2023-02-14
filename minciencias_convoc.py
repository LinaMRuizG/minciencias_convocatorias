#importing some modules
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import pandas as pd
from email.message import EmailMessage
import ssl # intern conectio secure - ass a layer of security
import smtplib
from email.mime.text import MIMEText

class mincienciasConvoc:

  def __init__(self, web, main_web):
    self.web = web
    self.main_web = main_web
  
  def get_links(self):
    print(f"{self.web}, {self.main_web}")