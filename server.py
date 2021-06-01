## Server - Client Communication

from flask import Flask, render_template, request
from urllib import request
import Main
import Firebase
import os 
import shutil
import scipy.io.wavfile as wav
import json

wav_name = '213F5100_test.wav'
url = 'https://firebasestorage.googleapis.com/v0/b/record-to-script.appspot.com/o/records%2F1617765721495_test2?alt=media&token=ead59f3a-87aa-4e66-96e4-58a05ca87aeb'

'''
app = Flask(__name__)
#app.route('/inference'. methods=['POST'])

@app.route('/', methods=['POST'])

def post():
    value = request.form['name']
    return value
'''

def main():

    #json_data = request.json
    #print(json_data)

    #wav_name = os.path.join(json_data['name'], '.wav')
    #wav_url = data['url']
    #print(savename)

    wavfile = request.urlretrieve(url, wav_name)
    wavfile = request.urlretrieve(url, 'test_wav/'+wav_name)
    #wavfile = request.post(url, auth=("id", "pass"))
    #print(is_dounloadable(url)
    
    script_path = Main.main(wav_name)
    Firebase.main(script_path,wav_name)
    
    #return jsonify(output)



if __name__ == '__main__':
    main()
    #app.run(host='0.0.0.0', port=2431, threaded=False)
