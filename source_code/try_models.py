from mfcc_gmm_func import try_personal_GMM
from math import inf
import os

audio_file_path = ''
model_type = ''

names = ['VDA', 'NNDH', 'NQT', 'LHQ', 'TQD', 'LHN', 'TMH', 'DGL']
model_path_list = ['models/'+model_type+'/'+name+'.gmm' for name in names]

scores = []
for model_path in model_path_list:
    if os.path.exists(model_path):
        scores.append(round(try_personal_GMM(audio_file_path, model_path),5))
    else:
        scores.append(-inf)


print('The file: ' + audio_file_path + '\n')
print('The likelihood score list: ')
names_scores = [name+': '+str(score) for name, score in zip(names, scores)]
print(*names_scores, sep = '\n')
print('\n' + 'The likelhood person: '+names[scores.index(max(scores))])
