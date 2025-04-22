from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["jacuzzi_db"]
artists = db["artists"]

artist_data = [
    {"name": "Tool", "image_url": "/media/artists/tool.jpg"},
    {"name": "Queen", "image_url": "/media/artists/queen.jpg"},
    {"name": "Led Zeppelin", "image_url": "/media/artists/led_zeppelin.jpg"},
    {"name": "Pink Floyd", "image_url": "/media/artists/pink_floyd.jpg"},
    {"name": "Joji", "image_url": "/media/artists/joji.jpg"},
    {"name": "Radiohead", "image_url": "/media/artists/radiohead.jpg"},
    {"name": "Tyler, The Creator", "image_url": "/media/artists/tyler.jpg"},
    {"name": "Mac DeMarco", "image_url": "/media/artists/mac.jpg"},
    {"name": "The Strokes", "image_url": "/media/artists/strokes.jpg"},
    {"name": "The Cranberries", "image_url": "/media/artists/cranberries.jpg"},
    {"name": "Kendrick Lamar", "image_url": "/media/artists/kendrick.jpg"},
    {"name": "AC/DC", "image_url": "/media/artists/acdc.jpg"},
    {"name": "Guns N' Roses", "image_url": "/media/artists/gnr.jpg"},
    {"name": "Peter Cat Recording Co.", "image_url": "/media/artists/pcrc.jpg"},
    {"name": "Lifafa", "image_url": "/media/artists/lifafa.jpg"},
    {"name": "Arctic Monkeys", "image_url": "/media/artists/arctic_monkeys.jpg"}
]

result = artists.insert_many(artist_data)
print(f"{len(result.inserted_ids)} artists added.")
