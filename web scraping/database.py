import pandas as pd
import pymysql

# MySQL database connection parameters
host = 'localhost'
user = 'root'
password = '1314'
database = 'scrapingdata'

# CSV file path
csv_file = 'Newoutput.csv'  # Replace with the path to your CSV file

# Establish a database connection
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    db=database
)

# Create a cursor object
cursor = connection.cursor()

# Read data from the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file)

# Insert data into the MySQL table
try:
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO outputdatas (Title, StarRating, Price, Imageurl, instock) VALUES (%s, %s, %s, %s, %s)",
            (row['Title'], row['StarRating'], row['Price'], row['Imageurl'], row['instock'])
        )

    connection.commit()
    print("Data from CSV file successfully imported into MySQL table")
except Exception as e:
    connection.rollback()
    print("Error:", str(e))
finally:
    cursor.close()
    connection.close()
