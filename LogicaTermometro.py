import pandas as pd

path = 'Liquidos.xlsx'
data = pd.read_excel(path)

def getliquidList():
    
    array = data['Líquido'].to_numpy()
    
    
    return array
