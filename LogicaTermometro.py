import pandas as pd

path = 'Liquidos.xlsx'
data = pd.read_excel(path)

def getliquidList():
    
    liquidlist = data['Líquido']
    
    return liquidlist

print(getliquidList())