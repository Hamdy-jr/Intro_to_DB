import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your MySQL server host
            user="root",       # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )
        
        # Create a cursor object to interact with the MySQL server
        cursor = connection.cursor()

        # Create the database 'alx_book_store' if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as err:
        # Handle errors while connecting to the MySQL server
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Invalid username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        # Ensure that the cursor and connection are properly closed
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    create_database()
