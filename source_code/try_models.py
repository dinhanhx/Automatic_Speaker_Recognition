from mfcc_gmm_func import try_personal_GMM
from math import inf
import pickle
import os

names = ['VDA', 'NNDH', 'NQT', 'LHQ', 'TQD', 'LHN', 'TMH', 'DGL']

model_path_list = [name + '/' + name + '.gmm' for name in names]

audio_file_path = '../datasets/VDA/notinlab.wav'

likelihood_score_list = []
for model_path in model_path_list:
    if os.path.exists(model_path):
        likelihood_score_list.append(round(try_personal_GMM(audio_file_path, model_path), 5))
    else:
        likelihood_score_list.append(-inf)


print('The file: ' + audio_file_path + '\n')
print('The likelihood score list: ')
name_likelihood_score = [name + ': ' + str(likelihood_score) for name, likelihood_score in zip(names, likelihood_score_list)] 
print(*name_likelihood_score, sep = '\n')
print('\n' + 'The likelhood person: '+names[likelihood_score_list.index(max(likelihood_score_list))])
