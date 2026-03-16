import psycopg2
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Creating Connection with postgresql
def get_connection():
    try:
        conn=psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return conn
    
    except Exception as e:
        print('Database connection failed !! ',e)
        return None
    
# Establishing the connection
conn=get_connection()
if conn:
    print('Connection established !!')
else:
    print('Connection Failed !!')
    
# Creating Cursor
cursor=conn.cursor()