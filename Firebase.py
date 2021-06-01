import firebase_admin
from firebase_admin import credentials, firestore, db
from google.cloud import storage
import os
import json

#script_path = "scripts/test1.wav"
#wav_name = "test.wav"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "store-record-to-script.json"

def store_db(script, wav_name): #store to database

    db = firestore.client()

    file_name = os.path.splitext(wav_name)[0]
    f = open(script, "r")
    
    doc = db.collection('scripts').document(file_name)
    doc.set({
        'wav_name' : wav_name,
        'script' : f.readlines()
    })

def store_st(script):
    
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('record-to-script.appspot.com')
    blob = bucket.blob(script)
    blob.upload_from_filename(script)

def main(script_path, wav_name):
    
    cred = credentials.Certificate('db-record-to-script.json')
    firebase_admin.initialize_app(cred)
    store_db(script_path+'.txt', wav_name)    
    store_st(script_path+'.txt')
    print("\nSuccessful save to DB and Storage\n")


if __name__ == '__main__':
    main()

