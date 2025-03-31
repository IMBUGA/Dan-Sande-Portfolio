import mysql.connector # type: ignore

# Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user="root", # Add user
    password="OLDER$2024" # Add your password
)

# Create a cursor object
cursor = conn.cursor()

# Create a new database
database_name = "SN METIT" # Add a unique Database name
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

print(f"Database '{database_name}' created successfully!")

# Close the connection
cursor.close()
conn.close()