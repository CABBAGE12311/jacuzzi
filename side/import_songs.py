from pymongo import MongoClient

# Connect to your MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["jacuzzi_db"]
collection = db["songs"]

# Your song data
songs = [
    
    {
        "title": "Eventually",
        "artist": "Tame Impala",
        "album": "Currents",
        "mp3_url": "/media/mp3s/eventually.mp3",
        "cover_art_url": "/media/covers/eventually.jpg"
    },
    
]

# Insert them into the DB
result = collection.insert_many(songs)
print(f"{len(result.inserted_ids)} songs added successfully.")
