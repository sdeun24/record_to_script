import os
import sys
import speech_recognition as sr
import Pyannote
import Identify

class STT:
    def __init__(self, wav_name):
        self.wav_name = wav_name
        self.result_file_name = wav_name.split('.')[0] + '.txt'
        self.language_code = 'ko'

    def run(self, seg_path, f): # wav 파일의 이름을 받아 그 파일의 STT결과 string을 text 파일에 append mode로 write
        file_list = os.listdir(seg_path)
        spk_list = os.listdir('source/test/')
        for idx, segment in enumerate(file_list):
            AUDIO_FILE = seg_path + segment
            speaker_id = Identify.main(AUDIO_FILE)
            r = sr.Recognizer()
            with sr.AudioFile(AUDIO_FILE) as source:
                audio = r.record(source)
            print('[Segment] ' + speaker_id + ': ' + r.recognize_google(audio, language=self.language_code))
            f.write('[Segment] ' + speaker_id + ': ' + r.recognize_google(audio, language=self.language_code) + '\n')       

def main(wavfile):
    script_path = os.path.join('scripts/', wavfile)
    script_file = open(script_path + '.txt', 'w')
    script_file.write('****************************\nSpeaker Identification\n**************************\n\n')
    stt=STT(wavfile)

    segment_path = Pyannote.main(wavfile, script_file)
    stt.run(segment_path, script_file)
    return (script_path)
