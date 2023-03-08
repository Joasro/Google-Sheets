from SortClass import *
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import random


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'C:/Users/joaqu/Desktop/GoogleSheetss/Key.json'
SPREADSHEET_ID = '1ygT16dc302h5Z4JVXNaGF7kaK_7Vf_mXT8jM5TFfbWg'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

def initArray(size=10, maxValue=200, seed=3.1415926):
    lista = Array(size)                   
    random.seed(seed)                   
    for i in range(size):              
        lista.insert(random.randrange(maxValue)) 
    return lista                          

pylit = initArray()

print("Numeros ingresados:")

pylit.traverse()
print('Contenido de la matriz desordenada:\n', pylit)
Nlist = [[pylit.get(i)] for i in range(len(pylit))]
range_ ='A2:A8' 
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range_,
							valueInputOption='USER_ENTERED',
							body={'values':Nlist}).execute()
print(f"Datos insertados.\n{(result.get('updates').get('updatedCells'))}")



pylit.bubbleSort()
print('Agregado Bubble Sort')
Nlist = [[pylit.get(i)] for i in range(len(pylit))]
range2_ ='B2:B8' 
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range2_,
							valueInputOption='USER_ENTERED',
							body={'values':Nlist}).execute()
print(f"Datos de Bubble insertados.\n{(result.get('updates').get('updatedCells'))}")



pylit.insertionSort()
print('Agregado Insertion sort')
Nlist = [[pylit.get(i)] for i in range(len(pylit))]
range4_ ='D2:D8' 
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range4_,
							valueInputOption='USER_ENTERED',
							body={'values':Nlist}).execute()
print(f"Datos de Insertion insertados.\n{(result.get('updates').get('updatedCells'))}")



pylit.selectionSort()
print('Agregado Insertion sort')
Nlist = [[pylit.get(i)] for i in range(len(pylit))]
range3_ ='C2:C8' 
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range3_,
							valueInputOption='USER_ENTERED',
							body={'values':Nlist}).execute()
print(f"Datos de Selection insertados.\n{(result.get('updates').get('updatedCells'))}")






