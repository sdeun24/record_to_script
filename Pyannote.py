#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
from pydub import AudioSegment
from pyannote.audio.features import Pretrained
from pyannote.audio.utils.signal import Binarize
from pyannote.audio.utils.signal import Peak

def SAD(test_file, wav_file,f): #
    sad = Pretrained(validate_dir='../pyannote-audio/tutorials/models/speech_activity_detection/train/AMI.SpeakerDiarization.MixHeadset.train/validate_detection_fscore/AMI.SpeakerDiarization.MixHeadset.development')
    sad_scores = sad(test_file)
    binarize_sad = Binarize(offset=0.52, onset=0.52, log_scale=True, min_duration_off=0.1, min_duration_on=0.1)
    speech = binarize_sad.apply(sad_scores, dimension=1)
    sad_point=[]
    for i in range (len(speech)):
        sad_point.append(round(speech[i].start,3))
        sad_point.append(round(speech[i].end,3))
        
    print("Speech activity detection")
    print("speech")
    f.write("[Speech activity detection]\nspeech\n")
    print(speech)
    print("sad_point")
    print(sad_point)
    real_wav = os.path.join('test_wav', wav_file)
    song = AudioSegment.from_wav(real_wav)
    file_name = wav_file.split('.')[0]
    for i in range(len(speech)):
        startTime=1000*round(speech[i].start,3)
        endTime=1000*round(speech[i].end,3)
        sad_time = "[%.2f -----------> %.2f]\n" % (startTime/1000, endTime/1000)
        f.write(sad_time)
        extract = song[startTime:endTime]
        new_file= "segment/{file_name}/{file_name}_{i}.wav".format(file_name=file_name, i=i)
        extract.export(new_file, format='wav')
    return speech, sad_point


def SCD(wav_file, sad_path, f): #
    scd = Pretrained(validate_dir='../pyannote-audio/tutorials/finetune/train/NEW.SpeakerDiarization.Audio.train/validate_segmentation_fscore/NEW.SpeakerDiarization.Audio.development')
    file_list = os.listdir(sad_path)
    file_list_wav = [file for file in file_list if file.endswith(".wav")]
    total_partition = []
    for sad_file in file_list_wav:
        sad_file_path = sad_path + sad_file
        test_file = {'uri': 'filename', 'audio': sad_file_path}
        scd_scores = scd(test_file)
        peak = Peak(alpha=0.2248, min_duration=0.1, log_scale=True)
        partition = peak.apply(scd_scores, dimension=1)
        total_partition += partition
        scd_point=[]
        print("Speech change detection")
        print("partition")
        f.write("[Speech change detection]\npartition\n")
        print(partition)
        for i in range(len(partition)):
            scd_point.append(round(partition[i].end,3))
        print("scd_point")
        print(scd_point)
        song = AudioSegment.from_wav(sad_file_path)
        file_name = sad_file.split('.')[0]
        for i in range(len(partition)):
            startTime=1000*round(partition[i].start,3)
            endTime=1000*round(partition[i].end,3)
            scd_time = "[%.2f ----------> %.2f]\n" %(startTime/1000, endTime/1000)
            f.write(scd_time)
            extract = song[startTime:endTime]
            new_file= sad_path + "segment/{file_name}_{i}.wav".format(file_name=file_name, i=i)
            extract.export(new_file, format='wav')
    return total_partition, scd_point


def main(wav_file, f):
    real_wav = os.path.join('test_wav', wav_file)
    test_file = {'uri': 'filename', 'audio': real_wav}
    sad_path = 'segment/' + wav_file.split('.')[0] + '/'
    try:
        if not os.path.exists(sad_path):
            os.makedirs(sad_path)
    except OSError:
        print ('Error: Creating directory. ' +  sad_path)
    speech, sad_point = SAD(test_file, wav_file, f)
    scd_path = 'segment/' + wav_file.split('.')[0] + '/segment/'
    try:
        if not os.path.exists(scd_path):
            os.makedirs(scd_path)
    except OSError:
        print ('Error: Creating directory. ' +  scd_path)
    partition, scd_point = SCD(wav_file, sad_path, f)
    return scd_path
