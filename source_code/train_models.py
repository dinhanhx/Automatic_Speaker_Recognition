from mfcc_gmm_func import *
from random import shuffle

names = ['VDA', 'NNDH', 'NQT', 'LHQ', 'TQD', 'LHN', 'TMH', 'DGL']
model_type = 'high'
test_type = 'high'

# Train models
for name in names:
    audio_fpath_list = []
    for i in range(1, 101):
        audio_fpath = '../datasets/'+model_type+'/'+name+'/'+name+'_'+str(i)+'.wav'
        audio_fpath_list.append(audio_fpath)


    model_path = 'models/'+model_type+'/' + name + '.gmm'
    shuffle(audio_fpath_list)
    generate_GMM(audio_fpath_list, model_path)
    print(model_path)


# For testing models
total_miss = 0
total_hit = 0
for name in names:
    miss = 0
    hit = 0
    audio_fpath_list = []
    for i in range(101, 136):
        audio_fpath = '../datasets/'+test_type+'/' + name + '/' + name + '_' + str(i) + '.wav'
        audio_fpath_list.append(audio_fpath)


    model_path_list = ['models/'+model_type+'/' + name + '.gmm' for name in names]
    for audio_fpath in audio_fpath_list:
        scores = []
        for model_path in model_path_list:
            scores.append(round(try_personal_GMM(audio_fpath, model_path), 5))

        if name != names[scores.index(max(scores))]:
            miss = miss + 1
            total_miss = total_miss + miss
        else:
            hit = hit + 1
            total_hit = total_hit + hit


    print('Test with .wav files of ' + name + '. System miss: ' + str(miss) + '. System hit: ' + str(hit))


accuracy = (total_hit/(total_hit+total_miss))*100
print('Accuray: '+str(round(accuracy,5))+'%')
