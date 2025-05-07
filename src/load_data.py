import pandas as pd

def load_online_retail_data(filepath):
    df = pd.read_csv('data/OnlineRetail.csv', encoding='ISO-8859-1')
    df.dropna(subset=['CustomerID'], inplace=True)
    df = df[df['Quantity'] > 0]
    df['InvoiceData'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    return df