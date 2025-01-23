from bs4 import BeautifulSoup
#import requests
# import sqlite3
# import csv

try:
    fhand = open('example.html')
    html = fhand.read()
    soup = BeautifulSoup(html, 'html.parser')
    car_details = soup.find('ul', class_='listing-key-specs')
    split_details = list(car_details.stripped_strings)
    print(split_details)
except:
    print('File Not Found')
# finally:
#     fhand.close()
