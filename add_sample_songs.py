from pymongo import MongoClient

def add_sample_songs():
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['jacuzzi_db']
        songs_collection = db['songs']
        
        # Sample songs data
        songs = [
            {
                'title': 'The Pot',
                'artist': 'Tool',
                'album': '10,000 Days'
            },
            {
                'title': 'Stairway to Heaven',
                'artist': 'Led Zeppelin',
                'album': 'Led Zeppelin IV'
            },
            {
                'title': 'Bohemian Rhapsody',
                'artist': 'Queen',
                'album': 'A Night at the Opera'
            }
        ]
        
        # Clear existing songs
        songs_collection.delete_many({})
        
        # Insert new songs
        result = songs_collection.insert_many(songs)
        print(f'Successfully added {len(result.inserted_ids)} sample songs to the database!')
        
        # Verify the songs were added
        print('\nCurrent songs in database:')
        for song in songs_collection.find():
            print(f"- {song['title']} by {song['artist']} ({song['album']})")
            
    except Exception as e:
        print(f'Error: {str(e)}')
    finally:
        client.close()

if __name__ == '__main__':
    add_sample_songs()