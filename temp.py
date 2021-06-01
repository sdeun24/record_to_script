import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db
from google.cloud import storage
import os
import json

script_path = "scripts/test.wav.txt"
wav_name = "test.wav"

def main():

    client = storage.Client(projcet='project-41653037768')
    firebase_admin.initialize_app(cred, {
        'storageBucket' : 'gs://record-to-script.appspot.com'})
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('scripts')
    blob = bucket.blob(script_path)
    blob.upload_from_filename(script_path)
    #store_st(script_path)
    print("success")


if __name__ == '__main__':
    main()

