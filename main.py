import requests
import bs4 as BeautifulSoup
import sys
import os
import csv

START_AT_ROW = 3
CSV_NAME = "export.csv"

def scrap_that_very_protected_google_sheets(url):

    params = "/preview/sheet?gid=0"
    html = requests.get(url+params).text
    soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')

    for e in soup.find_all('br'):
        e.replace_with(' ')

    dir_path = os.path.dirname(os.path.realpath(__file__))
    csv_file = os.path.join(dir_path, CSV_NAME)
    f = csv.writer(open(csv_file, "w", encoding="utf-8", newline=''))
    rows =  soup.find_all('tr')[START_AT_ROW:]
    for row in rows:
        cells = row.find_all('td')
        csv_row = ''
        for cell in cells:
            csv_row += cell.get_text() + ';'
        f.writerow([csv_row])


protected_doc_url = "https://docs.google.com/spreadsheets/d/10QtMPw3Cs-rGl0K2P5ct1u9NM1rT7ySdnd59jhAHyzw"
scrap_that_very_protected_google_sheets(protected_doc_url)


                                                                  
# 88                                88                              
# 88                                88                              
# 88                                88                              
# 88,dPPYba,  ,adPPYYba,  ,adPPYba, 88   ,d8  ,adPPYba, 8b,dPPYba,  
# 88P'    "8a ""     `Y8 a8"     "" 88 ,a8"  a8P_____88 88P'   "Y8  
# 88       88 ,adPPPPP88 8b         8888[    8PP""""""" 88          
# 88       88 88,    ,88 "8a,   ,aa 88`"Yba, "8b,   ,aa 88          
# 88       88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a `"Ybbd8"' 88                  lmao.       
                                                                  
                                                                  
