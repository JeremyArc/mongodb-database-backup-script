import pandas as pd
import pymongo
from datetime import datetime
import getpass


def getMongoDBCredentials():
    print("Please enter mongodb credential data...")
    host = input("Enter MongoDB host (default: localhost): ") or "localhost"
    port = input("Enter MongoDB port (default: 27017)") or "27017"
    username = input("Enter database username (default: root) ") or "root"
    password = getpass.getpass("Enter password (default: example) ") or "example"
    databaseName = input("Enter database name:")
    print(f"Received credentials => host:{host}, port:{port}, databaseName:{databaseName}, username:{username}, password:{password}")
    return {
        "host": host,
        "port": port,  
        "username": username,
        "password": password,
        "databaseName": databaseName
    }

def constructMongoDBConnectionUri(host, port, username, password):
    print("Constructing database connection uri...")
    uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"
    print(f"Constructed uri: {uri}")
    return uri

def backupMongodDBCollectionToCSV(mongoDBUri, databaseName, collectionName):
    client = pymongo.MongoClient(mongoDBUri)
    database = client[databaseName]
    collection = database[collectionName]

    print(f"Fetching data from database's collection...")
    data = collection.find()
    print(data)

    dataList = list(data)
    print(f"dataList: {dataList}")

    print(f"Framing data from fetched data...")
    df = pd.DataFrame(dataList)
    print(f"Framed data = {df}")

    # Define the backup file name with timestamp
    backupFilePath = f"backup_{databaseName}_{collectionName}_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"

    print(f"Saving data to csv...")
    df.to_csv(backupFilePath, index=False)

    print(f"Backup saved to {backupFilePath}")

def main():
    credentials = getMongoDBCredentials()
    mongoDBConnectionUri = constructMongoDBConnectionUri(credentials["host"], credentials["port"], credentials["username"], credentials["password"])
    collectionName = input("Enter collection name: ")
    backupMongodDBCollectionToCSV(mongoDBConnectionUri, credentials["databaseName"], collectionName)


# In Python, each module has a special built-in attribute called __name__.
# When a module is run directly, the __name__ attribute is set to '__main__'.
# However, when a module is imported from another module, the __name__ attribute is set to the module's name.
# The line if __name__ == "__main__": is used to check whether the script is being run directly or being imported as a module in another script.

if __name__ == "__main__":
    main()