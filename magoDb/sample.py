from pymongo import MongoClient

# Define the fields to be stored in the MongoDB document
data = {
    "lex": "value1",
    "tokens": "value2",
    "fullCode": "value3",
    "ast": "value4",
    "parser": "value5",
    "result": "value6",
    "context": "value7",
    "symbolTable": "value8",
    "executionTime": 123456,
    "resultValue": "value9"
}

# MongoDB connection URI
uri = "mongodb+srv://nagi:nagi@cluster0.ohv5gsc.mongodb.net/nagidb"

# Connect to MongoDB
client = MongoClient(uri)

# Access a specific database
db = client.Astrology

# Access a specific collection within the database
collection = db.your_collection_name

# Insert the document into the collection
insert_result = collection.insert_one(data)

# Check if the insertion was successful
if insert_result.inserted_id:
    print("Document inserted successfully.")
else:
    print("Failed to insert document.")
