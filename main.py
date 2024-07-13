from config import SqlConnector
import mysql.connector
def main():
    conn = SqlConnector.SqlConnector('secret.txt')
    conn.connect_to_mysql()

if __name__ == "__main__":
    main()
