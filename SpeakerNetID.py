#!/usr/bin/python
#-*- coding: utf-8 -*-


class SpeakerNetID(nn.Module):
    def __init__(self, max_frames, lr = 0.0001, margin = 1, scale = 1, hard_rank = 0, hard_prob = 0, model="alexnet50", nOut = 512, nSpeakers = 1000, optimizer = 'adam', encoder_type = 'SAP', normalize = True, trainfunc='contrastive', **kwargs):
        

    def init_speaker_info(self, usr_path): # 회의에 참가한 화자 ID 리스트 저장

    
    def evaluate(self, file_name, num_eval=10): # wav 파일 이름을 받아 ID string을 return
    
        return best_spk

    def store_embedding(self, test_path='', num_eval=10): # test_path에 있는 각 화자의 음성들을 embedding해서 등록


if __name__=='__main__':
    
