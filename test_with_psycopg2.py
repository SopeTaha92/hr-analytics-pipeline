

import pandas as pd
import psycopg2
from config import DB_CONFIG, TABLE_NAME
#file = config.BRUTE_DATA_FILE
#df = pd.read_csv(file)

try:
    conn = psycopg2.connect(**DB_CONFIG)
    print('testing connection !')
    df = pd.read_sql(f"SELECT * FROM {TABLE_NAME};", conn)
    print("✅ Connexion réussie !")
    conn.close()
    print(df.head(10))
except Exception as e:
    print(f"ERREUR : {e}")
