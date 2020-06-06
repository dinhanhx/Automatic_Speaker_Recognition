from mfcc_gmm_func import try_personal_GMM
from math import inf
import pickle
import os

names = ['VDA', 'NNDH', 'NQT', 'TQD', 'LHQ', 'LHN', 'DGL', 'TMH']

model_path_list = [name + '/' + name + '.gmm' for name in names]

audio_file_path = '../datasets/VDA/VDA_1.wav'

likelyhood_score_list = []
for model_path in model_path_list:
    if os.path.exists(model_path):
        likelyhood_score_list.append(round(try_personal_GMM(audio_file_path, model_path), 5))
    else:
        likelyhood_score_list.append(-inf)


print('The file is')
print(audio_file_path)
print()
print('The likelyhood score list is')
print(likelyhood_score_list)
print()
print('The person is')
print(names[likelyhood_score_list.index(max(likelyhood_score_list))])
