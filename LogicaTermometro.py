import pandas as pd

path = 'Liquidos.xlsx'
data = pd.read_excel(path)

def getliquidList():
    array = data['Líquido'].tolist()
    return array

def get_temperatura_estandar(nombre_liquido):
    liquido_data = data[data['Líquido'] == nombre_liquido]
    temperatura_estandar = liquido_data.iloc[0]['Temperatura estándar (°C)']
    return temperatura_estandar

def get_temperatura_max(nombre_liquido):
    liquido_data = data[data['Líquido'] == nombre_liquido]
    temperatura_maxima = liquido_data.iloc[0]['Punto de ebullición (°C)']
    return temperatura_maxima

def get_temperatura_min(nombre_liquido):
    liquido_data = data[data['Líquido'] == nombre_liquido]
    temperatura_minima = liquido_data.iloc[0]['Punto de congelación (°C)']
    return temperatura_minima
