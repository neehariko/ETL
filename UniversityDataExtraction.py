import pandas as pd
import requests
from sqlalchemy import create_engine


def extract() -> dict:
    API_URL="http://universities.hipolabs.com/search?country=United+States"
    data = requests.get(API_URL).json()
    return data
def transform(data:dict) -> pd.DataFrame:
    """ Transforms the dataset into desired structure and filters"""
    df = pd.DataFrame(data)
    print(f"Total Number of universities from API {len(data)}")
    #df = df[df["name"].str.contains("Ohio")]
    #print(f"Number of universities in Ohio {len(df)}")
    df['domains'] = [','.join(map(str, l)) for l in df['domains']]
    df['web_pages'] = [','.join(map(str, l)) for l in df['web_pages']]
    df = df.reset_index(drop=True)
    return df[["domains","country","web_pages","name"]]

def load(df:pd.DataFrame)-> None:
    """ Loads data into a sqllite database"""
    disk_engine = create_engine('sqlite:///my_lite_store.db')
    df.to_sql('All_uni', disk_engine, if_exists='replace')


data = extract()
df = transform(data)
load(df)

print(df.head())






***********************************************************************************************************
Retriving Data from database :


import sqlite3


connection = sqlite3.connect("my_lite_store.db")
connection

cursor = connection.cursor()
cursor

cursor.execute("select * from ohio_uni")
rows = cursor.fetchall()
for row in rows:
    print(row)

